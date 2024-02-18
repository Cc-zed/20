#---------------------BEFORE VARIANT

# try:
#     try:
#         fileObj = open("test.txt", "w+")
#         if fileObj:
#             print("file opened succsesfully")
#             fileObj.write("Hello World to all of you")
#             fileObj.write("\nOne more time")
#     finally:
#         fileObj.close()
# except Exception as e:
#     print("Error in opening file", e)

# try:
#     try:
#         fileObj = open("test.txt", "r")
#         if fileObj:
#             print("File opened succsesfully")
#             textFile = fileObj.readlines()
#             for i in textFile:
#                 print(i)

#     finally:
#         fileObj.close()
# except Exception as e:
#     print("Error in opening file", e)



#---------------------AFTER VARIANT

file_path = "Your_file_path"
try:
    with open(file_path, "w+") as fileObj:
        if fileObj:
            print("File opened successfully")
            fileObj.write("Hello World to all of you\n")
            fileObj.write("One more time\n")
except Exception as e:
    print("Error in opening file:", e)

try:
    with open(file_path, "r") as fileObj:
        if fileObj:
            print("File opened successfully")
            textFile = fileObj.readlines()
            for line in textFile:
                print(line.strip())
except Exception as e:
    print("Error in opening file:", e)

#P.S. I hope it is correct task, that needed to be done with "with open". I left before variant