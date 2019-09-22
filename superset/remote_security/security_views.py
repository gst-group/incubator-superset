# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from flask import g, redirect, flash
from flask_appbuilder._compat import as_unicode
from flask_appbuilder.forms import DynamicForm
from flask_appbuilder.security.views import AuthRemoteUserView, expose
from flask_babel import lazy_gettext
from flask_login import login_user
from wtforms import StringField, PasswordField
from wtforms.validators import Required
from flask import request
# import the remote server here
# remote server API to authenticate username
from . import remote_server_api

import logging
logger = logging.getLogger(__name__)


class MyLoginForm(DynamicForm):
    """
    My customize login form, only set telephone and password as login request
    more options could be set here
    """
    telephone = StringField(
        lazy_gettext('telephone'), validators=[Required()])
    password = PasswordField(lazy_gettext("Password"), validators=[Required()])


class MyAuthRemoteUserView(AuthRemoteUserView):
    # this front-end template should be put under the folder `superset/templates/appbuilder/general/security`
    # so that superset could find this templates to render
    login_template = 'appbuilder/general/security/login.html'
    title = "账号登陆"

    def process_user(self, my_user):
        # if my_user is authenticated
        if my_user:
            user = self.appbuilder.sm.auth_user_remote_user(
                my_user.get('username'))
            if user is None:
                flash(as_unicode(self.invalid_login_message), 'warning')
            else:
                login_user(user)
                return redirect(self.appbuilder.get_url_for_index)
        else:
            flash(as_unicode(self.invalid_login_message), 'warning')

    # this method is going to overwrite 
    # https://github.com/dpgaspar/Flask-AppBuilder/blob/master/flask_appbuilder/security/views.py#L556
    @expose('/login/', methods=['GET', 'POST'])
    def login(self):
        logger.info("My special login...")
        if g.user is not None and g.user.is_authenticated:
            return redirect(self.appbuilder.get_url_for_index)

        form = MyLoginForm()
        my_user = None
        result = None
        token = request.args.get('access_token')
        if request.method == "GET" and token:
            my_user = remote_server_api.authenticate_with_token(token)
            if my_user:
                result= self.process_user(my_user)
                if result:
                    return result;
        elif form.validate_on_submit():
            logger.info("going to auth MY user: %s" % form.telephone.data)
            my_user = remote_server_api.authenticate(form.telephone.data, form.password.data)
            result= self.process_user(my_user)
            if result:
                return result;
        else:
            if form.errors.get('telephone') is not None:
                flash(
                    as_unicode(" ".join(form.errors.get('telephone'))), 'warning')

        return self.render_template(
            self.login_template,
            title=self.title,
            form=form,
            appbuilder=self.appbuilder)