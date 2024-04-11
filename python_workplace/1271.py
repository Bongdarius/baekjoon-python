inputString = input();
splitArray = inputString.split(" ");

totalMoney = int(splitArray[0]);
totalLife = int(splitArray[1]);

print(totalMoney//totalLife);
print(totalMoney%totalLife);
