'''
Created on 2017年4月16日

@author: 阿苏
'''
import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = 'E:/我的学习/Python/code/DataMing/Arcitle/'
allText = ''
allText = PlaintextCorpusReader(corpus_root, ['demo_1.txt'])
# print(type(allText))
sinica_text = nltk.Text(allText.words())
mytexts = nltk.TextCollection(allText)
print (len(mytexts._texts))
print (len(mytexts))
the_set = set(sinica_text)
print (len(the_set))
for tmp in the_set:
    print (tmp, "tf", mytexts.tf(tmp, allText.raw(['demo_1.txt'])), "idf", mytexts.idf(tmp), mytexts.tf_idf(tmp, allText.raw(['demo_1.txt'])))