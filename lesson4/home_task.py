# task_1
#my_string = input("Your string: ")
#print(f"First caracter: {my_string[0]}")
#print(f"Last caracter: {my_string[-1]}")
#print(f"Middle caracter: {my_string[int(len(my_string)/2)]}")
#print(f"Even index caracters: {my_string[::2]}")
#print(f"Odd index caracters: {my_string[1::2]}")
#print(f"Reversed string: {my_string[::-1]}")
# task_2
#my_message = input("Your message: ")
#print(f"Lowercase: {my_message.lower()}")
#print(f"Uppercase: {my_message.upper()}")
#print(f"Capitalized: {my_message.capitalize()}")
#print(f"Title case: {my_message.title()}")
#words=my_message.split()
#print(f"{words=}")
# task_3
#width = int(input("Enter Screen width in pixels:  "))
#height = int(input("Enter Screen height in pixels:  "))
#print(f"Resolution: {width} X {height}")
#print(f"total pixels: {width*height}")
# task_4
numbers=list(range(1,17))
total_sum=0
total_sum+=numbers[15]
numbers.pop(15)
total_sum+=numbers[0]
numbers.pop(0)
total_sum+=numbers[12]
numbers.pop(12)
total_sum+=numbers[7]
numbers.pop(7)
print(numbers)
print(total_sum)