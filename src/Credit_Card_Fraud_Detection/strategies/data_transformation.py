import os
from src.Credit_Card_Fraud_Detection import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.Credit_Card_Fraud_Detection.entity.config_entity import DataTransformationConfig


class DataTransformationStrategy:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # All the EDA steps can be added here

    # I am only adding train_test_spliting because this data is already cleaned up

    def train_test_spliting(self):
        """
        Splitting the data into train, test --> 80% training 20% testing
        :return:
        """
        data = pd.read_csv(self.config.data_path)
        train, test = train_test_split(data, test_size=0.2, random_state=30)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
