#Create one empty list add prime numbers..........

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = []
for num in range(2, 51):
    if is_prime(num):
        prime_numbers.append(num)

print(prime_numbers)

# Print user input table

num_rows = int(input("Enter the number of rows: "))
num_cols = int(input("Enter the number of columns: "))
table = []
for i in range(num_rows):
    row = []
    for j in range(num_cols):
        data = input(f"Enter data for row {i+1}, column {j+1}: ")
        row.append(data)
    table.append(row)
for row in table:
    for data in row:
        print(data, end="\t")
    print()
   
 #  Print palindrome string taking input as string

def is_palindrome(string):
    return string == string[::-1]

def print_palindrome(string):
    if is_palindrome(string):
        print(f"The string '{string}' is a palindrome.")
    else:
        print(f"The string '{string}' is not a palindrome.")
string = input("Enter a string: ")
print_palindrome(string)

# Take input as string and reverse it

def reverse_string(input_string):
    return input_string[::-1]
input_str = input("Enter a string: ")
reversed_str = reverse_string(input_str)
print("Reversed string:", reversed_str)
