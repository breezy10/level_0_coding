def vowelfinder():
    word = ("beautiful")
    string = word.lower()
    list = ["a", "e", "i", "o", "u"]
    for char in string:
        if char in list:
            print("Vowels found: ", char)
vowelfinder()