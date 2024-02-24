def create_dictionary_from_file(file_path, delimiter=':'):
    dictionary = {}
    with open(file_path, 'r') as file:
        for line in file:
           
            parts = line.strip().split(delimiter, 1)
         
            if len(parts) == 2:
                key, value = parts
               
                key = key.strip()
                value = value.strip()
               
                dictionary[key] = value
            else:
                print(f"Ignoring line '{line.strip()}' as it doesn't contain a valid key-value pair.")

    return dictionary


file_path = 'file3.txt'


my_dictionary = create_dictionary_from_file(file_path)

print("Dictionary created from file:")
print(my_dictionary)
