import requests
r = requests.get('https://api.github.com/')
response = r.json()
print("JSON value of the said response:")
print(r.json())
print("\nEach key of the response:")
print("Current user url:",response['current_user_url'])
print("Current user authorizations html url:",response['current_user_authorizations_html_url'])
print("Authorizations url:",response['authorizations_url'])
print("code_search_url:",response['code_search_url'])
print("commit_search_url:",response['commit_search_url'])
# Importing Request module, which was installed prior to
import requests
# Http Methods:
response = requests.get('https://httpbin.org/get')
print (response.status_code)
response = requests.post('https://httpbin.org/post', json={'python': {'library': 'requests'}})
print (response.request.body)
response = requests.put('https://httpbin.org/put', json={'python': {'version': '2x', 'library': 'requests'}})
print (response.request.body)
response = requests.patch('https://httpbin.org/patch', json={'python': {'version': '3x', 'library': 'requests'}})
print (response.request.body)
response = requests.delete('https://httpbin.org/delete')
print (response.status_code)
# Status Codes:
for url in ['https://httpbin.org/status/200', 'https://httpbin.org/status/400', 'https://httpbin.org/status/500']:
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception, if applicable
    except:
        print ('Error with status code: ' + response.status_code)
    else:
        print ('Request completed successfully')