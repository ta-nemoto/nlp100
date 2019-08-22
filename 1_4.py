# -*- coding: utf-8 -*-

#お題の文章
sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

#整形
sentence = sentence.replace(',', '')
sentence = sentence.replace('.', '')

#リストに分割
li_sentence = sentence.split(" ")

#各リストの頭2文字を抜きだして、リストを更新
for i in range(len(li_sentence)):
    li_sentence[i] = li_sentence[i][0:2]

#頭1文字でいい単語の、リスト座標
li_on_char = [1, 5, 6, 7, 8, 9, 15, 16, 19]

#頭1文字でいい単語は、1文字にリストを更新
for i in li_on_char:
    li_sentence[i-1] = li_sentence[i-1][0:1]

#リストの文字と順番を対応付けた辞書を格納する変数
dic_sentence = {}

#辞書を作成
for i in range(len(li_sentence)):
    dic_sentence[li_sentence[i]] = i+1

#プリント
print dic_sentence
