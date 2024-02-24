def reverse_file_contents(input_file):
    
    with open(input_file, 'r') as f:
        lines = f.readlines()

    reversed_lines = lines[::-1]

  
    with open(input_file, 'w') as f:
        for line in reversed_lines:
            f.write(line)


input_file = 'f1.txt'

reverse_file_contents(input_file)
