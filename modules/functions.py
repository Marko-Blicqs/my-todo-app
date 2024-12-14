FILEPATH = "files/todo.txt"

def get_todos(file_path=FILEPATH):
    """Return the to-do list from the specified file."""
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()

    return todos_local

def write_todos(content, file_path=FILEPATH):
    """Write the to-do list to the specified file."""
    with open(file_path, 'w') as file_local:
        file_local.writelines(content)

#print(f"__name__ == {__name__}")

if __name__ == "__main__":
    """
    Note that __main__ has only has the value of 'main' when the file is run directly.
    If the file is run from an import command, it has the value of that import command.
    Hence, we can use the preceding IF statement to conditionally run code IFF, a file
    is being run directly.
    
    This technique is often used when building web apps.
    """
    print(f"Hello from functions.py. This message only appears when this file is run directly." \
            f"\nThe variable '__name__' == {__name__}")