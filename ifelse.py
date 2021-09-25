age = input()


if int(age) > 100:
    print('you can not ride this car')
elif int(age) >= 18:
   print('you can ride this car')
elif int(age) > 0:
    print('you are underage')
    
else:
 print('invalid age')