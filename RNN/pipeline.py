
import numpy as np
import os

def corpus(filename='temp/withoneattr_train.csv'):
    import csv
    reader = csv.reader(open(filename))
    data = []
    for row in reader:
        i_d,product_uid,product_title,search_term,relevance,name,value = row
        dic = {'search_term':search_term, 'product_title': product_title,'relevance': relevance, 'attr_1':value}
        data.append(dic)
    del data[0]
    return data

def tokenise(input):
    return input.split(' ')

def pipeline(data,vocab=None,qvocab=None,avocab=None, max_title_len_=None, max_query_len_=None,max_attr_len_=None):
    
    # Product Title Vocab
    exist_vocab = True
    if vocab is None:
        exist_vocab = False
        vocab = {'<PAD>': 0, '<OOV>':1}
    # Search Terms Vocab
    exist_qvocab = True
    if qvocab is None:
        exist_qvocab = False
        qvocab = {'<PAD>': 0, '<OOV>':1}
    # Attr Vocab
    exist_avocab = True
    if avocab is None:
        exist_avocab = False
        avocab = {'<PAD>': 0, '<OOV>':1}  
    
    
    ## Placeholder ## 
    # Product Title
    max_title_len = -1
    data_title = []
    # Search Term
    max_query_len = -1
    data_query = []
    # Attr Term
    max_attr_len = -1
    data_attr = []
    
    # Relevance
    data_relevance = []
    
    ## Processing ## 
    for instance in data:
        # Product Title Processing
        title = instance['product_title']
        t_tokenised = tokenise(title)
        each_title = []
        for token in t_tokenised:
            if not exist_vocab and token not in vocab:
                vocab[token] = len(vocab)
            if token not in vocab:
                token_id = vocab['<OOV>']
            else:
                token_id = vocab[token]
            each_title.append(token_id)
        # Product Title Length
        if len(each_title) > max_title_len:
            max_title_len = len(each_title)
        data_title.append(each_title)
            
        # Search Term Processing
        query = instance['search_term']
        q_tokenised = tokenise(query)
        each_query = []
        for qtoken in q_tokenised:
            if not exist_qvocab and qtoken not in qvocab:
                qvocab[qtoken] = len(qvocab)
            if qtoken not in qvocab:
                qtoken_id = qvocab['<OOV>']
            else:
                qtoken_id = qvocab[qtoken]
            each_query.append(qtoken_id) 
        # Search Terms Length
        if len(each_query) > max_query_len:
            max_query_len = len(each_query)
        data_query.append(each_query)
        

        # Attr Processing
        attr = instance['attr_1']
        a_tokenised = tokenise(attr)
        each_attr = []
        for atoken in a_tokenised:
            if not exist_avocab and atoken not in avocab:
                avocab[atoken] = len(avocab)
            if atoken not in avocab:
                atoken_id = avocab['<OOV>']
            else:
                atoken_id = avocab[atoken]
            each_attr.append(atoken_id) 
        # Search Terms Length
        if len(each_attr) > max_attr_len:
            max_attr_len = len(each_attr)
        data_attr.append(each_attr)
            
        # Relevance 
        data_relevance.append(instance['relevance'])

    if max_title_len_ is not None:
        max_title_len = max_title_len_
    out_title = np.full([len(data_title), max_title_len], vocab['<PAD>'], dtype=np.int32)
    
    for index, item in enumerate(data_title):
        if len(item) <= out_title.shape[1]:
            out_title[index, 0:len(item)] = item
    
    if max_query_len_ is not None:
        max_query_len = max_query_len_
    out_query = np.full([len(data_query), max_query_len], qvocab['<PAD>'], dtype=np.int32)
    
    for index, q in enumerate(data_query):
        out_query[index, 0:len(q)] = q
        
    if max_attr_len_ is not None:
        max_attr_len = max_attr_len_
    out_attr = np.full([len(data_attr), max_attr_len], avocab['<PAD>'], dtype=np.int32)
    
    for index, item in enumerate(data_attr):
        if len(item) <= out_title.shape[1]:
            out_attr[index, 0:len(item)] = item
        
    out_relevance = np.array(data_relevance, dtype=np.float64)
    
    return out_title, out_query, out_relevance, out_attr , vocab, qvocab, avocab
