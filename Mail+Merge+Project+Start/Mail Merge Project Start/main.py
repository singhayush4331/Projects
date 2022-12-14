#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", mode="r") as l:
    # print()
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
        le = letter.readlines()
        head1 = le[0]
        head = le[0]
    names = l.readlines()
    for i in names:
        new_name = i.replace("\n", "")
        with open(f"./Input/Letters/{new_name}", mode="w") as new_letter:

            new_head = head.replace("[name]", new_name)
            print(new_head)
            # m = le[0].replace("[name]", )
            new_letter.write(new_head)
            for i in le[1:]:
                new_letter.write(i)



