#dowloading a web page with the requests.get function

import requests
res = requests.get('http://automatetheoringstuff.com/files/rj.txt')
type(res)
res.status_code == requests.codes.ok
len(res.text)
print(res.text[:250]) #print the first 250 letters


