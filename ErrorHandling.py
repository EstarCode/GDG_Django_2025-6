try:
    with open("abraham.txt", "r") as file:
        content = file.read()
        print(f"Wellcome  {content} ")
except FileNotFoundError:
    with open("abraham.txt", "w") as file:
        file.write("Guest")
