def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

price = float(input("Enter your original price: "))
discount_percent = float(input("Enter your the discount percentage: "))
final_price = calculate_discount(price, discount_percent)

print(f"Your Finaly price is: {final_price}")