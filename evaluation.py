import numpy as np
import math
import random

def eval_construct(y_pred,y_score,test_group):
    eval_lst=[]
    i = 0
    for group_length in test_group:
        pred = [j-1 for j in list(y_pred[i:i+group_length])]
        real = [j-1 for j in list(y_score[i:i+group_length])]
        pred_seq = [y for x,y in sorted(zip(pred, real),reverse=True)]
        real_seq = sorted(real, reverse= True)
        eval_lst.append([real_seq,pred_seq])
        i=i+group_length
    return eval_lst

def eval_construct_random(y_score,test_group):
    eval_lst=[]
    i = 0
    for group_length in test_group:
        pred = [random.random() for j in range(group_length)]
        real = [j-1 for j in list(y_score[i:i+group_length])]
        pred_seq = [y for x,y in sorted(zip(pred, real),reverse=True)]
        real_seq = sorted(real, reverse= True)
        eval_lst.append([real_seq,pred_seq])
        i=i+group_length
    return eval_lst
    
def NDCG(eval_):
    opt_DCG = 0
    pred_DCG = 0
    for i in range(len(eval_[0])):
        opt_DCG +=  eval_[0][i]/np.log2(i+2)
        pred_DCG +=  eval_[1][i]/np.log2(i+2)
    return pred_DCG,opt_DCG

def mean_NDCG(eval_lst):
    n = len(eval_lst)
    m = n
    pred_sum_NDCG=0
    opt_sum_NDCG=0
    for i in range(n):
        eval_term = eval_lst[i]
        pred_DCG,opt_DCG =  NDCG(eval_term)
        pred_sum_NDCG += pred_DCG 
        opt_sum_NDCG += opt_DCG      
    return pred_sum_NDCG/opt_sum_NDCG