def script():
    with open("log.txt", 'w') as file:
        file.write("Userlogged in")
    with open("log.txt", 'r') as file:
        logs = file.read()
        print("full login History")
        print(logs)


script()
