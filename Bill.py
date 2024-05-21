def calculate_bill(units):
    if units <= 199:
        charge_per_unit = 1.20
    elif units < 400:
        charge_per_unit = 1.50
    elif units < 600:
        charge_per_unit = 1.80
    else:
        charge_per_unit = 2.00

    bill_amount = units * charge_per_unit

    if bill_amount > 400:
        surcharge = bill_amount * 0.15
        bill_amount += surchar
    bill_amount = max(bill_amount, 100)
    return bill_amount

def main():
    units = int(input("Enter the number of units: "))
    bill_amount = calculate_bill(units)
    print(f"Total Bill Amount: Rs. {bill_amount:.2f}")

if __name__ == "__main__":
    main()
