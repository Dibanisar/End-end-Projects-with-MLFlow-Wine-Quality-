from src.ML_Project import Logger
from src.ML_Project.pipeline.Stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    Logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    Logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx========x")
except Exception as e:
    Logger.exception(e)
    raise e

