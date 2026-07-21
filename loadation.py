import pandas as pd
class Loader:
    def __init__(self):
        pass
    def load(self,df):
        df.to_csv("final_inventory_report.csv", index=False)
    
if __name__ == "__main__":
    df = pd.DataFrame([[1,2,3,4],[5,6,7,8]])
    loader = Loader()
    loader.load(df)