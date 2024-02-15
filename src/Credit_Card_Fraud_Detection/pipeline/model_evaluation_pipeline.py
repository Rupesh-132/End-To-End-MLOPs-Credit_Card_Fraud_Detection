
from src.Credit_Card_Fraud_Detection.config.configuration import ConfigurationManager
from src.Credit_Card_Fraud_Detection import logger
from src.Credit_Card_Fraud_Detection.strategies.model_evaluation import ModelEvaluationStrategy

STRATEGY_NAME = "Model Evaluation"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):

        # Pipelines for the DataIngestionStrategy
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluationStrategy(config=model_evaluation_config)
            model_evaluation_config.log_into_mlflow()

        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Strategy {STRATEGY_NAME} started <<<<<<<<<<<")
        model_evaluation_pipeline = ModelEvaluationPipeline()
        model_evaluation_pipeline.main()
        logger.info(f">>>>>>> Strategy {STRATEGY_NAME} completed <<<<<<<<<<< \n \nx=========x")

    except Exception as e:
        logger.exception(e)
        raise e



