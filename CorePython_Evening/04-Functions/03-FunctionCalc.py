def add():
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))
    print(x+y)

def sub():
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))
    print(x-y)

def div():
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))
    print(x/y)

def mul():
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))
    print(x*y)


print("""
1. Add
2. Sub
3. Div
4. Mul
""")

user_choice = input("Enter your choice : ")

# num_1 = int(input("Enter first number : "))
# num_2 = int(input("Enter second number : "))

result = 0

if user_choice == "1":
    add()
elif user_choice == "2":
    sub()
elif user_choice == "3":
    div()
elif user_choice == "4":
    mul()
