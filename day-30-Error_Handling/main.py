
# #FileNotFound
# with open("a_file.txt") as file:
#     file.read()
#
# #KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]

#IndexErrors  (calling list item outside of range)

#TypeError (adding text to a number, etc)

cost = 5
string = "Zingers"

try:                                    #try the code that MIGHT cause an exception
    zinger_cost = cost + string
except TypeError:                      #Do this if there WAS an exception (and OPTIONALLY name the exception)
    print("can't do that")
#else:                                  #do this if there were NO exceptions

#finally:                               #Do this NO MATTER what happens

#raise:                                 #Lets you raise own exceptions


#FileNotFound
try:
    file = open("a_text_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["asdasd"])
except FileNotFoundError:
    print("File not found; creating...")
    file = open("a_text_file.txt", "w")
except KeyError as error_message:
    print(f"Key {error_message} not found, try again...")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
    #raise KeyError("Bazinga")                      #makes your own error



height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")              #one use for creating your own errors

bmi = weight / height ** 2
print(bmi)
