unit = int(input("enter electrcity units used: "))

if unit<=250:
    print("your electrcity bill is free")

elif unit<=500:
    print((unit-250)*7, "rs")

elif unit<=1000:
    print((unit-250)*15, "rs")

else:
    print((unit-250)*20, "rs")