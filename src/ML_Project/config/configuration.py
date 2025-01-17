from src.ML_Project.constants import *
from src.ML_Project.utils.common import read_yaml, create_directories
from src.ML_Project.entity.config_entity import (DataIngestionConfig,
                                                 DataValidationConfig) 

class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH
                     ,params_filepath = PARAMS_FILE_PATH
                         ,schema_filepath = SCHEMA_FILE_PATH ):
        
        self.config = read_yaml(config_filepath)
        self.params =read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        
        create_directories([self.config.artifacts_root]) #creating the artifact_root path
        


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion #this is reading the yaml file which points to config file and open the data_ingestion with conffig box
        
        create_directories([config.root_dir]) #using this function from common ro create dictionary accessed from the #self.config.data_ingestion above
        
        
        data_ingestion_config = DataIngestionConfig(
                root_dir = config.root_dir,
                source_URL = config.source_URL,
                local_data_file = config.local_data_file,
                unzip_dir = config.unzip_dir
        )#loading the container
        
        return data_ingestion_config
    
    
        
    def get_data_validation_config(self) -> DataValidationConfig:
        
        config = self.config.data_validation #this is reading the yaml file which points to config file and open the data_ingestion with conffig box
        schema = self.schema.COLUMNS
        
        create_directories([config.root_dir]) #using this function from common ro create dictionary accessed from the #self.config.data_ingestion above
        
        
        data_validation_config = DataValidationConfig(
                unzip_data_dir = config.unzip_data_dir,
                STATUS_FILE= config.STATUS_FILE,
                root_dir= config.root_dir,
                all_schema = schema
        )#loading the container
        
        return data_validation_config 




