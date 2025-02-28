from src.ML_Project.config.configuration import ConfigurationManager
from src.ML_Project.components.model_trainer import ModelTrainer
from src.ML_Project import Logger

STAGE_NAME ="Model Trainer Stage"

class ModelTrainingPipeline:
    def __init__(self):
        
        pass
    
    
    def main(self):
        
        config =ConfigurationManager()
        model_trainer_config =config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config= model_trainer_config)
        model_trainer_config.train()
        
        
if __name__ == "__main__":
    
    try:
        Logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        Logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx========x")
    except Exception as e:
        Logger.exception(e)
        raise e


    