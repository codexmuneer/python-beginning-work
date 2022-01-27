'''A box of cookies can hold 24 cookies, and a container can hold 75 boxes of cookies. Write a
program that prompts the user to enter the total number of cookies, the number of cookies in a
box, and the number of cookie boxes in a container. The program then outputs the number of
Boxes and the number of containers to ship the cookies. Note that each box must contain the
specified number of cookies, and each container must contain the specified number of boxes. If
the last box of cookies contains less than the number of specified cookies, you can discard it and
output the number of leftover cookies. Similarly, if the last container contains less than the
number of specified boxes, you can discard it and output the number of leftover boxes.'''

# TAKING USERINPUT OF COOKIES
total_cookies = int(input("Enter total number of cookies: "))
cookie_in_box = int(input("Enter total number of cookies in a box: "))
boxes_in_container = int(input("Enter total number of cookie boxes in a container : "))

a = total_cookies // 24    # IT WILL GIVE TOTAL NUMBER OF BOXES
b = boxes_in_container // 75 # IT WILL GIVE TOTAL NUMBER OF CONTAINER
c = total_cookies % 24 # FOR LEFTOVER COOKIES
d = boxes_in_container % 75 # FOR LEFTOVER CONTAINER

print("The total number of cookies are: ", total_cookies)
print("The total number of boxes are: ", a)
print("The total number of containers to ship the cookies are: ", b)
print("The leftover cookies are: ", c)
print("The leftover boxes are: ", d)