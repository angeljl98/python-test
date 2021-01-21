# A message has been encrypted with Pi cipher encryption.
# You need to print the decrypted message.
#
# In the Pi cipher encryption, each character is shifted by the value of the digit in Pi at the position of the letter in the message skipping non-letter characters (ex: 'T' is the 3rd letter in 'HI THERE', so its position is 3)
#
# Only shift if it is a letter.
# All characters in the input are upper case.
#
# For your information: Pi starts with 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
#
# Example:
# Original message:  HELLO WORLD!
# Pi used as a key:  31415 92653
# Encrypted message: KFPMT FQXQG!
#
#
# Again, you have to decrypt the message, not encrypt it.
# Input
# A string s which you need to decrypt
# Output
# A string which is the decrypted message
# Constraints
# 1 ≤ s length ≤ 100
# Letters in s are capital only.
# Example
# Input
# KFPMT FQXQG!
# Output
# HELLO WORLD!

# s = input()
P = '31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
assert len(P) > 99
s = "KFPMT FQXQG!"
ou=""
i = 0
for c in s:
    if c.isalpha():
        x = (ord(c) - 65 - int(P[i]) + 26000) % 26 + 65
        y=ord(c)
        # print(c," ",x," ",y)
        c = chr(x)
        i += 1
    ou=(ou+c)
    # print(end = c)
# print(ou)

r=''
*pi,=map(int,'31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337')
i=0
for c in s:
    if c.isalpha():
        p = ord(c)-pi[i]
        if p<65:
            p=90-(65-p-1)
        r+=chr(p)
        i+=1
    else:r+=c
print(r)
