2#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 16:19:09 2018

@author: virajdeshwal
"""

import sklearn
import pandas as pd
dos=[]
r2l=[]
u2r=[]
probe=[]
'''
label the headers of the columns'''

col_names = ["duration","protocol_type","service","flag","src_bytes",
    "dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins",
    "logged_in","num_compromised","root_shell","su_attempted","num_root",
    "num_file_creations","num_shells","num_access_files","num_outbound_cmds",
    "is_host_login","is_guest_login","count","srv_count","serror_rate",
    "srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
    "diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate","label"]




''' Categorising the attack  labels in the attack in the proper attack categories''' 
'''
dos = ["back.", "land.", "neptune.", "pod.", "smurf.", "teardrop."]
r2l = ["ftp_write.", "guess_passwd.", "imap.", "multihop." ,"phf.", "spy.", "warezclient.", "warezmaster."]
u2r = ["buffer_overflow.", "loadmodule.", "perl.", "rootkit."]
probe = ["ipsweep.", "nmap.", "portsweep.", "satan."]

Import the dataset'''

#file = pd.read_csv('Dataset', header =None, names = col_names)
test_file= pd.read_csv('test/labelled_10', header =None, names = col_names)
X = test_file.iloc[:,:-1].values
y=test_file.iloc[:,41].values
print(test_file.shape)
print(X.shape)


#train_file = pd.read_csv('unlabelled_10', names = col_names)
'''

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

label_X = LabelEncoder()
X[:,3]= label_X.fit_transform(X[:,3])


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)
'''
'''Select the features we needed for the experiments'''
'''num_features = [
    "duration","src_bytes",
    "dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins",
    "logged_in","num_compromised","root_shell","su_attempted","num_root",
    "num_file_creations","num_shells","num_access_files","num_outbound_cmds",
    "is_host_login","is_guest_login","count","srv_count","serror_rate",
    "srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
    "diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate"]



features = file[num_features].astype(float)


#Let's reduce the output to attack and normal only.


labels = file['label'].copy()
labels[labels!='attack.'] = 'normal.'
if 'attack.' in labels:
    attacks.append(labels)

print(len(attacks))

print('Done.')

'''