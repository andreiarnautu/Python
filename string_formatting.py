correct_password = "password"
name = input("Enter name: ")
password = input("Enter password: ")

while correct_password != password :
  password = input("Wrong password! Try again:")

message = "Hi %s, you have successfully logged in." % name
print(message)