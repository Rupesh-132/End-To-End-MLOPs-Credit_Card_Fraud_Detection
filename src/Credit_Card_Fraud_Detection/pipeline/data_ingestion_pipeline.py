from src.Credit_Card_Fraud_Detection.strategies.data_ingestion import DataIngestionStrategy
from src.Credit_Card_Fraud_Detection.config.configuration import ConfigurationManager
from src.Credit_Card_Fraud_Detection import logger

STRATEGY_NAME = "Data Ingestion"


class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):

        # Pipelines for the DataIngestionStrategy
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestionStrategy(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Strategy {STRATEGY_NAME} started <<<<<<<<<<<")
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.main()
        logger.info(f">>>>>>> Strategy {STRATEGY_NAME} completed <<<<<<<<<<< \n \nx=========x")

    except Exception as e:
        logger.exception(e)
        raise e



