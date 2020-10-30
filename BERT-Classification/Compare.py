import pandas as pd
from sklearn import metrics

path_predict = "predict_SVC.csv"
path_dev = "dev.tsv"


def data_compare():

    dev = pd.read_csv(path_dev, sep='\t',encoding='utf-16')
    predict = pd.read_csv(path_predict, encoding='utf-16')
    n=dev.shape[0]

    modeltest = predict["label"].copy()
    standard = dev["label"].copy()
    list_error = []
    for i in range(len(modeltest)):
        if modeltest[i] != standard[i]:
            list_error.append(i + 1)
    print(list_error)
    print(len(list_error))
    micro = metrics.f1_score(standard, modeltest, average="micro")
    macro = metrics.f1_score(standard,modeltest , average="macro")
    accuracy = metrics.accuracy_score(standard, modeltest)
    matrix=metrics.confusion_matrix(standard, modeltest)
    report=metrics.classification_report(standard, modeltest, target_names=['股称','股价','市值','涨跌','成交','增值'], digits=3)
    print("all",n)
    print("micro",micro)
    print("macro",macro)
    print("accuracy",accuracy)
    print(matrix)
    print(report)




data_compare()
