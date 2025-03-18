def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        new_price = price- (price*discount_percent/100)
        return new_price
    else:
        new_price = price
        return new_price
    
price= int(input("Please enter item price: "))
discount_percent = int(input("Please enter the discount percentage in numbers only: "))

print(f"The price is {calculate_discount(price, discount_percent)}. Thank you for shopping with us")
    
    