score = int(input("Enter your score: "))

if score >= 80:
    print("Distinction")
elif 60 <= score <= 70:
    print("Credit")
elif 40 <= score <= 50:
    print("Fair")
elif score < 40:
    print("Failed")
