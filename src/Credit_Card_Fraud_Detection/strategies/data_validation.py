import pandas as pd
from src.Credit_Card_Fraud_Detection import logger
from src.Credit_Card_Fraud_Detection.entity.config_entity import DataValidationConfig


class DataValidationStrategy:
    """
    class for data validation strategy
    """

    def __init__(self, config: DataValidationConfig):
        self.config = config
        self.validation_report = {}
        self.data = pd.read_csv(self.config.unzip_data_dir)

    def validate_all_columns(self) -> bool:
        """
        validates all the columns of the data with the schema defined
        :return: validation status: True if all columns matches the schema of data
        """
        try:

            all_cols = list(self.data.columns)
            logger.info(all_cols)

            all_schema = self.config.all_schema.keys()
            logger.info(all_schema)

            all_schema_set = set(all_schema)
            column_validation_status = True  # Set by default as True

            for col in all_cols:
                if col not in all_schema_set:
                    validation_status = False
                    break  # No need to continue checking if validation fails

            self.validation_report["column_validation_status"] = column_validation_status

            # # Write the final validation status
            # with open(self.config.STATUS_FILE, 'w') as f:
            #     f.write(f"Column Validation status: {column_validation_status}")

            return column_validation_status

        except Exception as e:
            raise e

    def check_missing_values(self) -> bool:
        missing_value_status = True  # Initially assumed to be no missing values
        data = pd.read_csv(self.config.unzip_data_dir)

        missing_values = data.isnull().sum()
        if missing_values.any():
            missing_value_status = False  # If the missing values is present

        self.validation_report["missing_value_status"] = missing_value_status

        return missing_value_status

    def check_data_types(self) -> bool:
        """
        validated the data type of all the columns
        :return: True if all the data types matches the defined schema else False
        """
        data_type_validation_status = True  # initially assumed to be of correct data type
        for column, expected_type in self.config.all_schema.items():
            if self.data[column].dtype != expected_type:
                data_type_validation_status = False  # sets false if violates data type validation
                break

        self.validation_report["data_type_validation_status"] = data_type_validation_status

        # Write the final validation status
        with open(self.config.STATUS_FILE, 'w') as f:
            f.write(f"validation report: {self.validation_report}")

        return data_type_validation_status

