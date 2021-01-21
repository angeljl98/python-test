# Goal
# Print the result of applying the XOR operator to N lines.
# Line 1 is XORed with line 2, the result is XORed with line 3, the result is XORed with line 4...
#
# A represents a 0 and B represents a 1
#
# Truth table for the XOR operator:
# 0^0 -> 0
# 0^1 -> 1
# 1^0 -> 1
# 1^1 -> 0
# Input
# Line 1: Two characters A and B.
# Line 2: Number of lines N.
# Next N lines: A string made up of A and B
# Output
# Line 1 : The result as a string made up of A and B
# Constraints
# A != B
# 2 ≤ N ≤ 50
# All N lines have the same length and are made up of only A and B
# Example
# Input
# QB
# 2
# QBBQQ
# BBQBQ
# Output
# BQBBQ

# s = input()
s="QB"
a=s[0]
b=s[1]
c=[]
# n = int(input())
n=2
for i in range(n):
    # c.append(input())
    emp=0
c.append("QBBQQ")
c.append("BQBBQ")
print(c)
for i in range(len(c)):
    z=''
    if i==0:
        m=c[i]
        continue
    for j in range(len(c[i])):
        if c[i][j]==m[j]:
            z+=a
        else:
            z+=b
    m=z
print(z)
