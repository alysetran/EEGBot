#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from glob import glob
import os
from sklearn.preprocessing import StandardScaler

########use this to find where the .csv files have been stored########

path = 'path/to/desktop'
for root, dirs, files, in os.walk(path):
    for file in files:
        if file.endswith('.csv'):
            print(file)
            
#next please copy and paste the directory that the .csv files are in 
os.chdir('path/to/files/')
    
#############function to read data###########

def prepare_data_train(fname):
    """ read and prepare training data """
    # Read data
    data = pd.read_csv(fname)
    # events file
    events_fname = fname.replace('_data','_events')
    # read event file
    labels= pd.read_csv(events_fname)
    clean=data.drop(['id' ], axis=1)#remove id
    labels=labels.drop(['id' ], axis=1)#remove id
    return  clean,labels

########## new addition to baseline from Simple Low Freq ###########
def butterworth_filter(X,t,k,l):
    if t==0:
        freq=[k, l]
        b,a = butter(5,np.array(freq)/250.0,btype='bandpass')
        X = lfilter(b,a,X)
    elif t==1:
        b,a = butter(5,k/250.0,btype='lowpass')
        X = lfilter(b,a,X)
    elif t==2:
        b,a = butter(5,l/250.0,btype='highpass')
        X = lfilter(b,a,X)      
    return X

def prepare_data_test(fname):
    """ read and prepare test data """
    # Read data
    data = pd.read_csv(fname)
    return data

scaler= StandardScaler()

def data_preprocess_train(X):
    X_prep=scaler.fit_transform(X)
    return X_prep
def data_preprocess_test(X):
    X_prep=scaler.transform(X)
    return X_prep

subsample=100 # training subsample.if you want to downsample the training data

#######columns name for labels#############

cols = ['HandStart','FirstDigitTouch',
        'BothStartLoadPhase','LiftOff',
        'Replace','BothReleased']

#######number of subjects###############
subjects = range(1,13)
ids_tot = []
pred_tot = []

###loop on subjects and 8 series for train data + 2 series for test data
for subject in subjects:
    y_raw= []
    raw = []
    
################ READ DATA ################################################
    
    #path = r"C:\Users\alysetran\Downloads\train\subj%d_series*_data.csv"
    fnames =  glob('/Users/alysetran/train/subj%d_series*_data.csv' % (subject))   
    for fname in fnames:
        data,labels=prepare_data_train(fname)
        raw.append(data)
        y_raw.append(labels)

    X = pd.concat(raw)
    y = pd.concat(y_raw)
    #transform in numpy array
    #transform train data in numpy array
    X_train =np.asarray(X.astype(float))
    y = np.asarray(y.astype(float))


################ Read test data #####################################
    
    fnames =  glob('/Users/alysetran/test/subj%d_series*_data.csv' % (subject))   
    test = []
    idx=[]
    for fname in fnames:
        data=prepare_data_test(fname)
        test.append(data)
        idx.append(np.array(data['id']))
    X_test= pd.concat(test)
    ids=np.concatenate(idx)
    ids_tot.append(ids)
    X_test=X_test.drop(['id' ], axis=1)#remove id
    #transform test data in numpy array
    X_test =np.asarray(X_test.astype(float))


################ Train classifiers ########################################
    
    pred = np.empty((X_test.shape[0],6))
    X_train=data_preprocess_train(X_train)
    X_test=data_preprocess_test(X_test)
    for i in range(6):
        y_train= y[:,i]
        print('Train subject %d, class %s' % (subject, cols[i]))
        LogisticRegression().fit(X_train[::subsample,:],y_train[::subsample])
        pred[:,i] = lr.predict_proba(X_test)[:,1]

    pred_tot.append(pred)

# submission file
submission_file = 'grasp-sub-simple.csv'
# create pandas object for sbmission
submission = pd.DataFrame(index=np.concatenate(ids_tot),
                          columns=cols,
                          data=np.concatenate(pred_tot))

# write file
submission.to_csv(submission_file,index_label='id',float_format='%.3f')


# In[ ]:




