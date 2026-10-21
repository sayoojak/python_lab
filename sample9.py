try:
    with open("sample.txt", "w") as file:
        file.write("Welcome to Python programming!")
 
    with open("sample.txt", "r") as file:
        content = file.read()
 
    print("File content:", content)
 
except FileNotFoundError:
    print("File not found")
 
except OSError as e:
    print("File error:", e)
