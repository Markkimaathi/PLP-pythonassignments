def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")
        return None

def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"File '{filename}' has been written successfully.")
    except IOError:
        print(f"Error: Could not write to the file '{filename}'.")

def main():
    filename = input("Enter the filename to read: ")
    content = read_file(filename)
    
    if content is not None:
        modified_content = content + "\nFile has been modified.\n"
        new_filename = filename.rsplit('.', 1)[0] + '_modified.' + filename.rsplit('.', 1)[1]
        write_file(new_filename, modified_content)

if __name__ == "__main__":
    main()