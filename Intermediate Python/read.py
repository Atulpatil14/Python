#only read() function:-
#f=open("file.txt","r")
#a=f.read()
#print(a)
#f.close()

#readlines() Function:-
f=open("code.txt","r")
a=f.readlines()
for i in a:
    print(i)
f.close()
