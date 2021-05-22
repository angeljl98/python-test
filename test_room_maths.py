import random
print(chr(70)) #convierte numero ascii a letra
print(int("15",16)) #convierte hexadecimal a decimal
print(random.randint(10,20))


numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
#map genera un resultado de una operación matemática
print(list(result))
# uso de fracciones
from fractions import Fraction
n=Fraction('8') // Fraction('0.4') #expresar fracciones
print(n)
# factorial
import sys
def factorial(num):
  '''Return large factorial by Jimmy Olano Sayago
         (GNU General Public License v3.0)       '''
  if num<=1:
    return 1
  else:
    sys.setrecursionlimit(sys.getrecursionlimit()+1)
    return num * factorial(num - 1)
print(factorial(400))
print(ord("a")) #convierte a ascii
print(str(bin(8))) #convierte a binario
