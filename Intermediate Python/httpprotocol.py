#............Http Protocol...........#

import requests                    #It's Library

url = "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.blackbox.com/en-us&ved=2ahUKEwi8k960x8uGAxUaT2wGHf3VB84QFnoECAgQAQ&usg=AOvVaw0oQ4C-lKBn7wLWFnTfe6kp"                                 #Url give or Give ip

data = requests.get(url, timeout=10)  #Send request to server and we give timeout then it will wait


print(data.status_code)      #It will give status code like 403,404,200,etc


print(data.headers)             #dict. data type


print(data.headers['Date'])   #It will give perticular key:value header


print(data.headers.items())     #It will show us all Key:Value pairs in the form of list


for a,b in data.headers.items():    #It will store key in a and value in b
    print("{}: {}".format(a,b))


print(data.text)  #Print the body in ASCII text
