from nltk.tokenize import sent_tokenize, word_tokenize

#text = 'This is a simple text designed for me to check whether I am able to use a toolkit for natural processing language or not. I will see the results and analyse them shortly after that.'
text = 'Isso é um texto simples desenhado por mim para checar se eu sou capaz de usar a caixa de ferramentas de processamento de linguagem natural. Eu verei os seus resultados e os analisarei após isso.'

a = sent_tokenize(text)
b = word_tokenize(text)
print(a[1])
print('======================================================')
print('======================================================')
print(b)