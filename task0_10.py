def common_char():
    word1 = input("Enter 1st word: ")
    word2 = input("Enter 2nd word: ")
    w1 = set(word1)
    w2 = set(word2)
    lst = w1 & w2
    print(lst)
common_char()