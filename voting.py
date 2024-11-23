def voting(age):
    if age>=18:
        print("Eligible")
    else:
        print("Not eligible")

age=int(input("Enter your age:"))
voting(age)