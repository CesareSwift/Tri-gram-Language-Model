import math

#preprocessing each line of the text
def preprocess_line(text_line):
    #using chr to get a-z from ASCII
    list1 = [chr(i) for i in range(97, 123)]
    #using chr to get A-Z from ASCII
    list2 = [chr(i) for i in range(65, 91)]
    #using chr to get 0-9 from ASCII
    list3 = [chr(i) for i in range(48,58)]
    #a list contains '.' , ' ' , '?' ,'!'
    list4 = ['.',' ','?','!']
    clist = list1 + list2 + list3 + list4
    #remove all the characters not in character list, replace '?' and '!' with '.'
    text_line = "".join(chs for chs in text_line.replace('?','.').replace('!','.') if chs in clist )
    #lowercase all the remaining characters
    text_line = text_line.lower()
    #convert all digits to '0'
    for i in range(9):
        text_line = text_line.replace(str(i+1),"0")
    #add two '#' in front of text_line and one '#' behind of the text_line
    text_line = '##' + text_line + '#'
    #return the line after preprocessing   
    return text_line

#read the model from file
def read_model(path):    
    br = {}
    br_p = {}
    #read the file line by line
    with open(path, 'r', encoding= 'utf-8') as f:
        lines = f.readlines()
    for line in lines:
        #the first two characters are the key
        key = (line[0],line[1])
        #read the probability of the line
        list = ''
        for i in range(9):
            list += line[i+4]
        #create the key if it never occured in previous lines
        if key not in br:
            br[key] = [] 
        #the value of the key is the third character
        br[key].append(line[2])
        #create a dictionary for each value to store the probabilities
        for key1,chs in br.items():
            c = {}
            for singlech in chs:
                #change the list of probability to float
                c[singlech] = float(list)
            br_p[key1] = c
    print('Read Done!')    
    return br_p

#calculate the perplexity by the test file and the model
def compelet_perplexity(text, model,listp):

    #begin with the third character in the text
    for i in range(len(text)-2):
        key = (text[i],text[i+1])
        value = model[key]
        #print(text[i+2])
        #print(value)
        #store the probability in the listp
        if float(value[text[i+2]]) == 0:
            print('erro')
        listp.append(math.log(float(value[text[i+2]])))
    return listp

def calculation(listp,count1):
    #calculate the product
    p = 0
    for i in range(len(listp)):
        p += listp[i]
    n = count1
    #print(p)
    #the length of the text
    #print(n)
    #do the calculation of the extraction of root
    #p = math.pow(p,1/n)
    p = p/n
    p = math.pow(10,p)
    return p


if __name__== '__main__':
    path = R'C:\Users\cesar\Desktop\anlp_asgn1\test.txt'
    path1 = R'C:\Users\cesar\Desktop\code\model_triadd_alpha0001.es'
    br_p = read_model(path1)
    with open(path) as f:
        lines1 = f.readlines()
        listp = []
        p = 1
        count1 = 0
    for line1 in lines1:
        line1 = preprocess_line(line1)
        if line1 != '###':
            listp = compelet_perplexity(line1, br_p, listp)
            count1 += len(line1) - 2
    ppp = calculation(listp, count1)
    print('p:', ppp)
    with open('pp.en', 'a+', encoding = 'utf-8') as f3:
        f3.write('p:')
        f3.write(str(ppp))
        f3.write('\n')
    f3.close() 
    