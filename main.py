PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names  = names_file.readlines()  #le o arquivo jogando para dentro da variavel em forma de lista
    print(names)