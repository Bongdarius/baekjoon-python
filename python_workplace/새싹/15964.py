def auto(x, y):
    result = (x+y)*(x-y);
    return result;

mystr = [int(x) for x in input().split()];

a = auto(mystr[0], mystr[1]);
print(a);
