for i in range(10):
    print(i)  # 0 1 2 3 4 5 6 7 8 9
print("-----")

for i in range(5, 10):
    print(i)  # 5 6 7 8 9

print("-----")
for i in range(0, 10, 2):
    print(i)  # 0 2 4 6 8

# 逆順にアクセスする
for i in range(10, 0, -1):
    print(i)

for x in reversed(range(1, 11)):
    print(x)
