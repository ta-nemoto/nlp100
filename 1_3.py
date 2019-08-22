# -*- coding: utf-8 -*-

#お題の文章
sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

#整形
sentence = sentence.replace(',', '')
sentence = sentence.replace('.', '')

#リストに分割
li_sentence = sentence.split(" ")

#リストの単語の文字数を格納するためのリスト
num_li_sentence = []

#文字数を数えて、リストに格納
for i in li_sentence:
    num_li_sentence.append(len(i))

#プリント
print num_li_sentence

