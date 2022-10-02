PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names  = names_file.readlines()  #le o arquivo jogando para dentro da variavel em forma de lista

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read() 
    for name in names: 
        new_leter = letter_contents.replace(PLACEHOLDER,name) #replace é um método que substitui o que está definito entre (anterior,novo).

