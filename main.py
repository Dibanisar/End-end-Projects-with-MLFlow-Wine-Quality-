from src.ML_Project import Logger
from src.ML_Project.pipeline.Stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.ML_Project.pipeline.Stage_02_data_validation import DataValidationPipeline
from src.ML_Project.pipeline.Stage_03_data_transformation import DataTransformationPipeline
from src.ML_Project.pipeline.Stage_04_model_trainer import ModelTrainingPipeline  
from src.ML_Project.pipeline.Stage_05_model_evaluation import ModelEvaluationPipeline
import dagshub


STAGE_NAME = "Data Ingestion stage"

try:
    Logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    Logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx========x")
except Exception as e:
    Logger.exception(e)
    raise e



STAGE_NAME = "Data IValidation stage"

try:
    Logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationPipeline()
    obj.main()
    Logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx========x")
except Exception as e:
    Logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation Stage"

try:
    Logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationPipeline()
    obj.main()
    Logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx========x")
except Exception as e:
    Logger.exception(e)
    raise e


STAGE_NAME ="Model Trainer Stage"

try:
    Logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    Logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx========x")
except Exception as e:
    Logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"
dagshub.init(repo_owner="Dibanisaf", repo_name="End-end-Projects-with-MLFlow-Wine-Quality-", mlflow=True)

try:
    Logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    Logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx========x")
except Exception as e:
    Logger.exception(e)
    raise e