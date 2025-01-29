from src.ML_Project.config.configuration import ConfigurationManager
from src.ML_Project.components.model_evaluation import ModelEvaluationConfig,ModelEvaluation
from pathlib import Path
from src.ML_Project import Logger


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config =ConfigurationManager()
        model_evaluation_config =config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config= model_evaluation_config)
        model_evaluation_config.log_into_mlflow()
            
if __name__ == "__main__":
    
    try:
        Logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        Logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx========x")
    except Exception as e:
        Logger.exception(e)
        raise e
                

