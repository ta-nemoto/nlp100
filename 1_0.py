# -*- coding: utf-8 -*-

#お題の単語
word = "stressed"

#順番を逆にした単語を格納するための変数
re_word = ""

#逆に並び替え
for i in range(len(word)):
    re_word += word[len(word)-1-i]

#プリント
print re_word
