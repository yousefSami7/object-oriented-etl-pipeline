from extraction import ExtractorAPI
from extraction import ExtractorLocal
from Transformation import Transformer
from loadation import Loader
if __name__ == "__main__":
    API_extractor = ExtractorAPI('https://fakestoreapi.com/products')
    storeDF = API_extractor.getAPI()
    local_extractor = ExtractorLocal('warehouse_stock.csv')
    warehouseDF = local_extractor.getFile()
    Tr = Transformer(warehouseDF)
    Tr.clean()
    merged_DF = Tr.merge_datasets(storeDF)
    loader = Loader()
    try:
        loader.load(merged_DF)
    except Exception as e:
        print(f"Data loading failed: {e}")