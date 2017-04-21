# COMPGI15 2016-2017 Group 22 Project 3
## Home Depot Product Search Relevance
Group 22 ([Zongsheng Wang](https://github.com/zcakzwa), [Fran Silavong](https://github.com/FranSilavong), [Qiuyi He](https://github.com/qh582))
### Step 1. Environment Setup

We used Python 3.6.0 with Anaconda 4.3.16 (64-bit), include:

* scikit-learn
* numpy 
* pandas 
* re
* matplotlib 
* scipy

Besides we also used the following packages:
* xgboost in pointwise model section
* tensorflow in deep learning section
* NLTK  and gensim in data preprocessing part

R-studio and matlab are also used for EDA and plotting mesh graph. 

### Step 2. Raw Data Preparation
The datasets provided by [Kaggle challenge](https://www.kaggle.com/c/home-depot-product-search-relevance/data), include
* train.csv
* test.csv
* product_description.csv
* attribute.csv
* solutions.csv (for local evaluation)

need to be first downloaded and put in data fold. 

### Step 3. Data Preprocessing
First we clean the data before extracting the features, by:
* Running: Data Preprocessing.ipynb

 The processed data will be generated in created processing_text folder. The data preprocessing takes aroung 12-20 hours, depends on the operating environment.

###  Step 4. Feature Extraction and pointwise models
The text similarity features are extracted by sequentially running:

* Distance_Similarity Features.ipynb
* Word2Vec.ipynb

Then we extract brand and matching features by running:

* Feature Extractions and Pointwise Model Training.ipynb

The above file notebook also trains, tests and evaluates several pointwise models using extracted features, include:

* xgboost
* random forest (with bagging)
* adaboost
* neural network (feature based)

The csv of final features will be saved in home directory called df_all.csv.

###  Step 5. pairwise data and LambdaMART/SVMRank
The dataset for pairwsie model is generated and saved in processing_text folder by running:

* Pairwise data convertion.ipynb

Then by running:

* Feature Extractions and Pairwise LambdaMART.ipynb / svmrank4_5.ipynb

We can train and test the pairwise dataset using LambdaMART and evaluate using NDCG. SVMRank will also be used to apply on dataset and evaluate using MAP.

###  Step 6. Grid search and Stacking
The Grid search and stacking is implementd by:

* Grid Search.ipynb 
* stacking.ipynb

Stacking.ipynb will automatically generate solution of predicted relevance on test set for submission.

### Step 7. Deep Learning 

The dataset used for this section is easily created by merging the train.csv with attribute.csv and the test.csv with attribute.csv. The merged dataset requires to have these variables (in this order): id, product_uid, product_title, search_term, relevance, name, value. 

Then, the processed dataset for Deep Learning Model (LSTM based Recurrent Neural Network) is obtained by running the following:
* pipeline.py

To generate the predicted relevance on test set, run the following notebook:
* lstm-rnn-final.ipynb

If you are interested in other models that we have experimented, please refer to the 
* lstm-rnn-final-with-descr.ipynb for the use of product description as training features
* lstm-rnn-final-classification.ipynb	for the classification approach
* lstm-rnn-final-balanced.ipynb for the use of balanced training dataset

