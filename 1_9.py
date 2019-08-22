# -*- coding: utf-8 -*-
import random

#お題の文章
sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

#スペースで分割して単語のリストに
li_sentence = sentence.split(" ")

#暗号化文章格納用
code = ""

for i in range(len(li_sentence)):


#単語リストをくっつけて文章に
code = li_sentence.join(" ")

#プリント
print code

