import pprint
from string import ascii_uppercase
from string import ascii_lowercase

# build the decoder key
decoder = {
 4: 'B',
 6: 'C',
 8: 'D',
 10: 'E',
 12: 'F',
 14: 'G',
 16: 'H',
 18: 'I',
 20: 'J',
 26: 'K',
 28: 'L',
 36: 'M',
 38: 'N',
 40: 'O',
 42: 'P',
 46: 'Q',
 48: 'R',
 50: 'S',
 54: 'T',
 56: 'U',
 58: 'V',
 68: 'W',
 70: 'X',
 72: 'Y',
 78: 'Z',
 80: 'A'
}

#{40: ' '}

# decoder_index = 41
# for letter in ascii_uppercase:
#     decoder[decoder_index] = letter
#     decoder_index += 1
# for letter in ascii_lowercase:
#     decoder[decoder_index] = letter
#     decoder_index += 1
#
# pprint.pprint(decoder);

# loop through the input file
data = []
with open('contact-medium.sample-in.txt') as infile:
    msg = []
    for line in infile:
        if "%" in line:
            #pass
            pprint.pprint(len(msg))
            data.append(msg)
            #pprint.pprint(sorted(set(msg)))
            msg = []
        else:
            count = line.count('*')
            #prefix = line.split('*')[0]
            #spacecount = prefix.count(' ')
            msg.append(count)
    #pprint.pprint(len(sorted(set(msg))))
    data.append(msg)
pprint.pprint(data)

## loop through the input file
messages = []
with open('contact-medium.sample-in.txt') as infile:
    msg = ""
    for line in infile:
        if "%" in line:
            messages.append(msg)
            msg = ""
        else:
            count = line.count('*')
            # prefix = line.split('*')[0]
            # spacecount = prefix.count(' ')
            msg += decoder[count]
    messages.append(msg)

#pprint.pprint(messages)

# for msg in messages:
#     print msg
