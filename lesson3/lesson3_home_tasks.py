# task_1
number1 = float(input("number 1: "))
number2 = float(input("number 2: "))
print (f"res: {abs(number1*-1+number2)}")

# task_2
grams=int(input("enter grams: "))
print(f"kilograms: {round(grams/1000)}")

# task_3
num_1, num_2 = input("Enter numbers: ").split(",")
print(int(num_1)%7==0 and int(num_2)%7==0)

# task_4
number=int(input("enter num: "))
print(f"last digit: {number%10}")