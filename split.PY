firstsentence = input(">")
empty_list= []
empty_string = ""
for char in firstsentence:
    if char == " ":
        empty_list.append(empty_string)
        empty_string = ""
    else:
        empty_string = empty_string + char
print(empty_list)