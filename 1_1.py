# -*- coding: utf-8 -*-

#お題の単語
word = u"パタトクカシーー"

#抜き出した文字を格納するための変数
pi_word = ""

#文字を抜き出す
for i in range(len(word)/2):
    pi_word += word[(i*2)+1]

#プリント
print pi_word
