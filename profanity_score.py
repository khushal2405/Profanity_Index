#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[3]:


#Assumption: assuming that each tweet is stored in each row of any column in a csv file.
#Assumption: let's assume that 10th column is for tweets.
#
#
#
input_ = "Tweets.csv"
def input_data(input_):
    #taking csv file name "Tweets.csv" as input
    df = pd.read_csv(input_)

# now iterating over each row to get the tweet as input and then we can split scentences ending with "." and store them in a list.
    sentences = []
    for i in range(len(df.index)):
        p = df.iloc[i,10]
    #here we need one more loop because split method returns an list and we don't need a lists appended inside an list.
    #SO, I used a loop to iterate over the list given by split method in order to get one list with all the scentences. 
        for x in p.split("."):
            if x == '':
                continue
            else:
                sentences.append(x)
    return sentences
            #now, why this if-else condition. If we take any sentence and break it using "." then after last fullstop it also takes the white space('') as a entry.
            # So, to eliminate this I skipped the append when the entry is ''
    


# In[23]:


#now lets even further break each sentence in words and conpare those to racial slurs one word by on word
#lets first define our racial slurs list or array.for now it's empty but if you give me some dataset and also some slurs then this model will work.
def slur_processing(sentences):
    racial_slurs = []
    slur_score = 0
    slur_score_list = []
#slur score defines number of slurs that happen to find in a sentnces that can help us later find the profanity score.

    for i in sentences:
        for w in i.split(" "):
            for s in racial_slurs:
                if w == s:
                    slur_score = slur_score + 1
        slur_score_list.append(slur_score)
    return slur_score_list
        


# In[24]:


# so, now we got our slur scores in a list that we can use to convert into an profanity score that happends to lie between zero and 10.
def prof_index(slur_score_list):
    
    profanity_index = []
    for num in slur_score_list:
        index = (max(slur_score_list) - num)/max(slur_score_list)
        profanity_index.append(index*10)
    return profanity_index()


# In[ ]:




