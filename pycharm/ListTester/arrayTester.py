import array

ary = array.array('i', [1, 2, 3, 4])  #※ 'i' は整数型を示す型コード。
print(ary)
print(ary[0])
# ここまで入力する。

# まずはココまで追加しましょう
ary[0] = 11
print(ary[0])

ary[0] = 'a'  # これはエラー
print(ary[0])
