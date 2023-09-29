from redwine import logger
from redwine.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline
from redwine.pipeline.stage2_data_validation import DataValidationTrainingPipeline
from redwine.pipeline.stage3_data_transformation import DataTransformationTrainingPipeline
from redwine.pipeline.stage4_model_trainer import ModelTrainingPipeline




STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_transformation = DataTransformationTrainingPipeline()
        data_transformation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = "Model Trainer stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_train = ModelTrainingPipeline()
        model_train.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e