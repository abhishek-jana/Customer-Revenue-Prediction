import os
from customer_revenue.constant.training_pipeline_config.data_ingesion import *

PIPELINE_NAME = "customer"
PIPELINE_ARTIFACT_DIR = os.path.join(os.getcwd(), "customer_artifact")