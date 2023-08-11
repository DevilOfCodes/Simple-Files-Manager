import os
import subprocess

FILE_TYPES = {
    "txt": "txt",
    "python": "py",
    "c++": "cpp",
    "js": "js",
    "html": "html",
    "css": "css",
    "java": "java",
    "yaml": "yaml",
    "json": "json",
    "c": "c",
    "csharp": "cs",
    "sql": "sql",
    "rust": "r",
    "go": "go",
    "jss": "jss",
}

def create_file(file_name, file_type):
    """Creates a new file with the specified name and type."""

    file_extension = "." + FILE_TYPES[file_type]

    with open(file_name + file_extension, "w") as f:
        f.write("")

def list_files():
    """Lists all the files in the current directory."""

    files = os.listdir()

    for file in files:
        print(file)

def delete_file(file_name):
    """Deletes a file."""

    os.remove(file_name)

def rename_file(file_name, new_file_name):
    """Renames a file."""

    os.rename(file_name, new_file_name)



def open_file():
    """Opens a file that the user chooses in the specified compiler."""

    file_name = input("Enter the file name: ")

    try:
        with open(file_name, "r") as f:
            contents = f.read()

            compiler_choices = ["Visual Studio Code","Atom"]
            compiler = input("Choose a compiler: ")

            path_to_compiler = ""
            if compiler == "VSCode":
                path_to_compiler = "Q:\\Programs\\Microsoft VS Code\\Code.exe"
            elif compiler == "Atom":
                path_to_compiler = "C:\\Users\\qande\\AppData\\Local\\atom\\atom.exe"

            subprocess.Popen([path_to_compiler, file_name])
    except FileNotFoundError:
        print("File not found.")

def main():
    """The main function."""

    print()
    print("*************************")
    print("       Welcome DOC;")
    print("*************************")
    print("1-create file")
    print("2-list files")
    print("3-delete file")
    print("4-rename file")
    print("5-open file")
    print("6-quit")

    done = False
    while not done:
        command = input("Enter a command: ")

        if command == "1":
            file_name = input("Enter the file name: ")
            file_type = input("Enter the file type: ")
            print("creation done DOC;")
            print("*******************")
            create_file(file_name, file_type)
        elif command == "2":
            print("***********")
            list_files()
            print("***********")
        elif command == "3":
            print("***********")
            file_name = input("Enter the file name: ")
            delete_file(file_name)
            print("Operation Done DOC;")
            print("***********")
        elif command == "4":
            print("***********")
            file_name = input("Enter the file name: ")
            new_file_name = input("Enter the new file name: ")
            rename_file(file_name, new_file_name)
            print("Operation Done DOC;")
            print("***********")
        elif command == "5":
            print("***********")
            open_file()
            print("***********")
        elif command == "6":
            # print("SEE YAA DOC;")
            done = True
        else:
            print("Invalid command.")

    print("Greetings...Your DOC;")
    

if __name__ == "__main__":
    main()
