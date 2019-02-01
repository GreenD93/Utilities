from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn import linear_model
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split

class feature_importance:
    def __init__(self,data,label):
        self.x = data.drop([label],axis=1)
        self.y = data[[label]]
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.33,
                                                                                random_state=42)

    def random_forest(self):
        clf = RandomForestClassifier(max_depth=2, random_state=0)
        clf.fit(self.x_train, self.y_train)
        print("RF :", accuracy_score(clf.predict(self.x_test), self.y_test))
        print(classification_report(self.y_test, clf.predict(self.x_test)))
        scores = cross_val_score(clf, self.x, self.y, cv=5)
        print(scores)

    def logistic_regression(self):
        print('logistic_regression')
        logreg = linear_model.LogisticRegression(C=2.0, random_state=42, solver='sag', multi_class='multinomial',
                                                 warm_start=True)
        logreg.fit(self.x_train, self.y_train)
        print("LR :", accuracy_score(logreg.predict(self.x_test), self.y_test))
        print(classification_report(self.y_test, logreg.predict(self.x_test)))
        scores = cross_val_score(logreg, self.x, self.y, cv=5)
        print(scores)

    def svm(self):
        result = LinearSVC(random_state=0).fit(self.x_train, self.y_train)
        print("SVM :", accuracy_score(result.predict(self.x_test), self.y_test))
        print(classification_report(self.y_test, result.predict(self.x_test)))
        scores = cross_val_score(result, self.x, self.y, cv=5)
        print(scores)