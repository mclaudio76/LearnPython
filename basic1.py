
def doSomethingWithString(str):
    print(" Input is "+str, end = '\n')
    split = str.split(" ")
    print(split)
    split.pop(2)
    print(split)

def secondFun():
    s = [10,20]
    x = [20,30]
    return s, x

x = 10
y = 11.2
dict = {1:'Alfa', 2:'Beta'}
k = "A sample approach"
doSomethingWithString(k)
x, y  = secondFun()
print(x, end='\n')
print(y)


