
input_count = input("Mau berapa apel ?")

count = int(input_count)
price = 2
money = 10
total_price = price * count

if money > total_price:
    print("Anda membeli " + str(count) +
          " apel dengan harga " + str(total_price) + " Dollar")
    print("Sisa uang anda " + str(money - total_price) + " Dollar")
elif money == total_price:
    print("Anda membeli " + str(count) +
          " apel dengan harga " + str(total_price) + " Dollar")
    print("Uang anda habis")
else:
    print("Uang anda kurang")
    print("Anda tidak dapat membeli " + str(count) + " apel")
