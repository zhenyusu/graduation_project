'''
Created on 2017年4月15日

@author: 阿苏
'''
# encoding=
import jieba
from _collections_abc import generator
#Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
#我来到北京清华大学
seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式


seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("精确模式: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut_for_search("我来到北京清华大学")# 搜索引擎模式
print("搜索引擎模式:"+",".join(seg_list))


seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print("精确模式："+", ".join(seg_list))


seg_list = jieba.cut("小明硕士毕业于中国科学院计算所，后在日本京都大学深造") # 默认是精确模式
print("精确模式："+", ".join(seg_list))

seg_list = jieba.cut("小明硕士毕业于中国科学院计算所，后在日本京都大学深造",cut_all = True)#全模式
print("全模式："+", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print("搜索引擎模式："+", ".join(seg_list))

#经过以上分析，精确模式，试图将句子最精确地切开，适合文本分析；