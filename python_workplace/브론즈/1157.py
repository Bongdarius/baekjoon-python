inputStr = input()
inputStr = inputStr.upper()
dic = {};

for s in inputStr:
    try:
        dic[s] += 1
    except:
        dic[s] = 1

max_value = max(dic.values())
max_keys = [key for key, value in dic.items() if value == max_value]

if len(max_keys) == 1:
    print(''.join(max_keys))
else:
    print('?')