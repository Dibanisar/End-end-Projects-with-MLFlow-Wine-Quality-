import os
from src.ML_Project import Logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.ML_Project.entity.config_entity import DataTransformationConfig


class DataTranformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config
        
        
    def train_test_splitting(self):
        data =pd.read_csv(self.config.data_path)
        
        #splitting the data into training and test sets.
        train, test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)
        
        Logger.info("Splitted data into Training and Testing")
        Logger.info(train.shape)
        Logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)