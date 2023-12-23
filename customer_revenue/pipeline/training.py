from customer_revenue.exception import CustomerException
from customer_revenue.logging import logger
from customer_revenue.config.pipeline.training import CustomerConfig
from customer_revenue.component.training.data_ingesion import DataIngestion
from customer_revenue.entity.artifact_entity import DataIngestionArtifact
import sys


class TrainingPipeline:

    def __init__(self, customer_config: CustomerConfig):
        self.customer_config: CustomerConfig = customer_config

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion_config = self.customer_config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact

        except Exception as e:
            raise CustomerException(e, sys)


    def start(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            
        except Exception as e:
            raise CustomerException(e, sys)