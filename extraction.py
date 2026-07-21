import requests
import pandas as pd

class ExtractorAPI: #JSON

    def __init__(self, url):
        self.url = url  
    def getAPI(self):
        self.getter = pd.DataFrame(requests.get(self.url).json())
        return self.getter
    def display(self):
        print(self.getter)

class ExtractorLocal: #CSV

    def __init__(self, fileLocation):
        self.fileLocation = fileLocation
    def getFile(self):
        self.content = pd.read_csv(self.fileLocation)
        return self.content
    def display(self):
        print(self.content)


if __name__ == "__main__":
    print("CSV FILE EXTRACTION TESTING")
    csv1 = ExtractorLocal("warehouse_stock.csv")
    csv1.getFile()
    csv1.display()
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("API URL EXTRACTION TESTING")
    api1 = ExtractorAPI("https://fakestoreapi.com/products")
    api1.getAPI()
    api1.display()
