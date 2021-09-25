# calculating bill of resturant and showing menu of resturant items : burger = 5$, pizza = 15$, cake = 10$
 #no of categories wanted by customer 
 #no of items of that category
 #if more than one category then keep asking no of items of other categories
 #Finally calculate the bill
print("Menu of restaurant")
print("burger = 5$")
print("pizza = 15$")
print("cake = 10$") 

print("how many burgers you want?")
burgers = int(input())

print("how many pizzas you want?")
pizzas = int(input())

print("how many cakes you want?")
cakes = int(input())

print("Your bill is: ", burgers*5 + pizzas*15 + cakes*10)
    
    
    