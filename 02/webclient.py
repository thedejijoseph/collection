# reach to the networks and talk

from urllib import request, parse

url = "http://localhost:8081/login"

params = {
    'username':'deji',
    'password':'joseph'
}

querystring = parse.urlencode(params)

u = request.urlopen(url, querystring.encode("ascii"))
response = u.read()

# print(response)

# using requests for humans

import requests

repsonse = requests.post(url, data=params)

print(response)
