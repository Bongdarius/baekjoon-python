#대문자에서 +32 하면 소문자 됨.
# 65 ~ 92 / 97 ~ 122

inputStr = input();
outputStr = "";
for c in inputStr:
    eachCode = ord(c);
    if(eachCode >= 65 and eachCode <= 92):
        outputStr += chr(eachCode + 32);
    else:
        outputStr += chr(eachCode - 32);
print(outputStr);