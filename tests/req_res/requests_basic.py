import requests
import pprint
response=requests.get('https://reqres.in/api/users/2', verify=False)
pprint.pprint(response.json()['data']['last_name'])
print(response.status_code)