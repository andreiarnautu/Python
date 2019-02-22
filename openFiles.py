my_file = open("/home/andi/Documents/Code/Python/sample.txt")
content = my_file.read()
print(content + "Ends here")

content2 = my_file.read()
print(content2 + "Ends here")

my_file.seek(0)
content3 = my_file.read()
print(content3 + "Ends here")