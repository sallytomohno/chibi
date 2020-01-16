import random
s=[1,2,3,4,5]
z=[1,2,3,4,5,6,7,8,9,10]
n=[1,2,3,4,5]
p=[1,2,3,4,5]
t=[1,2,3,4,5,6,7,8,9,10,11]
d=[1,2,3,4,5,6,7,8,9,10]
print('sarada=',random.choice(s),'zensai=',random.sample(z,2),'niku=',random.choice(n),'pizza=',random.choice(p),'tansuikabutu=',random.choice(t),'dezart=',random.choice(d))

import requests
 
query = "カレー"
url = "https://cookpad.com/" #クックパッド
res = requests.get(url)

soup = BeautifulSoup(res.text,"html.parser")
p = soup.find("p",class_="floatl pt5p")
 