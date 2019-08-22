# -*- coding: utf-8 -*-

#お題の文章
sentence1 = "paraparaparadise"
sentence2 = "paragraph"

#文字bi-gramを格納するためのリスト
li_bi_char1 = []
li_bi_char2 = []


#文字bi-gram作成
for i in range(len(sentence1)-1):
    bi_char = sentence1[i:i+2]
    li_bi_char1.append(bi_char)

for i in range(len(sentence2)-1):
    bi_char = sentence2[i:i+2]
    li_bi_char2.append(bi_char)

#それぞれの文字bi-gramをＸとＹとしてプリント
print "X", li_bi_char1
print "Y", li_bi_char2

#それぞれの文字bi-gramをset型に変換
set1 = set(li_bi_char1)
set2 = set(li_bi_char2)

#set型を使って積集合を出す
union = list(set1 | set2)

#set型を使って積集合を出す
intersection = list(set1 & set2)

#set型を使って差集合を出す
set_difference = list(set1 - set2)


#プリント
print "X|Y", union
print "X&Y", intersection
print "X-Y", set_difference

#それぞれの文字bi-gramに文字列「se」が入っているかの判定&プリント
print "se" in li_bi_char1
print "se" in li_bi_char2



