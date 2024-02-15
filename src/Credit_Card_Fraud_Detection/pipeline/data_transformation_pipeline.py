from src.Credit_Card_Fraud_Detection.strategies.data_transformation import DataTransformationStrategy
from src.Credit_Card_Fraud_Detection.config.configuration import ConfigurationManager
from src.Credit_Card_Fraud_Detection import logger

STRATEGY_NAME = "Data Transformation"


class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):

        # Pipelines for the DataTransformationStrategy
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformationStrategy(config=data_transformation_config)
            data_transformation.train_test_spliting()
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Strategy {STRATEGY_NAME} started <<<<<<<<<<<")
        data_transformation_pipeline = DataTransformationPipeline()
        data_transformation_pipeline.main()
        logger.info(f">>>>>>> Strategy {STRATEGY_NAME} completed <<<<<<<<<<< \n \nx=========x")

    except Exception as e:
        logger.exception(e)
        logger.exception(e)
        raise e



