def number_to_text(number):
   
    num_to_text = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    text_representation = ''
    for digit in str(number):
        if digit.isdigit():
            text_representation += num_to_text[digit]
        else:
            text_representation += digit  
    return text_representation

def convert_numbers_to_text(input_file, output_file):
    
    with open(input_file, 'r') as f:
        contents = f.read()

    converted_contents = ''
    for word in contents.split():
        if word.isdigit():
            converted_contents += number_to_text(word) + ' '
        else:
            converted_contents += word + ' '

  
    with open(output_file, 'w') as f:
        f.write(converted_contents)


input_file = 'file2.txt'
output_file = 'converted_file.txt'

convert_numbers_to_text(input_file, output_file)
