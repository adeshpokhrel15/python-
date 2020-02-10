#home task
x=2
print(type(x))
print(x)
print("Hello this is ,my home task")
y="let and \t live  \t  home"
print(y.split())
print(y.replace("let and \t live", "enjoy life"))
import re
regexpr=re.compile(y"[\t]+")
regexpr.sub(" ",y)
print(regexpr)




