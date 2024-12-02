def read_and_write_file():
    try:
        # Ask the user for the input and output filenames
        input_filename = input("Enter the name of the file to read: ")
        output_filename = input("Enter the name of the file to write to: ")

        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()  # Read the content of the file

        # Modify the content (example: appending a string)
        modified_content = content + "\n\n-- End of File --"  # Modify the content

        # Open the output file in write mode and write the modified content
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)  # Write the modified content

        print(f"File has been read from '{input_filename}' and written to '{output_filename}' successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: There was a problem reading or writing to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_and_write_file()
