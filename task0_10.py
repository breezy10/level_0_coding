def common_char():
    word1 = "entertainMent".lower()
    word2 = "forums".lower()
    print("Common Letters:", ', '.join(set.intersection(set(word1), set(word2))))
common_char()