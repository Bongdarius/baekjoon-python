inputStr = input()
inputStr = inputStr.upper()
my_dic = {}

for s in inputStr:
    try:
        my_dic[s] += 1
    except:
        my_dic[s] = 1

max_value = max(my_dic.values())
max_keys = [key for key, value in my_dic.items() if value == max_value];

if(len(max_keys) >= 2):
    print("?")
else:
    print("".join(max_keys))