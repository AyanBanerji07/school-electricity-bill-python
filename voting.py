origin = input("Enter your country of origin: ")

if origin=="India" or origin=="INDIA" or origin=="india":
    pass
else:
    print("you are not eligible to vote")

age = int(input("Enter your age: "))

if age>=18:
        print("you are eligible to vote")
else:
    print("you are not eligible to vote")
