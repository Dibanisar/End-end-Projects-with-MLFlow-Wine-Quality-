from src.ML_Project.config.configuration import ConfigurationManager
from src.ML_Project.components.data_transformation import DataTransformationConfig,DataTranformation
from pathlib import Path
from src.ML_Project import Logger

STAGE_NAME = "Data Transformation Stage"


class DataTransformationPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),"r") as f:
                status =f.read().split(" ")[-1]
                
                
                
            if status =="True":
                
                config = ConfigurationManager()
                data_transformation_config =config.get_data_transformation_config()
                data_transformation = DataTranformation(config = data_transformation_config)
                data_transformation.train_test_splitting()
            
            else:
                raise Exception("Your data schema is not valid")
            
        except Exception as e:
            print(e)
            
if __name__ == "__main__":
    
    try:
        Logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        Logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx========x")
    except Exception as e:
        Logger.exception(e)
        raise e
