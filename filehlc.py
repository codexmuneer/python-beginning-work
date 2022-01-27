'''2. Write a python program that display the menu of restaurant. Ask
the user to choose the item from the menu list i-e Espresso, over
Ice , fusion etc. let’s assume user have selected over ice option
show the menu along with the prices for regular as well as small.
Ask for the item name, size, and quantity. After that your program
should ask again choose the item from the menu list 1-e Espresso,
over Ice, fusion etc. and keep choosing until user press N or enter
no. Once user done with the menu display the total bill that
includes the total price and tax along with service charge. Also
write the final bill in bill.txt.
Menu is given below.'''

print("#####################################")
print("***********GLORIA JEANS************")
print("#####################################")
print("***********MENU************")
# creating MENU using lists
list = [["Please select any option below"],["PRESS 1 FOR ESPRESSO & MOCHA CHILLERS"], ["PRESS 2 FOR OVER ICE"], ["PRESS 3 FOR CHOCOLATE CHILLERS"], ["PRESS 4 FOR FUSION"]]

list1 = [["VERY VANILLA CHILLER Small: 361, Regular: 409"],["COCOA LOCO Small: 361, Regular: 409 "], ["COOKIES N CREAM Small: 361, Regular: 409"],
         ["HAZELNUT MOCHA CHILLER Small: 396, Regular: 461"], ["CHOCOLATE MACADAMA CHILLER Small: 396, Regular: 461"], ["ITALIAN DOLICE CHILLER Small: 396, Regular: 461"],
         ["CARAMEL NUT CHILLER Small: 396, Regular: 461"],["TIRAMISU CHILLER Small: 399, Regular: 509"], ["TOFFEE NUT CHILLER Small: 399, Regular: 509"]]

list2 = [["SIGNATURE ICED COFFEE:- Small: 300 , Regular: 374"],["ICED MOCHA:- Small: 300 , Regular: 361"],["ICED CARAMEL LATTE:- SmalL: 378 , Regular: 430 "],
        ["ICED AMERICANO:- Small: 252 , Regular: 274"],["BLUEBERRY LEMONADE:- Small: 250 , Regular: 291 "],["LYCHEE LEMONADE:- Small: 250 , Regular: 291  "], 
        ["GREEN APPLE LEMONADE:- Small: 250 , Regular: 291   "],["PEACH LEMONADE:- Small: 250 , Regular: 291  "],["APPLE SODA:- Small: 335 , Regular: 348"], 
        ["LIME SODA:- Small: 335 , Regular: 361"],["ICED TEAS(Peach / Lemon Lychee) :- Small: 239 , Regular: 291"]]

list3 = [["ORIGINAL ICED CHOCOLATE:- Small: 348, Regular: 365"],["WHITE ICED CHOCOLATE:- Small: 348, Regular: 365"],["CHOCOLATE DELIGHT:- Small: 348, Regular: 400"]]

list4 = [["ICED LIME:- Small: 335, Regular: 365"],["APPLE CHILLER:- Small: 335, Regular: 365"],["CHAI CHILLER:- Small: 348, Regular: 400"],
         ["GREEN TEA CHILLER:- Small: 348, Regular: 400"]]

n = ''
press = 0
total = 0
service_charges = 10

while n != 'n': # loop will run until n is pressed
    for i in list: # it will show all list items
        print(i)
        
    press = int(input("PRESS : "))  
 # creating 4 elif conditions according to menu   
    if press == 1: 
        for i in list1: # if user decision is 1 it will show list1 all items 
            print(i)
        #from here user now will choose it's order name, size and quantity
        name = str(input("Tell your item name: ")).lower()
        size = str(input("Small/Regular : ")).lower()
        quantity = int(input("How many you want : "))
        # nested elif ladder according to user decision of item
        if name in ('very vanilla chiller,cocoa loco,cookies n cream'):
            if size == 'small':
                total += quantity*361 + service_charges
            elif size == 'regular':
                total += quantity*409 + service_charges
        elif name in ('hazelnut mocha chiller,chocolate macadama chiller,italian dolice chiller,caramel nut chiller'):
            if size == 'small':
                total += quantity*396 + service_charges
            elif size == 'regular':
                total += quantity*461 + service_charges
        elif name == ('tiramisu chiller,toffee nut chiller'):
            if size == 'small':
                total += quantity*399 + service_charges
            elif size == 'regular':
                total += quantity*509 + service_charges
# same process as above   
    elif press == 2:
        for i in list2:
            print(i)
            
        name = str(input("Tell your item name: ")).lower()
        size = str(input("Small/Regular : ")).lower()
        quantity = int(input("How many you want : "))
        
        if name in 'signature iced':
            if size == 'small':
                total += quantity*300 + service_charges
            elif size == 'regular':
                total += quantity*374 + service_charges
        elif name in 'iced mocha':
            if size == 'small':
                total += quantity*300 + service_charges
            elif size == 'regular':
                total += quantity*361 + service_charges
        elif name in 'iced caramel latte':
            if size == 'small':
                total += quantity*378 + service_charges
            elif size == 'regular':
                total += quantity*430 + service_charges
        elif name in 'iced americano':
            if size == 'small':
                total += quantity*252 + service_charges
            elif size == 'regular':
                total += quantity*274 + service_charges                
        elif name in ('blueberry lemonade,lychee lemonade,green apple lemonade,peach lemonade,'):
            if size == 'small':
                total += quantity*250 + service_charges
            elif size == 'regular':
                total += quantity*291 + service_charges                
        elif name in 'apple soda':
            if size == 'small':
                total += quantity*335 + service_charges
            elif size == 'regular':
                total += quantity*348 + service_charges                
        elif name in 'lime soda':
            if size == 'small':
                total += quantity*335 + service_charges
            elif size == 'regular':
                total += quantity*361 + service_charges
        elif name in 'iced teas':
            if size == 'small':
                total += quantity*239 + service_charges
            elif size == 'regular':
                total += quantity*291 + service_charges   
                
    elif press == 3:
        for i in list3:
            print(i)
        name = str(input("Tell your item name: ")).lower()
        size = str(input("Small/Regular : ")).lower()
        quantity = int(input("How many you want : "))
        
        if name in ('original iced chocolate,white iced chocolate'):
            if size == 'small':
                total += quantity*348 + service_charges
            elif size == 'regular':
                total += quantity*365 + service_charges
        elif name in ('chocolate delight'):
            if size == 'small':
                total += quantity*348 + service_charges
            elif size == 'regular':
                total += quantity*400 + service_charges           
                
    elif press == 4:
        for i in list4:
            print(i)        
                
        name = str(input("Tell your item name: ")).lower()
        size = str(input("Small/Regular : ")).lower()
        quantity = int(input("How many you want : "))
        
        if name in ('iced lime,apple chiller'):
            if size == 'small':
                total += quantity*348 + service_charges
            elif size == 'regular':
                total += quantity*365 + service_charges
        elif name in ('chai chiller,green tea chiller'):
            if size == 'small':
                total += quantity*348 + service_charges
            elif size == 'regular':
                total += quantity*400 + service_charges  
                             
    n = input("press N to exit: ").lower() # if press n while loop will terminate
    
tax = total*0.05        
final_bill = total + tax
bill = open("bill.txt", "w")
print(f"Your Bill including all taxes and service charges: {final_bill}Rs/-")
bill.write(f"Your Bill including all taxes and service charges: {final_bill}Rs/-")
bill.close()