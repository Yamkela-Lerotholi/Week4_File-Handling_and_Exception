def safe_file_read(filename):
    try:
        # Try opening the file to read
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    
    except IOError:
        print(f"Error: There was an issue reading the file '{filename}'.")
