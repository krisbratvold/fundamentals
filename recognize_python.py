num1 = 42 #variable decleration, numbers
num2 = 2.3 #variable decleration, number, float
boolean = True  #boolean, data type 
string = 'Hello World' #string, data type
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary, boolean, string, number
fruit = ('blueberry', 'strawberry', 'banana') #list
print(type(fruit)) #log statement access value list 
print(pizza_toppings[1]) #log acces list sausage 
pizza_toppings.append('Mushrooms') #add value mushrooms to list
print(person['name']) #log access dictionary John
person['name'] = 'George' #change value dictionary 
person['eye_color'] = 'blue' #add value dictionary
print(fruit[2]) #log list banana

if num1 > 45:
    print("It's greater") #conditional if
else:
    print("It's lower") #conditional else

if len(string) < 5:
    print("It's a short word!") #conditional if
elif len(string) > 15: #conditional else if 
    print("It's a long word!") #log
else:
    print("Just right!") #conditional else log 

for x in range(5): #for loop start 0 end 5 log x
    print(x)
for x in range(2,5): #for loop start 2 end 5 log x
    print(x)
for x in range(2,10,3): #for loop start 2 end 10 increment 3
    print(x)
x = 0    
while(x < 5): #while loop x less than 5 log x increment 1
    print(x)
    x += 1

pizza_toppings.pop() #delete value to list
pizza_toppings.pop(1) #delete value sausage

print(person) #log dicitonary
person.pop('eye_color') #delete value eye color form dictionary
print(person) #log dictionary

for topping in pizza_toppings:  #for loop if conditional break
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): #function 
    for num in range(10): #for loop start 0 end 10
        print('Hello') #log

print_hello_ten_times()

def print_hello_x_times(x): #function
    for num in range(x): #for loop start end x
        print('Hello') #log

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #function
    for num in range(x): #for loop end x=10
        print('Hello') #log

print_hello_x_or_ten_times() #log hello ten times
print_hello_x_or_ten_times(4) #log hello 4 times


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)