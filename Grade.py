def calculate_grade():

    subject1 = float(input("Enter the marks for subject 1: "))
    subject2 = float(input("Enter the marks for subject 2: "))
    subject3 = float(input("Enter the marks for subject 3: "))
    
    
    average_marks = (subject1 + subject2 + subject3) / 3
    
    
    if average_marks >= 90:
        grade = 'A'
    elif 80 <= average_marks < 90:
        grade = 'B'
    elif 70 <= average_marks < 80:
        grade = 'C'
    elif 60 <= average_marks < 70:
        grade = 'D'
    elif 50 <= average_marks < 60:
        grade = 'E'
    else:
        grade = 'F'
    
  
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Grade: {grade}")


calculate_grade()
