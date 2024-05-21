def calculate_fine(days_late):
    if days_late <= 0:
        return "No fine"
    elif days_late <= 5:
        return "Your fine: Rs. 0.50"
    elif days_late <= 10:
        return "Your fine: Rs. 1.00"
    elif days_late <= 30:
        return "Your fine: Rs. 5.00"
    else:
        return "Your membership has been cancelled"

def main():
    days_late = int(input("Enter how many days late you are: "))
    result = calculate_fine(days_late)
    print(result)

if __name__ == "__main__":
    main()
