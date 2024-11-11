import pandas as pd
from sklearn.neighbors import NearestNeighbors

class Recommendation:
    def __init__(self):
        self.df = pd.read_csv("d.csv")
    
    def suggestions(self,price: int) -> list:
        # Filter to only rows with price close to or below input price
        df_below_price = df[df["price"] <= input_price]
        # If dataset has no exact matches, use NearestNeighbors to find closest matches
        if df_below_price.empty:
            nbrs = NearestNeighbors(n_neighbors=3, algorithm='auto').fit(df[['price']])
            distances, indices = nbrs.kneighbors([[input_price]])
            return df.iloc[indices[0]]
        else:
            return df_below_price
            
def test() -> None:
    r = Recommendation()
    print(r.suggestions(190))
    
if __name__ == "__main__":
    test()


