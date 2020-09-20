import pandas as pd
import numpy as np

#dataset location.
path = '/home/divyu/PycharmProjects/pythonProject/Resources/electro.csv'

#read dataset.
ds = pd.read_csv(path)

#convert panda-series into dictionary of arrays.
dataset = {}
for attr in ds.columns:
    dataset[attr] = list(ds[attr])

#Number of rows, no of yes(s), and no of no(s)
nRows= len(dataset['buys_computer'])
nYes = dataset['buys_computer'].count('yes')
nNo  = nRows - nYes

#Probabloty of yes and no.
pYes = nYes / nRows
pNo  = nNo  / nRows

#List of attributes.
attributes = list(dataset.keys())[:-1]

#Splitting the dataset on the basis of labels, yes/no.
ds_yes = ds.loc[ds['buys_computer'] == 'yes']
ds_no = ds.loc[ds['buys_computer'] == 'no']

#calculating posterior probablities.
print('Posterior Probablities->\n')
pAttrYes, pAttrNo = {}, {}
for attr in attributes:
    print(attr)
    for attrVal in set(dataset[attr]):
        pAttrYes[attrVal] = list(ds_yes[attr]).count(attrVal) / nYes
        pAttrNo [attrVal] = list(ds_no[attr]). count(attrVal) / nNo

        #print the result out. hehe
        printYes = 'P('+attrVal+'| Yes) = '+str(pAttrYes[attrVal])
        printNo  = 'P('+attrVal+'| No ) = '+str(pAttrNo [attrVal])
        print(printYes)
        print (printNo)

    print('~'*40)

def predict(): #Takes necessary input and maps to most probable class.
    age = input("age?...youth/middle_aged/senior -> ")
    income = input("income?...low/medium/high -> ")
    credit_rating = input("credit-rating?...fair/excellent -> ")
    student = input("student?...yes/no -> ")

    #posterior probablity for yes.
    ppYes = pAttrYes[age] * pAttrYes[income] * pAttrYes[credit_rating] * pAttrYes[student]

    #posterior probablity for no.
    ppNo  = pAttrNo[age] * pAttrNo[income] * pAttrNo[credit_rating] * pAttrNo[student]

    #probablity yes.
    _pYes = ppYes * pYes

    #probablity no.
    _pNo  = ppNo * pNo

    if _pYes > _pNo:
        print('\nPredicted label-> Yes')
    else:
        print('\nPredicted Label->  No')

#Run predictor based on prev. calculations.
run_predictor = int(input('\nRun predictor? 1/0 ->'))
while run_predictor:
    predict()
    run_predictor = int(input('\nAgain/Exit? 1/0 ->'))