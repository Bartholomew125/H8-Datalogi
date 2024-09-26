import sys

def create_reverse_txt(file: str) -> None:
    """
    Reads .txt file, copying and reversing
    file title, and reversing content line by line and.
    """
    content = reverse_list_to_str(read_file(file).splitlines()) # Reads file content, and reverses lines so that last line appear first
    title = file.split(".")[0] # removes .txt surfix from title
    write_file(title[::-1], content[::-1]) # Creates file with content, and title reversed, so that first line is first, and each line is backwards
    print("Reversed file created!") #Prints that the file was created to user

def reverse_list_to_str(w: list[str]) -> str:
    """
    Takes list and returns every element in backwards order to
    a string, each element on a new line.
    >>>reverse_list_to_str(['hello','world'])
    \n world
    \n hello
    """
    reverse_str = ""
    for line in reversed(w): #Loops backwards through each element in list
        reverse_str += "\n " + line #appending line break and line
    return reverse_str

def read_file(file: str) -> str:
    """
    Reads .txt file and returns content.
    """
    with open(file) as file:
        return file.read() # Returns file content as str

def write_file(title: str, content: str) -> None:
    """
    Creates .txt with title, and writes content in file.
    """
    with open(title+".txt", "w") as file: #writes file with title and content
        file.write(content)

if __name__ == "__main__":
    file = sys.argv[1]
    create_reverse_txt(file)
