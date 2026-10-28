price= int(input("Enter the price you want"))
quality = int(input("Enter the Quality Of the product in digit"))
if price < 0 or quality < 0:
    print("Price should be positive not negative")
if price >= 10000:
    discount = price - (price * 10 / 100)
    print("The Price of the product After discount is" , discount)
else:
    print("price is")