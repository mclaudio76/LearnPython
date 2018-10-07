# Numeri
x = 10
y = 11.2
z = 3 ** 2 # Elevamento a potenza
#print(z)


#String
s = 'Hello, cruel world'
targetWord = 'hey'
try:
    idx = s.index(targetWord)    
    print (idx)
    print (s[idx+len(targetWord):])
except:
    pass

lista = list(s)
print(lista)

if s.find(targetWord) >= 0 :
    print ("Trovato.")
else:
    print ("Non trovato.")

l = list(('a', 'b', 'c'))
l *= 2
l += 'd'

print (l)
print(l.pop())

matrix  = [ [1,2,3], [4,5,6], [7,8,9]]

print(matrix)

#estrae una colonna
col2 = [r[1] for r in matrix]



print(col2)