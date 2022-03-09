def name_age(name, age):
    print("Hello", name, ".", "Your age is:", age)
    name = input("Enter name:")
    age = input("Enter age:")
    print(name + age)


name_age("Ramona", 21)


def swap_integers(num1, num2):
    a = num1
    b = num2
    temp = a  # num1
    a = b  # num2
    b = temp  # num1
    print(a)
    print(b)


swap_integers(4, 8)


swap_integers(10, 22)


def check_numbers(num1, num2):
    if (num1 % 6 == 0 or num2 % 6 == 0) and num1 % 10 == 0 and num2 % 10 == 0:
        print(True)
    else:
        print(False)


check_numbers(6, 10)


def sum_up(num1, num2):
    num_list = range(num1, num2 + 1)
    if num2 > num1 > 0:
        result = sum(num_list)
        print(result)
    else:
        print(0)


sum_up(3, 9)


def circle_area(r1, r2, r3):
    pi = 3.14
    a1 = pi * r1
    a2 = pi * r2
    a3 = pi * r3
    print("a1:", a1)
    print("a2:", a2)
    print("a3:", a3)
    print(a1 + a2 + a3)  # 'return the area as combined integer'? - das was rauskommt ist kein Integer sondern ein Float


circle_area(1, 2, 3)


def check_string(text):
    text = input("Enter a text: ")
    string = text.lower().endswith("a") or text.lower().startswith("a")
    print(string)


check_string(input)


def triangle(row):
    row = int(input("Number of rows: "))
    for i in range(row + 1):  # i = rows / already printing rows
        for j in range(i):  # j = columns
            print("*", end=" ")
        print()


triangle("row")
