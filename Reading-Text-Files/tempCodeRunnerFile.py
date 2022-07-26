def read_file_content(filename):
    # [assignment] Add your code here
    with open("story.txt", "r") as file:
        data = file.read()
    # return "Hello World"
    return data