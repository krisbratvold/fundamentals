#part 1
def countdown(start):
    countdown_list= []
    for num in range(start,-1,-1):
        countdown_list.append(num)
    return(countdown_list)
print(countdown(5))

#part 2
def print_and_return(list):
    for index in range(len(list)):
        if index == 0:
            print(list[index])
        else:
            return(list[index])

print_and_return([2,5])

#part 3
def first_plus_length(list):
    for index in range(len(list)):
        if index == 0:
            first_number = list[index]
        return(first_number + len(list))

print(first_plus_length([2,3,4,5,6]))

#part 4
def value_greater_than_second(list):
    new_list=[]
    for index in range(len(list)):
        if(len(list)) <= 2:
            return(False)
        if list[index] > list[1]:
            new_list.append(list[index])
    print(len(new_list))
    return(new_list)

print(value_greater_than_second([5,2,3,4,5,6,1,1,1]))

#part 5
def length_and_value(length=4,value=7):
    list=[]
    for index in range(length):
        list.append(value)
    return(list)

print(length_and_value(6,8))