# コレクション型...データの集まり
# シーケンス型...順序を持っているコレクション型

print("リスト型---")
a = [10, 20, 30, 40]
for num in a:
    print(num)
print(f"a is {type(a)}")  # <class 'list'>
print(f"a[0] = {a[0]}")  # 10
print(f"sum(a) = {sum(a)}")  # 100

print("ディクショナリ型---")
# ディクショナリ型はループできるけどシーケンス型じゃない
a = {'tomato': 60, 'apple': 120}
print(type(a))  # <class 'dict'>
for num in a:
    print(num)
# print(f"a[0] = {a[0]}") #KeyError: 0 →Key＝0に対応するValueが登録されていない

print("セット型---")
# セットはシーケンス型ではない
a = {10, 20, 30, 40}
print(type(a))  # <class 'set'>
print(f"sum(a)={sum(a)}")
for num in a:
    print(num)
# print(f"a[0] = {a[0]}") #TypeError: 'set' object is not subscriptable

print("タプル型---")
a = (10, 20, 30, 40)
print(type(a))  # <class 'tuple'>
print(f"sum(a)={sum(a)}")
for num in a:
    print(num)
print(f"a[0] = {a[0]}")

print("文字列型---")
a = "hello"
# a = "12345" 数字にしても無理
print(type(a))  # <class 'str'>
for num in a:
    print(num)
print(f"a[0] = {a[0]}")
print(len(a))

print("レンジ型---")
a = range(10)
print(type(a))
for num in a:
    print(num)
print(f"a[0] = {a[0]}")
