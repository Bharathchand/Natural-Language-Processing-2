import nltk
    
f=open('constitution.txt','rU')

raw = f.read()
raw = raw.upper()
raw = raw.decode('utf-8')
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)

text.dispersion_plot(["AGRICULTURE","EDUCATION","ENVIRONMENT","ENERGY","SCIENCE","TECHNOLOGY","LAW","ECONOMY"])
