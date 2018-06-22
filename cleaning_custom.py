# transformer to select df columns
from sklearn.base import BaseEstimator, TransformerMixin

# Create a class to select numerical or categorical columns
# since Scikit-Learn doesn't handle DataFrames yet
class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names].values


import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin

class CustomLabelBinarizer(BaseEstimator, TransformerMixin):
    """Perform one-hot encoding to categorical features."""
    def __init__(self, cat_features):
        self.cat_features = cat_features

    def fit(self, X_cat, y=None):
        return self

    def transform(self, X_cat):
        X_cat_df = pd.DataFrame(X_cat, columns=self.cat_features)
        X_onehot_df = pd.get_dummies(X_cat_df, columns=self.cat_features)
        return X_onehot_df.values
