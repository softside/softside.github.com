# md = open("c4f_api.md",'a+')
# for one in md.readlines():
#     if one[1]==')':
#         one.insert('*',0)

# md.close()

fileReadObj = open("c4f_api.md")
fileWriteObj = open("output.txt", 'a+')
fileLineText = fileReadObj.readline()
while ('' != fileLineText):
    if fileLineText[1]==')':
        string = fileLineText.insert('*',0)
        fileWriteObj.write(string)
        fileLineText = fileReadObj.readline()

fileReadObj.close()
fileWriteObj.close()
