import pandas as pd
import os
from src.Credit_Card_Fraud_Detection import logger
from sklearn.ensemble import RandomForestClassifier
import joblib
from src.Credit_Card_Fraud_Detection.entity.config_entity import ModelTrainerConfig


class ModelTrainerStrategy:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        rfc = RandomForestClassifier(n_estimators=self.config.n_estimators, criterion=self.config.criterion,
                                     bootstrap=self.config.bootstrap, random_state=42, verbose=True)
        rfc.fit(train_x, train_y)

        joblib.dump(rfc, os.path.join(self.config.root_dir, self.config.model_name))

