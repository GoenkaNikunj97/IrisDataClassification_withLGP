import pandas as pd
from sklearn.model_selection import train_test_split

class Initialize:
    def __init__(self, fileName):
        print("Creating Population")
        self.fileName = fileName
        self.getData()

    def getData(self):
        #reading Data
        df = pd.read_csv(self.fileName, header=None)

        #splitting input and lable
        X = df[df.columns[:-1]]
        Y = df[df.columns[-1]]

        #one hot encode lable
        Y = pd.get_dummies(Y)

        #test and train split
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(X, Y, test_size=0.20, random_state=1, stratify=Y)

        self.X_train = self.X_train.values.tolist()
        self.X_test = self.X_test.values.tolist()
        self.Y_train = self.Y_train.values.tolist()
        self.Y_test = self.Y_test.values.tolist()