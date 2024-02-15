import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, matthews_corrcoef
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.Credit_Card_Fraud_Detection.utils.common import save_json
from src.Credit_Card_Fraud_Detection.entity.config_entity import ModelEvaluationConfig
from pathlib import Path


class ModelEvaluationStrategy:
    """
    Class to handle the model evaluation strategies
    """
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        """
        evaluates the model and calculates metrics
        :param actual: y_test
        :param pred: y_pred
        :return: accuracy, precision, recall, f1, matthews_corr
        """
        # classification_report = classification_report(actual,pred)
        accuracy = accuracy_score(actual, pred)
        precision = precision_score(actual, pred)
        recall = recall_score(actual, pred)
        f1 = f1_score(actual, pred)
        matthews_corr = matthews_corrcoef(actual, pred)

        return accuracy, precision, recall, f1, matthews_corr

    def log_into_mlflow(self):
        """
        - handles all the events related to the mlflow.
        - stores all the metrics
        - saves model configuration and version
        - stores model parameters as history

        :return: None
        """
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            predicted_qualities = model.predict(test_x)

            (accuracy, precision, recall, f1, matthews_corr) = self.eval_metrics(test_y, predicted_qualities)

            # Saving metrics as local
            scores = {"accuracy": accuracy, "precision": precision, "recall_score": recall, "f1_score": f1,
                      "matthews_corr": matthews_corr}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("accuracy", accuracy)
            mlflow.log_metric("precision", precision)
            mlflow.log_metric("recall_score", recall)
            mlflow.log_metric("f1_score", f1)
            mlflow.log_metric("matthews_corr", matthews_corr)

            # Model registry does not work with file store
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="RandomForestClassifier")
            else:
                mlflow.sklearn.log_model(model, "model")





