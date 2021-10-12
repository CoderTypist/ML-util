# Transformers turn panda DataFrames into NumpyArrays, which is inconvenient if you want to refer to columns by name
# This transformer will help preserve column names
class PandaKeeper(BaseEstimator, TransformerMixin):

    def __init__(self):
        self.cols = []

    def fit(self, X, y=None):
        
        # must receive a pandas DataFrame
        if type(X) != pd.DataFrame:
            raise Exception('ColumnKeeper: fit(): X must be a pandas DataFrame')
        
        self.cols = X.columns
        return self

    def transform(self, X, y=None):
        
        # make sure the transformer has been fitted
        if 0 == len(self.cols):
            raise Exception('ColumnKeeper: transform(): has not been fitted')

        # convert to panda
        if type(X) != pd.DataFrame:
            X = pd.DataFrame(X)

        # ensure that the correct number of columns are present
        if X.shape[1] != len(self.cols):
            raise Exception(f'ColumnKeeper: transform(): shape mismatch, expected {len(self.cols)} columns, found {X.shape[1]}')
        
        X.columns = self.cols
        return X
