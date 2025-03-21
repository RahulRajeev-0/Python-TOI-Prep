with open(r"file path", 'a+') as file:
    file.write("\n This is new")
    content = file.read()
    print(content)


'''
syntax = with open('filepath', 'read') as file:

'''