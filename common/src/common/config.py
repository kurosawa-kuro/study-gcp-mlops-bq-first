"""Base settings — env-var / .env driven via pydantic-settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseAppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    project_id: str = "mlops-dev-a"
    region: str = "asia-northeast1"
    bq_dataset_mlops: str = "mlops"
    bq_dataset_feature_mart: str = "feature_mart"
    bq_table_training_runs: str = "training_runs"
    bq_table_predictions_log: str = "predictions_log"
    bq_table_feature_mart: str = "california_housing_features"
    gcs_models_bucket: str = "mlops-dev-a-models"
