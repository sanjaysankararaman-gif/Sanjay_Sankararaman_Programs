def calculate_subtotal(*prices):
    subtotal = 0
    for i in prices:
        subtotal += i
    return subtotal

def calculate_discount(amount, discount = 5):
    discount_amount = amount * (discount/100)
    return discount_amount

def calculate_tax(amount, tax_rate = 18):
    tax_amount = amount * (tax_rate/100)
    return tax_amount

def generate_bill(*prices, discount, tax_rate):
    subtotal = calculate_subtotal(*prices)
    discount_amount = calculate_discount(subtotal, discount)
    amount_after_discount = subtotal - discount_amount

    tax_amount = calculate_tax(subtotal, tax_rate)
    final_amount = tax_amount + amount_after_discount

    return final_amount, discount_amount, tax_amount



