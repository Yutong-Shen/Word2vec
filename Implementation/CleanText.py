#coding:utf-8
import  os
import  re
import gensim, pprint
from gensim.parsing.preprocessing import preprocess_string
from gensim.parsing.preprocessing import strip_tags,strip_punctuation,strip_numeric,strip_non_alphanum
from gensim.parsing.preprocessing import strip_multiple_whitespaces

def read_file_by_lines(file):
    with open(file, mode='r', encoding='utf-8') as f:
        for line in f:
            yield line


def delete():
    filter = [strip_tags, strip_punctuation, strip_numeric, strip_non_alphanum, strip_multiple_whitespaces]
    print('Start--------')
    inputfile='D:/wiki.txt'
    outfile=open('D:/'+'clean_wiki.txt','w',encoding = 'UTF-8')
    lines = read_file_by_lines(inputfile)
    i = 0
    for line in lines:
        if i % 100000 == 0:
            print(i)
        i += 1
        line = preprocess_string(line, filter)
        outfile.write(" ".join(line) + '\n')
    outfile.close()
    print('Done--------')

delete()
