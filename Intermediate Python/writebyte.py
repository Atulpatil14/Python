import requests

url = "https://lhwmis.sindhealth.pk/img/lhwimg2.jpg"

h={'User-Agent':'Mysterice'}

data=requests.get(url, headers=h, timeout=10)

print(type(data.text))
print(type(data.content))

f=open("image.jpg","wb")
f.write(data.content)
f.close()
