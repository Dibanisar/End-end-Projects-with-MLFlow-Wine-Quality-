from src.ML_Project.config.configuration import ConfigurationManager
from src.ML_Project.components.data_validation import DataValidation
from src.ML_Project import Logger


STAGE_NAME = "Data IValidation stage"

class DataValidationPipeline:
    def __init__(self):
        pass
    
    def main(self):

        config = ConfigurationManager()
        data_validation_config =config.get_data_validation_config()
        data_validation = DataValidation(config =data_validation_config)
        data_validation.validate_all_columns()
    

if __name__ == "__main__":
    
    try:
        Logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        Logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx========x")
    except Exception as e:
        Logger.exception(e)
        raise e