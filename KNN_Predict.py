import math
import pickle
K = 5

    

def predict(x,doc_vectors,word_bank):
		
	# transform x to vector space
    x_words = word_bank.copy()   
    for word in x.split(" "):
        lower_word = word.lower()
        if lower_word in x_words:
            x_words[lower_word] += 1
        else:
            x_words[lower_word] = 1

    x_vec=[]
    for words in x_words:
        x_vec.append(x_words[words])


    docs_similarity=[]
    similarity=0
    for doc in doc_vectors:	

        x_length = (sum([x ** 2 for x in x_vec ])) ** 0.5
        doc_length= (sum([x ** 2 for x in doc[1] ])) ** 0.5
        similarity=sum([x * y for x, y in zip(doc[1], x_vec)]) / (doc_length * x_length)
        docs_similarity.append((doc[0],similarity))

	#find k nearest neighbors
    sim_dict = dict(sorted(docs_similarity, key=lambda x: x[1], reverse=True)[:K])
    predicted={}
    for k,v in sim_dict.items():
            if v != 0:
                predicted[k]=v
    
    return predicted






