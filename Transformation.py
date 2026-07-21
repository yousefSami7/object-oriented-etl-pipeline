import pandas as pd

class Transformer:
    def __init__(self,df):
        self.df = df 

    def clean(self):
        self.df['stock_qty'] =  self.df['stock_qty'].fillna(0)
        self.df = self.df[self.df["warehouse_loc"].notna() & (self.df["warehouse_loc"] != 0) & (self.df["warehouse_loc"] != '')]
        return self.df
    def merge_datasets(self,df):
      merger =   self.df.merge(df, on='id', how="outer")
      return merger
    
if __name__ == '__main__':
    df = pd.read_csv('warehouse_stock.csv')
    df2 = pd.DataFrame({
        'name':['x','y','z'],
        'id': [1,2,3]
    })
    Tr = Transformer(df)
    Tr.clean()
    merge = Tr.merge_datasets(df2)
    print(merge)
