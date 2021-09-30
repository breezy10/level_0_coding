def vowelfinder():
    word = "beautiful"
    #import pdb; pdb.set_trace()
    string = word.lower()
    list = ["a", "e", "i", "o", "u"]
    found = []
    for char in string:
        if char in list:
            found.append(char)
    print("Vowels found: ", ', '.join(found))
vowelfinder()