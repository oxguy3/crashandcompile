import pprint
from string import ascii_uppercase

# build the decoder key
decoder = {1: ' '}
decoder_index = 3
for letter in ascii_uppercase:
    decoder[decoder_index] = letter
    decoder_index += 2

#pprint.pprint(decoder);

# loop through the input file
messages = []
with open('contact-easy.in.txt') as infile:
    msg = ""
    for line in infile:
        if "%" in line:
            messages.append(msg)
            msg = ""
        else:
            count = line.count('*')
            msg += decoder[count]
    messages.append(msg)

# pprint.pprint(messages)

for msg in messages:
    print msg
