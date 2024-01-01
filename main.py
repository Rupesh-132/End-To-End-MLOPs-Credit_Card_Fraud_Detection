from Credit_Card_Fraud_Detection import logger
from Credit_Card_Fraud_Detection.pipeline.data_ingestion_pipeline import DataIngestionPipeline

STRATEGY_NAME = "Data Ingestion"

try:
    logger.info(f">>>>>>> Strategy {STRATEGY_NAME} started <<<<<<<<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>>> Strategy {STRATEGY_NAME} completed <<<<<<<<<<< \n \nx=========x")

except Exception as e:
    logger.exception(e)
    raise e