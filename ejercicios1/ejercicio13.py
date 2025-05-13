
prices = [100, 450, 27]

def apply_taxes(price):
    vat = 0.15 * price
    duties = 0.20 * price
    return price + vat + duties

tax_inclusive = [apply_taxes(price) for price in prices]

for base_price, total_price in zip(prices, tax_inclusive):
    print(f"Para el precio base {base_price}, el total con impuestos es {total_price}.")

"""
Para el precio base 100, el total con impuestos es 135.0.
Para el precio base 450, el total con impuestos es 607.5.
Para el precio base 27, el total con impuestos es 36.45. 
"""