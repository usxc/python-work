x = 10
y = 3
z = 0

# yを一ずつ減算してFor文を回す
for i in range(3):
    y -= 1
    print("x =", x)
    print("y =", y)
    print("z =", z)    
    
    z = x / y
    print("z =", z)    
    print("---")    # この１行があるとループ回数がわかりやすい

print("x =", x)