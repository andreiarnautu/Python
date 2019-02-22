#  How to write something in a file
my_file = open("employees.txt", "w")
my_file.write("oh hi mark")
my_file.close()

#  How to append text to an existing file
my_file = open("employees.txt", "a")
my_file.write("\ncaptain jack is here")
my_file.close()

#  How to read and write in a file
my_file = open("employees.txt", "a+")
print(my_file.read())
print("--------")
my_file.seek(0)
print(my_file.read())
print("--------")
my_file.write("\n")
for i in range(0, 3) :
  my_file.write(str(i) + "\n")
my_file.seek(0)
print(my_file.read())
my_file.close()

