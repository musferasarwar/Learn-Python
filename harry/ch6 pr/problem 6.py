marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    grade = "EX"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Your grade is:" ,grade)

"my grade out of 800"