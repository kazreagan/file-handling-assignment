#file creation and writing to the file
try:
    #create a text file named "my_file.text" in write(W) mode
    with open("my_file.txt", 'w') as file:
        #write atleast three lines of text including a mix of strings and numbers
        file.write("Hello there! this is my line 1.\n")
        file.write("this is my line 2 with a number: 28\n")
        file.write("my line 3 includes a string and a number: 12 books\n")

    print("File created and initial content written successfully.")

    #file reading and displaying contents
    with open("my_file.txt", 'r') as file:
        print("\nreading the contents of 'my_file.txt':")
        contents = file.read()
        print(contents)

    #file appending(adding additonal lines to the existing content)
    with open("my_file.txt", 'a') as file:
        file.write("this is my line 4.\n")
        file.write("this is my line 5 with a number: 128\n")
        file.write("and this is my line 6.\n")

    print("additional content appended successfully")
    
    #reading and displaying the updated contents
    with open("my_file.txt", 'r') as file:
        print("\nreading the updated contents of 'my_file.txt':")
        updated_content = file.read()
        print(updated_content)

except FileNotFoundError:
    print("error: The file was not found.")
except PermissionError:
    print("error: you do not have permision to write to the file.")
except Exception as e:
    print(f"an unexpected error occurred: {e}")
finally:
    print("\nfile handling operations completed.")
