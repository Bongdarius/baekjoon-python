x = input()
y = input()
z = input()

def _case1(x, y, z):
    x = int(x)
    y = int(y)
    z = int(z)

    return x + y - z

def _case2(x, y, z):
    xy = int(x + y)
    z = int(z)

    return xy - z

print(_case1(x, y, z))
print(_case2(x, y, z))