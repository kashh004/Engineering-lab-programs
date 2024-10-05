# Question 6: Sort contents of a text file and write to another file

def sort_file_contents(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    sorted_lines = sorted([line.strip() for line in lines])
    
    with open(output_file, 'w') as file:
        file.write('\n'.join(sorted_lines))

input_file = input("Enter the input file path: ")
output_file = input("Enter the output file path: ")
sort_file_contents(input_file, output_file)
