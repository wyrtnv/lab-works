f = open('try.txt', 'r') # cursor on zero
print(f.read(4)) # 0, 1, 2, 3, 4, 5 and 4 symbols away from 0
print(f.read(5)) # 4 + 5
print(f.read()) # 9 + 0
f.close()