import numpy as np

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])