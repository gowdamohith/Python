def count_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.lower().split()
            word_count = {}
            
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
            
            # Print the results
            for word, count in word_count.items():
                print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: There was an issue reading the file '{filename}'.")

# Example usage
count_words('example.txt')




def write_and_read_file(filename):
    try:
        # Write user input to the file
        with open(filename, 'w', encoding='utf-8') as file:
            user_input = input("Enter some text to write to the file: ")
            file.write(user_input)
        
        # Read the content back from the file
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("\nContent read from the file:")
            print(content)
    
    except IOError as e:
        print(f"An error occurred: {e}")

# Example usage
write_and_read_file('user_input.txt')

def modify_file(filename, old_word, new_word):
    try:
        # Read the entire content of the file
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace the word in the content
        new_content = content.replace(old_word, new_word)
        
        # Write the modified content back to the file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(new_content)
        
        print(f"The word '{old_word}' has been replaced with '{new_word}' in '{filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError as e:
        print(f"An error occurred while modifying the file: {e}")

# Example usage
modify_file('example.txt', 'old', 'new')