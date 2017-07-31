import pprint
from string import ascii_uppercase

# build the decoder key
decoder = {0: ' '}
decoder_index = 1
for letter in ascii_uppercase:
    decoder[decoder_index] = letter
    decoder_index += 1

#pprint.pprint(decoder);

# loop through the input file
data = []
with open('contact-hard.in.txt') as infile:
    msg = []
    for line in infile:
        if "%" in line:
            data.append(msg)
            for l in msg:
                print l
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            msg = []
        else:
            ctPeriod = line.count('.')
            ctLittle = line.count('o')
            ctBig    = line.count('O')
            ctZero   = line.count('0')

            left = ctLittle - ctBig
            right = ctZero - ctPeriod
            fuck = (ctPeriod + ctZero) - (ctLittle + ctBig)
            msg.append(str(ctPeriod)+"\t"+str(ctLittle)+"\t"+str(ctBig)+"\t"+str(ctZero)+"\t###\t"+str(left+right)+"\t"+str(fuck))
    data.append(msg)

#pprint.pprint(data)

print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

# loop through the input file
messages = []
with open('contact-hard.in.txt') as infile:
    msg = []
    notTooBig = [True, True, True, True]
    stillSequential = [True, True, True, True]
    sequenceDirection = ["", "", "", ""]
    for line in infile:
        if "%" in line:
            lastRow = []
            # use process of elimination to figure out which signal the one we want
            for row_idx in range(len(msg)):
                row = msg[row_idx]
                print "########################################"
                #print "ROWLEN:"+str(len(row))
                for i in range(len(row)):
                    #pprint.pprint(lastRow)
                    m = row[i]
                    if m > 27:
                        notTooBig[i] = False
                    if row_idx > 0:
                        if stillSequential[i]:
                            print i
                            pprint.pprint(lastRow)
                            pprint.pprint(row)
                            print sequenceDirection[i]
                            if sequenceDirection[i] == "":
                                if lastRow[i]+1 == m:
                                    sequenceDirection[i] = "up"
                                elif lastRow[i]-1 == m:
                                    sequenceDirection[i] = "down"
                                else:
                                    stillSequential[i] = False
                                    break

                            if lastRow[i] == 26:
                                sequenceDirection[i] = "down"
                            if lastRow[i] == 1:
                                sequenceDirection[i] = "up"

                            if sequenceDirection[i] == "up" and lastRow[i]+1 != m:
                                stillSequential[i] = False
                            if sequenceDirection[i] == "down" and lastRow[i]-1 != m:
                                stillSequential[i] = False
                            print stillSequential[i]
                            print "@@@@@@@@@@@"
                lastRow = row
            pprint.pprint(notTooBig)
            pprint.pprint(stillSequential)
            exit()
            print ("###")
            for col in range(4):
                if notTooBig[col] and stillSequential[col]:
                    fullMessage = ""
                    for l in msg:
                        fullMessage += decoder[l[col]]
                        msg = []
                    messages.append(fullMessage)
                    break
        else:
            ctPeriod = line.count('.')
            ctLittle = line.count('o')
            ctBig    = line.count('O')
            ctZero   = line.count('0')
            msg.append([ctPeriod, ctLittle, ctBig, ctZero])
    #messages.append(msg)

# pprint.pprint(messages)

for msg in messages:
    print msg
