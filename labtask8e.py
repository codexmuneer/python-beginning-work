'''5. Write a program that performs a survey tally on beverages. The
program should prompt for the next person until a sentinel value of –1 is entered to
terminate the program. Each person participating in the survey should choose
their favorite beverage from the following list:'''

coffee = 0
tea = 0
coke = 0
orange_juice = 0
ask = 0
i = 0
print("choose your favourite beverages from the following list: ")
print("1.Coffee 2.Tea 3.Coke 4.Orange juice")


while ask != -1:
    i += 1
    ask = int(input(f"Please input the favourite beverage of person #{i} choose 1,2,3 or 4 fom the above menu or -1 to exit the program \n"))
    if ask == 1:
        coffee += 1
    
    elif ask == 2:
        tea += 1
        
    elif ask == 3:
        coke += 1
    
    elif ask == 4:
        orange_juice += 1
               
print("Beverage             Number of votes")
print("#######################################")
print("Coffee                   ", coffee)
print("Tea                      ",  tea)
print("Coke                     ", coke)
print("Orange juice             ", orange_juice)