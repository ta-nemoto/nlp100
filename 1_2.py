# -*- coding: utf-8 -*-

#お題の単語
word1 = u"パトカー"
word2 = u"タクシー"

#2つの単語をまとめたものを入れる変数
jo_word = ""

#2つの単語をまとめる
for i in range(len(word1)):
    jo_word += word1[i]+word2[i]

#プリント
print jo_word
