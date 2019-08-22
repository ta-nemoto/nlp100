# -*- coding: utf-8 -*-

#お題の文章
sentence = "I am an NLPer"

#暗号化文章格納用
code = ""

#小文字をasciiコードに変換
for i in sentence:
    if 97 <= ord(i) & ord(i) <= 122:
        code += str(ord(i))
    else:
        code += i

#プリント
print code
        

