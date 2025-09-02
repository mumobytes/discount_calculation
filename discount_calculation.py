def discount(price, discount_percent):
    if discount_percent >= 5:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt the user for inputs
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = discount(price, discount_percent)

# Print the result
if discount_percent >= 5:
    print(f"Discount applied! The final price is: {final_price:.2f}")
else:
    print(f"No discount applied. The price remains: {final_price:.2f}")
