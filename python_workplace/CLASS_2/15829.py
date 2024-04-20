#Hashing
#abcde의 해시 값은 1 × 310 + 2 × 311 + 3 × 312 + 4 × 313 + 5 × 314
#               = 1 + 62 + 2883 + 119164 + 4617605 = 4739715이다.

firstInput = int(input())

asciiStart = 97
alDic = {}
for i in range(asciiStart, asciiStart + 26, 1):
    alDic[chr(i)] = (i - asciiStart + 1)

# print(alDic)

secInput = input()
# secInput = "hello"
strIntoInt = [alDic.get(x) for x in secInput]

# print(strIntoInt) #[8, 5, 12, 12, 15]

firstList = []
sum = 0
for i in range(0, len(secInput), 1):
    sum += strIntoInt[i] * (31 ** i)

print(sum % 1234567891)