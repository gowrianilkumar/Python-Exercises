def reverse_dictionary(ascii_dict):
    reversed_dict = {value: key for key, value in ascii_dict.items()}
    return reversed_dict


ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
result = reverse_dictionary(ascii_dict)
print(result)  
