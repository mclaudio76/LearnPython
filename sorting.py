import functools
class Person:
    age  = 0
    name = ""
    def __init__(self, name, age, cmpFun=None):
        self.age = age
        self.name = name
        self.cmpFun = cmpFun

    def __repr__(self):
        return self.name+" "+str(self.age)

def compare(p1, p2, *attributes):
    for attr in attributes:
        val1 = getattr(p1, attr)
        val2 = getattr(p2, attr)
        if val1 != val2:
            return 1 if val1 > val2 else -1
    return 0        
             
def nameSorter(p1, p2):
    return compare(p1,p2, "name")

def ageSorter(p1, p2):
    return compare(p1,p2, "age")

def nameThenAgeCmp(p1, p2):
    res =   compare(p1,p2, "name")
    return res if res != 0 else compare(p1,p2, "age")


ls = [Person("John",42), Person("Mark",15), Person("Jane",47), Person("Mark",14)]


ls = sorted(ls, key=functools.cmp_to_key(nameThenAgeCmp))

print(ls)
