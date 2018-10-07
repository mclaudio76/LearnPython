def generator(str):
    lst = list(str)
    for item in lst:
        yield item

G = generator('Hello')
H = (x for x  in list('World'))

for x in G:
    print (x)

for x in H:
    print (x)

