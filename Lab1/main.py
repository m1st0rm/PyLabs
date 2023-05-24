def calculate(x, y, operation):
    if operation == 'add':
        return x+y
    elif operation == 'sub':
        return x-y
    elif operation == 'mul':
        return x*y
    elif operation == 'div':
        if y == 0:
            print('Division by zero is impossible')
        else:
            return x/y


def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


if __name__ == '__main__':
    print('Hello World!')
    print(calculate(25, 5, 'add'))
    print(calculate(1, 9, 'sub'))
    print(calculate(6, 3.3, 'mul'))
    print(calculate(15, 3, 'div'))
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(get_even_numbers(numbers))
    