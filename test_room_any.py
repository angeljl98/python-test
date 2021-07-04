#funciones list, all y any

nums=[55,44,33,22,11]

if all([i>5 for i in nums]):
    print("All larger than 5")

if any([i%2 == 0 for i in nums]):
    print("At least one is even")

for v in enumerate(nums):
    print(v)



#esta es una funcion que cuenta los caracteres
def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))

filename = input("Enter a filename: ")
with open(filename) as f:
    text = f.read()

print(count_char(text, "r"))

#este es un ejemplo de como un programa abre un archivo
filename = input("Enter a filename: ")

with open(filename) as f:
   text = f.read()

print(text)


#imprimir mas grande
txt = input()

sp=txt.split()
r=0
for x in sp:
    if len(x)>r:
        res=x
        r=len(x)
    else:
        pass
print(res)
