'''
Created on 2017年4月16日

@author: 阿苏
'''
import jieba
with open('E:\我的学习\Python\code\DataMing\Arcitle\demo.txt','r',encoding = 'utf-8') as f:
    tmp_line = f.read()
    jieba_cut = jieba.cut(tmp_line)
    ans = ' '.join(jieba_cut)
    with open('E:\我的学习\Python\code\DataMing\Arcitle\demo_1.txt','w',encoding = 'utf-8') as f2:
        f2.write(ans)