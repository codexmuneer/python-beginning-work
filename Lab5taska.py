# write a program that takes quantity in pounds and convert it into kilogram and gram
#"reflect the concept of required arguments"
# 1 pound = 453.59237 gram
# 1 pound = 0.454 kg


def weight_con(pounds):

 gram = pounds * 453.59237
 kilogram = pounds * 0.454
 print("The amount of pound you entered is: ", pounds)
 print("Given quantity in gram is", gram)
 print("Given quantity in Kilogram is", kilogram)

 return gram,kilogram

pounds = float(input("Enter your quantity you want to convert: "))
weight_con(pounds)
