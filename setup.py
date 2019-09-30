# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import io
import json
import os
import subprocess
import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 6):
    sys.exit("Sorry, Python < 3.6 is not supported")

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

PACKAGE_JSON = os.path.join(BASE_DIR, "superset", "assets", "package.json")
with open(PACKAGE_JSON, "r") as package_file:
    version_string = json.load(package_file)["version"]

with io.open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


def get_git_sha():
    try:
        s = subprocess.check_output(["git", "rev-parse", "HEAD"])
        return s.decode().strip()
    except Exception:
        return ""


GIT_SHA = get_git_sha()
version_info = {"GIT_SHA": GIT_SHA, "version": version_string}
print("-==-" * 15)
print("VERSION: " + version_string)
print("GIT SHA: " + GIT_SHA)
print("-==-" * 15)

VERSION_INFO_FILE = os.path.join(
    BASE_DIR, "superset", "static", "assets", "version_info.json"
)

with open(VERSION_INFO_FILE, "w") as version_file:
    json.dump(version_info, version_file)


setup(
    name="apache-superset",
    description=("A modern, enterprise-ready business intelligence web application"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=version_string,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts=["superset/bin/superset"],
    install_requires=[
        "alembic==1.0.11",
        "amqp==2.5.0",
        "apispec[yaml]==1.3.3",
        "asn1crypto==0.24.0",
        "attrs==19.1.0",
        "babel==2.7.0",
        "backoff==1.8.0",
        "billiard==3.6.0.0",
        "bleach==3.1.0",
        "celery==4.3.0",
        "cffi==1.12.3",
        "click==6.7",
        "colorama==0.4.1",
        "contextlib2==0.5.5",
        "croniter==0.3.30",
        "cryptography==2.7",
        "decorator==4.4.0",
        "defusedxml==0.6.0",
        "flask-appbuilder==2.1.13",
        "flask-babel==0.12.2",
        "flask-caching==1.7.2",
        "flask-compress==1.4.0",
        "flask-jwt-extended==3.20.0",
        "flask-login==0.4.1",
        "flask-migrate==2.5.2",
        "flask-openid==1.2.5",
        "flask-sqlalchemy==2.4.0",
        "flask-talisman==0.7.0",
        "flask-wtf==0.14.2",
        "flask==1.1.1",
        "future==0.17.1",
        "geographiclib==1.49",
        "geopy==1.20.0",
        "gunicorn==19.8.1",
        "humanize==0.5.1",
        "isodate==0.6.0",
        "itsdangerous==1.1.0",
        "jinja2==2.10.1",
        "jsonschema==3.0.1",
        "kombu==4.6.3",
        "mako==1.0.14",
        "markdown==3.1.1",
        "markupsafe==1.1.1",
        "marshmallow-enum==1.4.1",
        "marshmallow-sqlalchemy==0.17.0",
        "marshmallow==2.19.5",
        "msgpack==0.6.1",
        "numpy==1.17.0",
        "pandas==0.24.2",
        "parsedatetime==2.4",
        "pathlib2==2.3.4",
        "polyline==1.4.0",
        "prison==0.1.2",
        "py==1.8.0",
        "pyarrow==0.14.1",
        "pycparser==2.19",
        "pyjwt==1.7.1",
        "pyrsistent==0.15.4",
        "python-dateutil==2.8.0",
        "python-dotenv==0.10.3",
        "python-editor==1.0.4",
        "python-geohash==0.8.5",
        "python3-openid==3.1.0",
        "pytz==2019.2",
        "pyyaml==5.1.2",
        "retry==0.9.2",
        "selenium==3.141.0",
        "simplejson==3.16.0",
        "six==1.12.0",
        "sqlalchemy-utils==0.34.1",
        "sqlalchemy==1.3.6",
        "sqlparse==0.3.0",
        "urllib3==1.25.3",
        "vine==1.3.0",
        "webencodings==0.5.1",
        "werkzeug==0.15.5",
        "wtforms-json==0.3.3",
        "wtforms==2.2.1",
        "black==19.3b0",
        "coverage==4.5.3",
        "flake8-import-order==0.18.1",
        "flake8-mypy==17.8.0",
        "flake8==3.7.7",
        "flask-cors==3.0.7",
        "ipdb==0.12",
        "mypy==0.670",
        "nose==1.3.7",
        "pip-tools==3.7.0",
        "pre-commit==1.17.0",
        "psycopg2-binary==2.7.5",
        "pycodestyle==2.5.0",
        "pydruid==0.5.6",
        "pyhive==0.6.1",
        "pylint==1.9.2",
        "redis==3.2.1",
        "requests==2.22.0",
        "statsd==3.3.0",
        "tox==3.11.1",
        "mysqlclient==1.4.4",
        "pymysql==0.9.3",
    ],
    # extras_require={
    #     "bigquery": ["pybigquery>=0.4.10", "pandas_gbq>=0.10.0"],
    #     "cors": ["flask-cors>=2.0.0"],
    #     "gsheets": ["gsheetsdb>=0.1.9"],
    #     "hive": ["pyhive[hive]>=0.6.1", "tableschema", "thrift>=0.11.0, <1.0.0"],
    #     "mysql": ["mysqlclient==1.4.2.post1"],
    #     "postgres": ["psycopg2-binary==2.7.5"],
    #     "presto": ["pyhive[presto]>=0.4.0"],
    #     "druid": ["pydruid==0.5.2", "requests==2.22.0"],
    # },
    python_requires="~=3.6",
    author="Apache Software Foundation",
    author_email="dev@superset.incubator.apache.org",
    url="https://superset.apache.org/",
    download_url=(
        "https://dist.apache.org/repos/dist/release/superset/" + version_string
    ),
    classifiers=["Programming Language :: Python :: 3.6"],
)
