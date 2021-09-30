def common_char():
    word1 = ("entertainment")
    word2 = ("forums")
    w1 = set(word1)
    w2 = set(word2)
    lst = w1 & w2
    print(lst)
common_char()