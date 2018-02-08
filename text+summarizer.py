
# coding: utf-8

# In[13]:

from gensim.summarization import summarize
from gensim.summarization import keywords

file_text = open("Downloads/basics/research_paper_tw_sarcasm.txt",encoding="utf8")

text=file_text.read()
summary = summarize(text,word_count=100)
key_words = keywords(text,ratio=0.05)
print(key_words)
print(summary)




# In[ ]:



