print(7==9)
print(7!=9)
print(7>=9)
print(7<=9)
def funcion(x,y,z): #definir funcion
    r=x+y+z
    return r
print(funcion(1,2,3))
c=0
if 5>4:
    print("5>4")
elif 5>3:
    print("5>3")
else:
    pass

sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass #aqui agregas el código luego

while (c<5): #rutina del while condition:
    pass #no hace nada, usalo en los else, cuando no termines de escribir los else
    print(str(c))
    c+=1 #incremento

i=0
while True:
    i+=1
    if i==3:
        print("aqui salto")
        continue #saltará a iteración en i=2
    elif i==4:
        print ("aqui me salgo") #se sale del while
        break
    else:
        print("imprime i:"+str(i)) #imprimira todo los i

class punto: #definir una clase
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
pto_1=punto(3.0,3.0,3.0) #crear variable a partir de una clase
print("dist")
print(funcion(pto_1.x,pto_1.y,pto_1.z))

def espar(x): #función par
    z = {
         0: True,
         1: False,
    }
    return z.get((x%2),"Empty")
# uso de
print(espar(2))

for i in [1,5,9]:
    print(str(i))
for i in (1,5,9):
    print(str(i))

s1="A B C"
s2="B C A"
a=[]

def word2number(x): #convierte la palabra a ascii
    r=[]
    for i in x:
        v=r.append(int(ord(i))) #convierte a binario
    return r
v=word2number(s1)
print(v)
u=v.copy()
w=v.sort()
print(v)

print(list(range(5,8))) #imprime una lista, hasta el 7, no el 8
print(list(range(5,16,2))) #imprime los impares del 5 al 16, incluyendo el 5
