#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) #print the number 5


# #2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()) #error becasue the other function is not defined


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold()) #print the number 5


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers()) #print the number 5


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x) # print 5 then print none


#6
def add(b,c):
    print(b+c)
    #return(b+c)
print(add(1,2) + add(2,3)) #print 3 print 5 print 8 #actually doesnt print 8 because it never returns the value


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5)) #print the string "25"


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents()) #print the number 100 print the number 10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) #print the number and return 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #print the number and return 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #print the total of 7+14 which is 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5)) #print the number 8


#11
b = 500
print(b)  #print 500
def foobar():
    b = 300
    print(b)
print(b) #print 500
foobar() #print 300
print(b) #print 500


#12
b = 500
print(b) #print 500
def foobar():
    b = 300
    print(b)
    return b
print(b) #print 500
foobar() #print 300
print(b) #print 500


#13
b = 500
print(b) #print 500
def foobar():
    b = 300
    print(b) #print 300
    return b
print(b) #print 500
b=foobar() 
print(b) #print 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo() #print 1 then 3 then 2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo() 
print(y) #print 1 then 3 then 5 then 10