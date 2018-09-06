text = input("Text: ")
word_list = text.split()
i = 0
max_word_length = 0
word_group = {}
for words in word_list:
    words = words.lower()
    if words in word_group:
        word_group[words] += 1
    else:
        word_group[words] = 1
    if len(words) > max_word_length:
        max_word_length = len(words)
ordered_word_list = list(word_group.keys())
ordered_word_list.sort()

for words in ordered_word_list:
    print("{:{}} : {}".format(words, max_word_length, word_group[words]))

##changes