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


if __name__ == '__main__':
    print('Hello World!')
