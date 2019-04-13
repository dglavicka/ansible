import requests, json, pprint

apic_ip = '10.0.100.6'
apic_username = 'admin'
apic_password = 'cisco123'
login_creds = {'aaaUser':
                {'attributes':
                      {'name': apic_username, 'pwd': apic_password }
                }
              }

base_url = 'https://%s/api/' % apic_ip
login_url = base_url + 'aaaLogin.json'

json_creds = json.dumps(login_creds)

post_response = requests.post(login_url, data=json_creds, verify=False)

post_response_load = json.loads(post_response.text)
cookie_cutter = post_response_load['imdata'][0]['aaaLogin']['attributes']
cookie = {}
cookie['APIC-Cookie'] = cookie_cutter['token']
print(cookie)

request_url = '/node/class/fabricNode.json'

request_get = requests.get(base_url + request_url, cookies=cookie, verify=False)
jsonToPyload = json.loads(request_get.text)

pprint.pprint(jsonToPyload)
