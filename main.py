from Credit_Card_Fraud_Detection import logger
from Credit_Card_Fraud_Detection.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from Credit_Card_Fraud_Detection.pipeline.data_validation_pipeline import DataValidationPipeline
from Credit_Card_Fraud_Detection.pipeline.data_transformation_pipeline import DataTransformationPipeline

STRATEGY_NAME = "Data Ingestion"

try:
    logger.info(f">>>>>>> Strategy {STRATEGY_NAME} started <<<<<<<<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>>> Strategy {STRATEGY_NAME} completed <<<<<<<<<<< \n \nx=========x")

except Exception as e:
    logger.exception(e)
    raise e


STRATEGY_NAME = "Data Validation"

try:
    logger.info(f">>>>>>> Strategy {STRATEGY_NAME} started <<<<<<<<<<<")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.main()
    logger.info(f">>>>>>> Strategy {STRATEGY_NAME} completed <<<<<<<<<<< \n \nx=========x")

except Exception as e:
    logger.exception(e)
    raise e


STRATEGY_NAME = "Data Transformation"

try:
    logger.info(f">>>>>>> Strategy {STRATEGY_NAME} started <<<<<<<<<<<")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.main()
    logger.info(f">>>>>>> Strategy {STRATEGY_NAME} completed <<<<<<<<<<< \n \nx=========x")

except Exception as e:
    logger.exception(e)
    raise e


