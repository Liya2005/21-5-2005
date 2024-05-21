def can_form_rectangle(sides):

    side_count = {}
    
    for side in sides:
        if side in side_count:
            side_count[side] += 1
        else:
            side_count[side] = 1
    
  
    if len(side_count) == 2 and all(count == 2 for count in side_count.values()):
        return True
    else:
        return False

def main():
    
    sides = list(map(int, input("Enter rectangle four sides of length: ").split()))
    
    
    if len(sides) != 4:
        print("Please enter exactly four side lengths.")
        return
    
    if can_form_rectangle(sides):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
