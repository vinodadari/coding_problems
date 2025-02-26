"""
ls = ["A","B",["A",["B",["A"]]]] - 3

list_values = {value: occurances = 1 } if it is a string
step 1 - for loop
    if value in list_values
        list_values += 1
    else
        list_values = 1

"""
# Output : {A:3,B:2}
ls = ["A","B",["A",["B",["A"]]]]

output = {}
def get_list_occurances(output, list_data):
    for value in list_data:
        if isinstance(value, list):
            get_list_occurances(output, value)
        elif value in output:
            output[value] += 1
        else:
            output[value] = 1
get_list_occurances(output, ls)
print(output)
