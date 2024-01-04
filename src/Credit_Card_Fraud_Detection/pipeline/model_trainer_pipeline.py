from Credit_Card_Fraud_Detection.strategies.model_trainer import ModelTrainerStrategy
from Credit_Card_Fraud_Detection.config.configuration import ConfigurationManager
from Credit_Card_Fraud_Detection import logger

STRATEGY_NAME = "Model Trainer"


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):

        # Pipelines for the DataIngestionStrategy
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainerStrategy(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Strategy {STRATEGY_NAME} started <<<<<<<<<<<")
        data_ingestion_pipeline = ModelTrainerPipeline()
        data_ingestion_pipeline.main()
        logger.info(f">>>>>>> Strategy {STRATEGY_NAME} completed <<<<<<<<<<< \n \nx=========x")

    except Exception as e:
        logger.exception(e)
        raise e



