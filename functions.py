def get_todos(filepath="todos.txt"):
    """ Read the text file and return
        the list of to-do items from it.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()

    return todos_local

def write_todos(todos_arg, filepath="todos.txt"):
    """Write the to-do list items
        in the text file
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

# the (__name__) value here when i executed this file is equal to __main__ , but
# when i execute the main file that would be equal to the name of the module file which is functions
#that's why the code after the line 23 not executed because when i run the main function
# the (__name__) dosen't equal to (__main__) it's equal to the file name which is function



if __name__ == "__main__":
    print("hello i don't want to execute that ")