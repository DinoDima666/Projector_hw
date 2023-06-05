with open("file_with_some_content.txt", "r") as input_file, open("file_in_upper.txt", "w") as output_file:
    text = input_file.read()
    print(text)
    output_file.write(text.upper())
