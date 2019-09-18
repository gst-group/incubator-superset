import requests
import json
import logging
import base64

logger = logging.getLogger(__name__)

def authenticate(username, password):

	server_url = "http://cemtest.insight365.ai:5001"
	auth_url = '%s/session/appuser/login' % server_url
	encodedPassword = str(base64.b64encode(password.encode("utf-8")), "utf-8")


	param_dict = dict(telephone=username, userTelephone=username, password=encodedPassword)
	headers = {'content-type': 'application/json'}
	logger.warn(encodedPassword)
	#requests.post(url, params=params, data=json.dumps(data), headers=headers)
	auth_result = requests.post(
	    auth_url, json=param_dict, headers=headers, verify=False)
	response_data = json.loads(auth_result.text)
	logger.info(json.dumps(response_data))
	if auth_result.status_code != 200:
	    logger.warn("failed to auth user: %s, status: %s, response: %s " %
	                (username, auth_result.status_code, auth_result.text))
	    return None
	if "errCode" in response_data and response_data["errCode"] == 999:
	    logger.warn("failed to auth user: %s, message: %s, response: %s " %
	                (username, response_data["errMessage"], auth_result.text))
	    return None
	result_dict = auth_result.json()
	userinfo = dict(
	    username=username,  
		first_name=response_data["data"]["nickName"],
        last_name='',
        email=response_data["data"]["email"])
	return userinfo

"""
  username=username,
                first_name=username.split('@')[0],
                last_name='-',
                email=username,
                role=self.find_role(self.auth_user_registration_role))

"""
