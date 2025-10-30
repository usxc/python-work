def clacTaxPriceSimple(price):
    return int(price) * 1.1


x = input("金額を入力してください。")
print(clacTaxPriceSimple(x))