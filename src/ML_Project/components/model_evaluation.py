
import os
import pandas as pd
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import mlflow
from urllib.parse import urlparse
import mlflow.sklearn
import numpy as np
import joblib
from src.ML_Project.entity.config_entity import ModelEvaluationConfig
from src.ML_Project.utils.common import save_json
from pathlib import Path




class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config = config
        
    def eval_metrics(self,actual,pred):
        rsme = np.sqrt(mean_squared_error(actual,pred))
        mae =mean_absolute_error(actual,pred)
        r2 =r2_score(actual,pred)
        
        return rsme,mae,r2
    def log_into_mlflow(self):
        # Load the test data
        test_data = pd.read_csv(self.config.test_data_path)

        # Load the trained model
        model = joblib.load(self.config.model_path)

        # Split data into features (X) and target (y)
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        # Set the MLflow registry URI
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # Start an MLflow run
        with mlflow.start_run():
            # Make predictions
            predicted_qualities = model.predict(test_x)

            # Evaluate metrics
            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
            
            scores ={"rmse":rmse, "mae":mae, "r2":r2}
            
            save_json(path=Path(self.config.metric_file_name),data =scores)
            
            mlflow.log_params(self.config.all_params)

            # Log metrics (not visible in the screenshot but likely part of the code)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)
            
            
            if tracking_url_type_store != "file":
                #Note to self (Refer this part to the documentation it depends on the use case)!!!!!!!!!!!!!
                
                mlflow.sklearn.log_model(model,"model",registered_model_name= "ElasticnetModel")
                
            else:
                mlflow.sklearn.log_model(model,"model")
                
            