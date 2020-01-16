with open("file.txt", "r") as f:
    words = f.read().split() #split words into a list

    for i in range(len(words)):
        if len(words[i]) > 3:
            first_letter = words[i][0]
            words[i] = words[i].replace(words[i][0], "")
            words[i] = words[i] + first_letter + "ay"

    print(words)
        
