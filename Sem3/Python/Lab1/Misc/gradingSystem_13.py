total_marks = int(input("Enter the total marks : "))

achieved_marks = float(input("Enter the achieved marks : "))

percentage = (achieved_marks/total_marks)*100

if percentage >= 90:
    print(f"Percentage : {percentage}%, GRADE A")
elif percentage >= 80:
    print(f"Percentage : {percentage}%, GRADE B")
elif percentage >= 70:
    print(f"Percentage : {percentage}%, GRADE C")
elif percentage >= 60:
    print(f"Percentage : {percentage}%, GRADE D")
elif percentage >= 40:
    print(f"Percentage : {percentage}%, GRADE E")
elif percentage < 40:
    print(f"Percentage : {percentage}%, GRADE F")