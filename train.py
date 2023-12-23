from customer_revenue.pipeline.training import TrainingPipeline
from customer_revenue.config.pipeline.training import CustomerConfig

if __name__=="__main__":
    training_pipeline_config= CustomerConfig()
    training_pipeline = TrainingPipeline(customer_config=training_pipeline_config)
    training_pipeline.start()
