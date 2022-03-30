import data_preprocess
import pickle



def train(ds):
    #create bank of all the words
    word_bank={}
    for num, row in ds.iterrows():
        for word in row['name'].split(" "):
            lower_word = word.lower()
            if len(lower_word)>2 :
                if lower_word not in word_bank :
                    word_bank[lower_word]=0

    d_vectors = []
    for num, row in ds.iterrows():
        word_doc = word_bank.copy()
        for doc in row['name'].split(" "):
            lower_word = doc.lower()
            if lower_word in word_doc:
                word_doc[lower_word] += 1
            else: 
                word_doc[lower_word] = 1 
        
        word_doc=[word_doc[i] for i in word_doc]
        d_vectors.append(([row['originalTitle'],word_doc]))
		
    return d_vectors,word_bank

training_vectors,word_bank= train(data_preprocess.total_data.head(2000))
print(data_preprocess.total_data.shape)

with open('data/training_pkl', 'wb') as f:
     pickle.dump(training_vectors, f)
with open('data/word_bank_pkl', 'wb') as f:
     pickle.dump(word_bank, f)
