num1 = float(input("Enter number 1:  "))
num2 = float(input("Enter number 2:  "))
num3 = float(input("Enter number 3:  "))
num4 = float(input("Enter number 4:  "))
num5 = float(input("Enter number 5:  "))
numbers = [num1, num2, num3, num4, num5]
total_sum = 0
for i in range(len(numbers)):
    total_sum += numbers[i]
print(f"RESULT: {total_sum/len(numbers)}")