#original_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#def get_even_numbers(numbers):
 #   even_numbers = []
 #   for num in numbers:
  #      if num % 2 == 0:
   #         even_numbers.append(num)
    #return even_numbers
# print(f"Using Regular function: {get_even_numbers(original_numbers)}")

original_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, original_numbers))
print(even_numbers)
