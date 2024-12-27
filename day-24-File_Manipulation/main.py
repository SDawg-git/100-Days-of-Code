
file = open("my_file.txt")          #opens file

contents = file.read()              #saves contents of file

print(contents)

file.close()                   #have to close the file, uses PC resources to keep it open


with open("my_file.txt") as file2:                   #opens file, does whatever you want it to do, then closes automatically when done
    contents = file2.read()
    print(contents)

with open("my_file.txt", mode="a") as file2:                   #opens file, does whatever you want it to do, then closes automatically when done     - mode = "w" SETS IT TO WRITE MODE
    file2.write("New Text")                                     #overwrites the existing text                                                        - mode = "a" STAND FOR APPEND, IT ADDS ONTO
                                                                                                                                         #EXISTING TEXT
