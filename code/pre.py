#line is a line of text
def preprocess_line(text_line):
    #punctuation list without the '.' character
    list1 = [chr(i) for i in range(97, 123)]
    list2 = [chr(i) for i in range(65, 91)]
    list3 = [chr(i) for i in range(48,58)]
    list4 = ['.',' ','?','!']
    clist = list1 + list2 + list3 + list4
    #remove all the characters in the punctuation list
    text_line = "".join(chs for chs in text_line.replace('?','.').replace('!','.') if chs in clist )
    #lowercase all the remaining characters
    text_line = text_line.lower()
    #convert all digits to '0'
    for i in range(9):
        text_line = text_line.replace(str(i+1),"0")
    #add two '#' both in front of and behind of the text_line
    text_line = '##' + text_line + '#'
    #return the line after preprocessing    
    return text_line

if __name__== '__main__':
    path1 = R'C:\Users\cesar\Desktop\anlp_asgn1\training.en'  
    output = []
    with open(path1) as f:
        lines = f.readlines()
    for line in lines:
        line = preprocess_line(line)
        with open('pre-training.en', 'a+', encoding = 'utf-8') as f2:
            f2.write(line)
        f2.close()
