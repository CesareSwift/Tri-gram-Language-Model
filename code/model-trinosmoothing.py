import numpy as np
np.set_printoptions(suppress = True)
#an empty dictionary
tri = {}

#preprocessing each line of the text
def preprocess_line(text_line):
    #using chr to get a-z from ASCII
    list1 = [chr(i) for i in range(97, 123)]
    #using chr to get A-Z from ASCII
    list2 = [chr(i) for i in range(65, 91)]
    #using chr to get 0-9 from ASCII
    list3 = [chr(i) for i in range(48,58)]
    #a list contains '.' and ' '
    list4 = ['.',' ']
    clist = list1 + list2 + list3 + list4
    #remove all the characters not in character list
    #text_line = "".join(chs for chs in text_line.replace('\n',' ') if chs in clist )
    text_line = "".join(chs for chs in text_line if chs in clist )
    #text_line = "".join(chs for chs in text_line.replace('?', ' ') if chs in clist )
    #lowercase all the remaining characters
    text_line = text_line.lower()
    #convert all digits to '0'
    for i in range(9):
        text_line = text_line.replace(str(i+1),"0")
    #add two '#' in front of text_line and one '#' behind of the text_line
    text_line = '##' + text_line + '#'
    #return the line after preprocessing   
    return text_line

#create a dictionary which key is the first two characters of a trigram and value is the third character
def create_tri(pre_data):
    for i in range(len(pre_data)-2):
        key = (pre_data[i],pre_data[i+1])
        if key not in tri:
            tri[key] = []
        tri[key].append(pre_data[i+2])
    return tri

#create two new dictionaries to finish a dictionary which holds all the probabilities from the trigrams    
def create_tri_p(tri, a):
    #using chr to get a-z from ASCII
    list1 = [chr(i) for i in range(97, 123)]
    list2 = [' ','#','0','.']
    #get the vocabulary of the trigram
    chlist = list1 + list2
    #create a new empty dictionary
    tri_p = {}
    #compelet the dictionary with the keys which don't have any value in the training data 
    # for i in range(30):
    #     for j in range(30):
    #         key = (chlist[i],chlist[j])
    #         #the key such as 'a#' is illegal for the trigram model 
    #         if (chlist[i] != '#') & (chlist[j] == '#'):
    #             print('illegal')
    #         elif key not in tri:
    #             tri[key] = []  
    for key,chs in tri.items():
        #create a new empty dictionary to store the probabilities
        c = {}
        csum = 0
        catch = str(key)
        #get the count of each character which follows the key
        for singlech in chs:
            if singlech not in c:
                c[singlech] = 0
            c[singlech] += 1
            csum += 1 
            #set the value of the character which does not follow the key to 0
        # for m in range(30):
        #     #trigrams such as '###' and '#a#' is alos illege for the model
        #     if (catch[2] == '#') & (chlist[m] == '#'):
        #         print('illegal')
        #     #give a count 0 to the value   
        #     elif chlist[m] not in chs:
        #         c[chlist[m]] = 0
        for singlech,count in c.items():
            #trigrams begin with bigrams such as '##' and 'a#' only have 29 vocabularies
            # if catch[2] == '#':
            #     c[singlech] = floatcount)/csum
            #calculate the trigram probabilities using add-one smoothing
            # else:
            c[singlech] = float(count)/(csum)
            #write the probabilities of trigram into the file line by line using scientific notation
            line = "".join(str(i) for i in key) + "".join(str(j) for j in singlech) + " "+ str('%.3e'%c[singlech])
            with open('model_triadd_nosm.en', 'a+', encoding = 'utf-8') as f3:
                f3.write(line)
                f3.write('\n')
        tri_p[key] = c


if __name__== '__main__':
    path1 = R'C:\Users\cesar\Desktop\anlp_asgn1\training.en'  
    output = []
    #read the file line by line
    with open(path1) as f:
        lines = f.readlines()
    for line in lines:
        line = preprocess_line(line)
        tri = create_tri(line)
        #print(line)
        with open('pre-training.en', 'a+', encoding = 'utf-8') as f2:
            f2.write(line)
        f2.close()
    a = 0.5
    create_tri_p(tri,a)