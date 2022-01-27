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


a = 0
b = " "
total = 0
tax = 30
service_charges = 10

while b != "n":
    print("Please select any option below:")
    print("PRESS 1 FOR ESPRESSO & MOCHA CHILLERS")
    print("PRESS 2 FOR OVER ICE")
    print("PRESS 3 FOR CHOCOLATE CHILLERS")
    print("PRESS 4 FOR FUSION")
    choose = int(input("PRESS: "))
    
    if choose == 1:
        print("Press a for VERY VANILLA CHILLER:- Small: 361 , Regular: 409")
        print("Press a for COCOA LOCO:- Small: 361 , Regular: 409")
        print("Press a for COOKIE N'CREAM ")
        print("Press b for HAZELNUT MOCHA CHILLER:- Small: 396 , Regular: 461")
        print("Press b for CHOCOLATE MACADAMIA CHILLER ")        
        print("Press b for CHOCOLATE MACADAMIA CHILLER ") 
        print("Press b for ITALIAN DOLCE CHILLER ") 
        print("Press b for CARAMEL NUT CHILLER ") 
        print("Press c for TIRAMISU CHILLER:- Small: 399 , Regular: 509") 
        print("Press c for TOFFEE NUT CHILLER ")
        
        name = str(input("Tell your item name: ")).lower()
        size = str(input("Small/Regular : ")).lower()
        quantity = int(input("How many you want : "))
        
        if name == 'a':
            if size == 'small':
                total += quantity*361 + service_charges
            elif size == 'regular':
                total += quantity*409 + service_charges
        elif name == 'b':
            if size == 'small':
                total += quantity*396 + service_charges
            elif size == 'regular':
                total += quantity*461 + service_charges
        elif name == 'c':
            if size == 'small':
                total += quantity*399 + service_charges
            elif size == 'regular':
                total += quantity*509 + service_charges

    if choose == 2:
        print("Press a for SIGNATURE ICED COFFEE:- Small: 300 , Regular: 374")
        print("Press b for ICED MOCHA:- Small: 300 , Regular: 361")
        print("Press c for ICED CARAMEL LATTE:- SmalL: 378 , Regular: 430 ")
        print("Press d for ICED AMERICANO:- Small: 252 , Regular: 274")
        print("Press e for BLUEBERRY LEMONADE:- Small: 250 , Regular: 291 ")        
        print("Press e for LYCHEE LEMONADE ") 
        print("Press e for GREEN APPLE LEMONADE  ") 
        print("Press e for PEACH LEMONADE ") 
        print("Press f for APPLE SODA:- Small: 335 , Regular: 348") 
        print("Press g for LIME SODA:- Small: 335 , Regular: 361")
        print("Press h for ICED TEAS(Peach / Lemon Lychee) :- Small: 239 , Regular: 291") 
                
        name = str(input("Tell your item name: ")).lower()
        size = str(input("Small/Regular : ")).lower()
        quantity = int(input("How many you want : "))
        
        if name == 'a':
            if size == 'small':
                total += quantity*300 + service_charges
            elif size == 'regular':
                total += quantity*374 + service_charges
        elif name == 'b':
            if size == 'small':
                total += quantity*300 + service_charges
            elif size == 'regular':
                total += quantity*361 + service_charges
        elif name == 'c':
            if size == 'small':
                total += quantity*378 + service_charges
            elif size == 'regular':
                total += quantity*430 + service_charges
        elif name == 'd':
            if size == 'small':
                total += quantity*252 + service_charges
            elif size == 'regular':
                total += quantity*274 + service_charges                
        elif name == 'e':
            if size == 'small':
                total += quantity*250 + service_charges
            elif size == 'regular':
                total += quantity*291 + service_charges                
        elif name == 'f':
            if size == 'small':
                total += quantity*335 + service_charges
            elif size == 'regular':
                total += quantity*348 + service_charges                
        elif name == 'g':
            if size == 'small':
                total += quantity*335 + service_charges
            elif size == 'regular':
                total += quantity*361 + service_charges
        elif name == 'h':
            if size == 'small':
                total += quantity*239 + service_charges
            elif size == 'regular':
                total += quantity*291 + service_charges                

    if choose == 3:
        print("Press a for ORIGINAL ICED CHOCOLATE:- Small: 348 , Regular: 365")
        print("Press a for WHITE ICED CHOCOLATE  ")        
        print("Press b for CHOCOLATE DELIGHT:- Small: 348 , Regular: 400")

        
        name = str(input("Tell your item name: ")).lower()
        size = str(input("Small/Regular : ")).lower()
        quantity = int(input("How many you want : "))
        
        if name == 'a':
            if size == 'small':
                total += quantity*348 + service_charges
            elif size == 'regular':
                total += quantity*365 + service_charges
        elif name == 'b':
            if size == 'small':
                total += quantity*348 + service_charges
            elif size == 'regular':
                total += quantity*400 + service_charges


    if choose == 4:
        print("Press a for ICED LIMED:- Small: 335 , Regular: 365")
        print("Press a for WHITE ICED CHOCOLATE  ")        
        print("Press b for CHAI CHILLER:- Small: 348 , Regular: 400")
        print("Press b for GREEN TEA CHILLER  ") 
        
        name = str(input("Tell your item name: ")).lower()
        size = str(input("Small/Regular : ")).lower()
        quantity = int(input("How many you want : "))
        
        if name == 'a':
            if size == 'small':
                total += quantity*348 + service_charges
            elif size == 'regular':
                total += quantity*365 + service_charges
        elif name == 'b':
            if size == 'small':
                total += quantity*348 + service_charges
            elif size == 'regular':
                total += quantity*400 + service_charges

                                           
    b = str(input(" Press N to close the Menu: ")).lower()

final_bill = total + tax
bill = open("bill.txt", "w")
bill.write(f"Your Bill including all taxes and service charges: {final_bill}Rs/-")
bill.close()
