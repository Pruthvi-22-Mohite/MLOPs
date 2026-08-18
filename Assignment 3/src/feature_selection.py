from sklearn.feature_selection import SelectKBest, f_classif

def feature_selector(k=10):
    selector = SelectKBest(score_func=f_classif, k=k)
    return selector