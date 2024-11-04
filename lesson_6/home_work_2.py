def filter_word(list,lenWord):
    return [x for x in list if (len(x)>=lenWord)]

orginal_list=["teacher","home","kids","camera","computer","baby","salenium"]

filterted_words=filter_word(orginal_list,5)
print(filterted_words)