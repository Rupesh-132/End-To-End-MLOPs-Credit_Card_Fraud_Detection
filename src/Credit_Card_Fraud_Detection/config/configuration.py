from Credit_Card_Fraud_Detection.constants import *
from Credit_Card_Fraud_Detection.utils.common import read_yaml,create_directories
from Credit_Card_Fraud_Detection.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(
            self,
            config_file_path=CONFIG_FILE_PATH,
            params_file_path=PARAMS_FILE_PATH,
            schema_file_path=SCHEMA_FILE_PATH):

        self.config = read_yaml(config_file_path),
        self.params = read_yaml(params_file_path),
        self.schema = read_yaml(schema_file_path)

        # print(self.config)
        # print(self.config[0].artifacts_root)
        create_directories([self.config[0].artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config[0].data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

