'''4. Write a Python program that allows a user to type in an English day of the week (Sunday,
Monday, etc.). The program should print the Spanish equivalent, if possible. '''

'''lunes — Monday.
martes — Tuesday.
miércoles — Wednesday.
jueves — Thursday.
viernes — Friday.
sábado — Saturday.
domingo — Sunday.'''

week = input("Enter your week in english to convert it in spanish: ").lower()

if week == 'monday':
    print("lunes")
    
elif week == 'tuesday':
    print("martes")

elif week == 'wednesday':
    print("miércoles")    
    
elif week == 'thursday':
    print("jueves")
    
elif week == 'friday':
    print("viernes")

elif week == 'saturday':
    print("sábado")

elif week == 'sunday':
    print("domingo")
    
else:
    print("Invalid week!!")