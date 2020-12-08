import random
import json
import requests
import pprint

url = "https://slack.com/api/users.list"
auth_token=''
headers = {'Authorization': 'Bearer ' + auth_token}

# sending get request and saving the response as response object
req_get = requests.get(url=url, headers=headers)

data = req_get.json()
# pprint.pprint(data)
# print(type(data))

exclude_list = ('USLACKBOT', 'U01EU5ESD7V',
                'U01EXA4224W', 'U01F89XMWPP',
                'U01GZ001TNC')

i = 0
my_dict = {}
while i < len(data['members']):
    if data['members'][i]['id'] in exclude_list:
        i += 1
        continue
    my_dict.update({data['members'][i]['id']: data['members'][i]['profile']['real_name']})
    i += 1
# print(my_dict, type(my_dict))

victim_name = random.choice(list(my_dict.values()))
print(victim_name)

victim_id = list(my_dict.keys())[list(my_dict.values()).index(victim_name)]
print(victim_id)

url = "https://slack.com/api/chat.postMessage"
message = {"channel": {victim_id}, "text": f"It's a test! Don't be scared. {victim_name} is a homework check victim!"}
ver_message = {"channel": 'C01GN5HDFPT', "text": f"It's a test! Don't be scared. {victim_name} is a homework check victim!"}

req_post = requests.post(url=url, headers=headers, data = message)
req_post = requests.post(url=url, headers=headers, data = ver_message)