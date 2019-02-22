from datetime import datetime

current_date = datetime.now()

solution_file = open(current_date.strftime("%Y-%m-%d-%H-%M"), "w")

file_1 = open("/home/andi/Downloads/file1.txt", "r")
file_2 = open("/home/andi/Downloads/file2.txt", "r")
file_3 = open("/home/andi/Downloads/file3.txt", "r")

content_1 = file_1.read()
content_2 = file_2.read()
content_3 = file_3.read()

solution_file.write(content_1 + "\n")
solution_file.write(content_2 + "\n")
solution_file.write(content_3 + "\n")