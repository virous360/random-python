from uni import *
cleaned_words : list = json_file("cleaned").raw_read()

special_words :list[list[str]]= [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

for length_set in cleaned_words:
    for word in length_set:
        l = list(word)
        length  = len(l)
        s = len(set(l))
        if s == length : 
            special_words[cleaned_words.index(length_set)].append(word)
file = json_file("wordle_specials")
file.raw_write(special_words)