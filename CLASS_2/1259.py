def _check(number):
    reversed_number = number[::-1]
    if number == reversed_number:
        return 'yes'
    else:
        return 'no'

while True:
    x = input()
    if x == '0':
        break
    print(_check(x))