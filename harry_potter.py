# file = open('/Users/Shane/Desktop/harrypotter.txt', 'r')
# text = file.read()
# print(text)
# for line in file:
#     print(line)
# file.close()
# with(open('/Users/Shane/Desktop/harrypotter.txt', 'r')) as file:
#     text = file.read()
# print(text[:100])
# shows first 100 characters?
# print(len(text))
# shows number of characters in harry potter
# text = text.lower()
# text = text.replace('.', '')
# text = text.replace('?', '')
# text = text.replace('!', '')
# text = text.replace("'", '')
# text = text.replace('"', '')
# text = text.replace(';', '')
# text = text.replace(':', '')
# text = text.replace('(', '')
# text = text.replace(')', '')
# text = text.replace('-', '')
# text = text.replace(',', '')
# text = text.replace('~', '')
# replaces punctuation
# sets every word to lowercase
# text_list = text.split()
# print(len(text_list))
# prints number of words in harry potter
# text_set = set(text_list)
# print(len(text_set))
# prints number of unique words in harry potter


# import random
#
# # Open file
# with open('/Users/Shane/Desktop/harrypotter.txt', 'r') as file:
#    text = file.read()
#
# # Make lowercase
# text = text.lower()
#
# # Remove punctuation
# text = text.replace(',', '')
# text = text.replace(':', '')
# text = text.replace('.', '')
# text = text.replace('?', '')
# text = text.replace(')', '')
# text = text.replace("(", '')
# text = text.replace('"', '')
# text = text.replace('!', '')
# text = text.replace(';', '')
# text = text.replace('-', '')
# text = text.replace("'s", '')
# text = text.replace("'t", '')
#
# # Turn into a list
# tlist = text.split()
#
# # Print how many words
# print(len(tlist))
#
# # How many times Harry appears
# print('Harry appears:', tlist.count('harry'))
# print('Hermione appears:', tlist.count('hermione'))
# print('Ron appears:', tlist.count('ron'))
# print('Hagrid appears:', tlist.count('hagrid'))
# print('Slytherin appears:', tlist.count('slytherin'))
# print('like appears:', tlist.count('like'))
# print('said appears:', tlist.count('said'))
# print('and appears:', tlist.count('and'))
#
# # Print how many unique words
# print('Unique word count:', len(set(tlist)))
#
# unique_list = list(set(tlist))  # turn the unique set to a list
#
# rword = random.choice(unique_list)
# print('Random word:', rword, 'appears', tlist.count(rword), 'time(s).')

file_handler = open('/Users/Shane/Desktop/harrypotter.txt', 'r')
text = file_handler.read()
file_handler.close()
text = text.lower()
text = text.replace('.', '')
text = text.replace('?', '')
text = text.replace('!', '')
text = text.replace("'", '')
text = text.replace('"', '')
text = text.replace(';', '')
text = text.replace(':', '')
text = text.replace('(', '')
text = text.replace(')', '')
text = text.replace('-', '')
text = text.replace(',', '')
text = text.replace('~', '')
tlist = text.split()
ulist = list(set(tlist))
ulist.sort()
# for w in ulist:
#     print(w, 'appears', tlist.count(w))


fo = open('/Users/Shane/Desktop/hp_wordcounts.txt', 'w')
for w in ulist:
    print(w, 'appears', tlist.count(w), file = fo)
fo.close()