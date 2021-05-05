x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


x[1][0]=15
print(x)
students[0]["last_name"] = "Bryant"
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
z[0]["y"]=30
print(z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(original_list):
    for dict in original_list:
        f_name = dict["first_name"]
        l_name = dict["last_name"]
        print(f"first_name - {f_name}, last_name - {l_name}")

iterate_dictionary(students)

def print_dict_info(key,incoming_list):
    for dict in incoming_list:
        print(dict[key])

print_dict_info("last_name",students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_loc_and_instructor(dict):
    all_keys = dict.keys()
    for key in all_keys:
        key_length = len(dict[key])
        print(f"{key_length} {key.upper()}")
        for item in dict[key]:
            print(item)
            if item == "Devon":
                break
        else:
            print("")

print_loc_and_instructor(dojo)