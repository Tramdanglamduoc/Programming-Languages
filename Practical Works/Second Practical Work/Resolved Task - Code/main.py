#Ngoc Bao Tram Tran 231ADB294

#############
#Exercise 1
output = []

for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        output.append("FizzBuzz")
    elif i % 5 == 0:
        output.append("Fizz")
    elif i % 7 == 0:
        output.append("Buzz")
    else:
        output.append(str(i))

print(', '.join(output))

#############
#Exercise 2
height = int(input("Type the input of the height of the Christmas tree: "))

for i in range(1, height + 1):
    space = ' ' * (height - i)
    star = '*' * (2 * i - 1)
    print(space + star)

#############
#Exercise 3
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

def add_mult(a, b, c):
    values = sorted([a, b, c]) # Sort the values to know the two smallest and the largest
    result = (values[0] + values[1]) * values[2] #(sum of the two smallest) * largest
    return result

print(add_mult(a, b, c))

#############
#Exercise 4
text = input("Enter the text: ")

def is_palindrome(text):
    clean_text = ''.join(text.split()).lower()
    return clean_text == clean_text[::-1]

print(is_palindrome(text)) 
