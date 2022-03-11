def name_age(name, age):
    print("Hello", name, ".", "Your age is:", age)
    name = input("Enter name:")
    age = input("Enter age:")
    return input(name + age)


name_age("Ramona", 21)


def swap_integers(num1, num2):
    a = num1
    b = num2
    print(a)
    print(b)
    temp = a  # num1
    a = b  # num2
    b = temp  # num1
    print(a)
    print(b)
    return str(a) + str(b)


print(swap_integers(10, 22))


def check_numbers(num1, num2):
    if (num1 % 6 == 0 or num2 % 6 == 0) and num1 % 10 == 0 and num2 % 10 == 0:
        return True
    else:
        return False


print(check_numbers(6, 10))  # vorher hatte ich hier kein print, aber hab es nicht geschafft
                            # dass der return value angezeigt wird


def sum_up(num1, num2):
    numbers = range(num1, num2 + 1)
    if num2 > num1 > 0:
        result = sum(numbers)
        return result
    else:
        return 0


print(sum_up(3, 9))


def circle_area(r1, r2, r3):
    pi = 3.14
    a1 = pi * r1
    a2 = pi * r2
    a3 = pi * r3
    print("a1:", a1)
    print("a2:", a2)
    print("a3:", a3)
    return r1 + r2 + r3  # die Summe aller Radii ist nur ein Float, wenn die einzelenen Radii Floats sind


print(circle_area(1, 2, 3))


def check_string(text):
    string = text.lower().endswith("a") or text.lower().startswith("a")
    print(string)


check_string("ahead")


def triangle(row):
    for i in range(row + 1):  # i = rows / already printing rows
        for j in range(i):  # j = columns
            print("*", end=" ")
        print()


triangle(3)
