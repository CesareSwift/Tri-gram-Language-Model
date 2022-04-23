def read_model(path):    
    br = {}
    br_p = {}
    with open(path, 'r', encoding= 'utf-8') as f:
        lines = f.readlines()
    for line in lines:
        key = (line[0],line[1])
        list = ''
        for i in range(9):
            list += line[i+4]
        #print(list)
        if key not in br:
            br[key] = []
#        list = line[2] + ':' + line[4]    
        br[key].append(line[2])
        for key1,chs in br.items():
            c = {}
            for singlech in chs:
                c[singlech] = float(list)    
            br_p[key1] = c
    # with open('br_p_model.en', 'w', encoding = 'utf-8') as f2:
    #     f2.write(str(br_p))
    # f2.close()

if __name__== '__main__':
    path = R'C:\Users\cesar\Desktop\anlp_asgn1\model-br.en'
    read_model(path)