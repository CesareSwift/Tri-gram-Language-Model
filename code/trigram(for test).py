def create_tri(pre_data):
    tri = {}
    for i in range(len(pre_data)-2):
        key = (pre_data[i],pre_data[i+1])
        if key not in tri:
            tri[key] = []
        tri[key].append(pre_data[i+2])
    create_tri_p(tri)
    

def create_tri_p(tri):
    list1 = [chr(i) for i in range(97, 123)]
    list2 = [' ','#','0','.']
    chlist = list1 + list2
    tri_p = {}
    for i in range(30):

        for j in range(30):
            key = (chlist[i],chlist[j])
            if key not in tri:
                tri[key] = []
    for key,chs in tri.items():
        c = {}
        csum = 0
        for singlech in chs:
            if singlech not in c:
                c[singlech] = 0
            c[singlech] += 1
            csum += 1 
            for m in range(30):
                catch = str(key)
                if (catch[2] == '#') & (m == '#'):
                    print('illegal')
                elif chlist[m] not in chs:
                    c[chlist[m]] = 0
        for singlech,count in c.items():
            c[singlech] = float(count+1)/(csum+30)
            line = "".join(str(i) for i in key) + "".join(str(j) for j in singlech) + " "+ str(c[singlech])
            with open('model_triadd-one.en', 'a+', encoding = 'utf-8') as f2:
                f2.write(line)
                f2.write('\n')
        tri_p[key] = c
        
    # with open('count.en', 'w', encoding = 'utf-8') as f:
    #     f.write(str(tri_p))
    # f.close()
    # print(1)
    # for key,chs in tri.items():
    #     if(len(set(chs))>1):
    #         c = {}
    #         csum = 0
    #         for singlech in chs:
    #             if singlech not in c:
    #                 c[singlech] = 0
    #             c[singlech] += 1
    #             csum += 1 
    #         for singlech,count in c.items():
    #             c[singlech] = float(count)/csum
    #             line = "".join(str(i) for i in key) + "".join(str(j) for j in singlech) + " "+ str(c[singlech])
    #             with open('model_tri1.en', 'a+', encoding = 'utf-8') as f2:
    #                  f2.write(line)
    #                  f2.write('\n')
    #             tri_p[key] = c
    #             #print(tri_p)
    #     f2.close()

if __name__== '__main__':
    path1 = R'C:\Users\cesar\Desktop\anlp_asgn1\pre-training1.en'  
    with open(path1, 'r', encoding = 'utf-8') as f:
        data = f.read()
    create_tri(data)
