def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file to read
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (e.g., replacing 'old' with 'new')
        modified_content = content.replace('old', 'new')
        
        # Open the output file to write the modified content
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"File modified successfully! The new content is written to '{output_filename}'")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read or write to the file.")
