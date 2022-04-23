import numpy as np

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
        br[key].append(line[2])
        #create a dictionary for each value to store the probabilities
        for key1,chs in br.items():
            c = {}
            for singlech in chs:
                if singlech not in c:
                #change the list of probability to float
                    c[singlech] = float(list)

            br_p[key1] = c
            # print(br_p[key1])
    print('Read Done!')    
    print(br_p)
    return br_p

#the Mark of citing：this is from the file lab-w2.py
#we cite this function to get random characters
def generate_random_sequence(distribution, N):
    outcomes = np.array(list(distribution.keys()))
    probs = np.array(list(distribution.values()))
    bins = np.cumsum(probs)
    #because the sum of some bins is not equal to 1(the probabilities are approximate)
    #instead of using the origin function which generate the value from 0-1
    #we generate the value from 0 to the sum of the bins
    max = 0
    for i in range(len(bins)):
        if float(bins[i]) >= max:
            max = float(bins[i])   
    ran = np.random.uniform(0, max)

    return list(outcomes[np.digitize(ran, bins)])

def generate_from_LM(br_p, N):
    str_br = '##'  
    for i in range(N):
        distribution = {}
        key = (str_br[i],str_br[i+1])
        # print(key)
        #when we generate '#' when are not at the end of the generating sequence
        #we use key '##' to replace the illgal keys such as 'a#' to keep generating character
        if ((str_br[i] != '#') & (str_br[i+1] == '#')):
            key = (str_br[i+1],str_br[i+1])
        distribution = br_p[key]
        # print(distribution)
        list_new = generate_random_sequence(distribution, 1)
        #add the new geneated character to the output string
        # print(str(list_new[0]))
        str_br += str(list_new[0])
    return str_br

if __name__== '__main__':
    path = R'C:\Users\cesar\Desktop\ANLP\model-br.en'
    br_p = read_model(path)
    str_br = generate_from_LM(br_p, 300)
    with open('generating1.en', 'w', encoding = 'utf-8') as f:
        f.write('##')
        for i in range(len(str_br)):
            if (i != 0) & (i != 1):
                if str_br[i] == '#':
                    #add a line break after the generated '#'
                    f.write(str_br[i]+'\n')
                else :
                    f.write(str_br[i])
    f.close()




