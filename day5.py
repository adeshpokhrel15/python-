d={}
alpha=[]
x="c1b2a3"
for i in range(len(x)):
    char=x[i]
    d[char]=i
l=[0,2,4]
y=print(l[::-1])
print(d)
for key,value in d.items():
    if key.isalpha():
        alpha.append(value)
z=alpha[::-1]
print(z)


for key,value in d.items():
    if key.isalpha():
        d[key] = alpha.pop()

#list
l=['za','sayam','Adesh','adesh','ram']
l=list(sorted(l,key = lambda a:a[-1]))
print(l)
print(ord("A"))
print(ord('a'))

#dictionary
d={'a': "adesh",
'b':"Rambahadur",
'z':"Tiger",
'u':"Ronaldo"}
print(sorted(d,key=lambda k: d[k]))
items=d.items()
print(items)
for key,value in items:
    print(key,value)
for key,value in items:
    print(key,value)

