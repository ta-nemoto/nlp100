# -*- coding: utf-8 -*-

#お題の文章
sentence = "I am an NLPer"

#文章をリストに分割
li_sentence = sentence.split(" ")

#単語bi-gramを格納するためのリスト
li_bi_word = []

#単語bi-gram作成
for i in range(len(li_sentence)-1):
    bi_word = li_sentence[i] + " " + li_sentence[i+1]
    li_bi_word.append(bi_word)

#プリント
print li_bi_word


#次は文字bi-gram、文章のスペースを消して整形
ds_sentence = sentence.replace(" ", "")

#文字bi-gramを格納するためのリスト
li_bi_char = []

#文字bi-gram作成
for i in range(len(ds_sentence)-1):
    bi_char = ds_sentence[i:i+2]
    li_bi_char.append(bi_char)

#プリント
print li_bi_char
    
