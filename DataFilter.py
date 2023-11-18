import pandas as pd

class DataFilter:
    def __init__(self, exResultDataSet: pd.DataFrame) -> None:
        self.ExResultDataSet = exResultDataSet
        
    def Filtering(self) -> None:    
        self.ExResultDataSet = self.ExResultDataSet[self.ExResultDataSet['Celsius'] < 30]
        self.ExResultDataSet = self.ExResultDataSet[20 <= self.ExResultDataSet['Celsius']]
        
        self.ExResultDataSet['Set Number'] = range(len(self.ExResultDataSet))
        
        return self.ExResultDataSet
        
            
    
    