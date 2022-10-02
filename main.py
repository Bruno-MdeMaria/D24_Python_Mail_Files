PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names  = names_file.readlines()  #le o arquivo jogando para dentro da variavel em forma de lista

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read() 
    for name in names: 
        somente_name = name.strip()  #método python que retira espaços antes e depois das strings.
        new_letter = letter_contents.replace(PLACEHOLDER,somente_name) #replace é um método que substitui o que está definito entre (anterior,novo).
        with open(f".\Output\ReadyToSend\letter_for_{somente_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
