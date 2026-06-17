#first exercise
username = input()
print(f"Username: {username}")
age = int(input())
print(f"Age: {age}")
print(str(100 - age), "years it takes to reach your 100th birthday.")

#second exercise
width = int(input())
length = int(input())
height = int(input())
print(f"The width of the room: {str(width)} meters.\n")
print(f"The length of the room: {str(length)} meters.\n")
print(f"The height of the room: {str(height)} meters.\n")
print(f"The volume of the room: {str(width)} * {str(length)} * {str(height)} = {str(width * length * height)} meters cube.")

#third exercise
degree_in_Celsius = float(input())
print(f"Temperature in degree Celsius: {str(degree_in_Celsius)}.\n")
print(f"Temperature in degree Fahrenheit: {str(degree_in_Celsius * 9/5 + 32)}.")

#fourth exercise
body_temperature = float(input())
print(f"The user's temperature: {body_temperature}.")
if body_temperature < 35.0:
    print("Too cold.")
elif body_temperature > 37.0:
    print("Too hot.")
else:
    print("Everything looks good.")
    
#fifth exercise
n = int(input("How many numbers you want to sort: "))
lst = []

for i in range(n):
    lst.append(float(input()))

print("Your numbers before sorting: ")
for i in lst:
    print(i)

#Sort with for
for i in range(n):
    for j in range(n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("Your numbers after sorting in ascending order: ")
for i in lst:
    print(i)
    
#fifth exercise another way to solve: sort
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Sorting logic using if..elif..else
if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        print(f"Ascending order: {num1}, {num2}, {num3}")
    else:
        print(f"Ascending order: {num1}, {num3}, {num2}")
elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        print(f"Ascending order: {num2}, {num1}, {num3}")
    else:
        print(f"Ascending order: {num2}, {num3}, {num1}")
else:
    if num1 <= num2:
        print(f"Ascending order: {num3}, {num1}, {num2}")
    else:
        print(f"Ascending order: {num3}, {num2}, {num1}")

##fifth exercise another way to solve: sort