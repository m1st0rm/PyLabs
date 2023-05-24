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
