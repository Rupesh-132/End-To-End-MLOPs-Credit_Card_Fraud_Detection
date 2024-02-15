from src.Credit_Card_Fraud_Detection.strategies.data_validation import DataValidationStrategy
from src.Credit_Card_Fraud_Detection.config.configuration import ConfigurationManager
from src.Credit_Card_Fraud_Detection import logger

STRATEGY_NAME = "Data Validation"


class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):

        # Pipelines for the DataValidationStrategy
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidationStrategy(config=data_validation_config)
            data_validation.validate_all_columns()
            data_validation.check_missing_values()
            data_validation.check_data_types()
        except Exception as e:
            logger.exception(e)
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Strategy {STRATEGY_NAME} started <<<<<<<<<<<")
        data_validation_pipeline = DataValidationPipeline()
        data_validation_pipeline.main()
        logger.info(f">>>>>>> Strategy {STRATEGY_NAME} completed <<<<<<<<<<< \n \nx=========x")

    except Exception as e:
        logger.exception(e)
        logger.exception(e)
        raise e



