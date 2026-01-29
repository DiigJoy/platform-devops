from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+psycopg://app:app@localhost:5432/platform"
    cors_origins: str = "http://localhost:3000"  # comma-separated allowed origins
    service_name: str = "platform-api"
    env: str = "local"
    log_level: str = "INFO"
    version: str = "0.1.0"
    influxdb_url: str = "http://localhost:8086"
    influxdb_token: str = "dev-token"
    influxdb_org: str = "platform"
    influxdb_bucket: str = "iot_agri"
    mqtt_broker_host: str = "localhost"
    mqtt_broker_port: int = 1883

    def cors_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]

settings = Settings()
