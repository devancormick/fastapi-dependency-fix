"""
Configuration management for FastAPI application.
"""

import os
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings."""
    
    # App settings
    app_name: str = "FastAPI Dependency Fix"
    app_version: str = "1.0.0"
    debug: bool = Field(default=False, env="DEBUG")
    
    # Algolia settings
    algolia_app_id: Optional[str] = Field(default=None, env="ALGOLIA_APP_ID")
    algolia_api_key: Optional[str] = Field(default=None, env="ALGOLIA_API_KEY")
    
    # AWS S3 settings
    aws_access_key_id: Optional[str] = Field(default=None, env="AWS_ACCESS_KEY_ID")
    aws_secret_access_key: Optional[str] = Field(default=None, env="AWS_SECRET_ACCESS_KEY")
    aws_region: str = Field(default="us-east-1", env="AWS_REGION")
    aws_s3_bucket_name: Optional[str] = Field(default=None, env="AWS_S3_BUCKET_NAME")
    
    # Service health checks
    check_algolia: bool = Field(default=True, env="CHECK_ALGOLIA")
    check_s3: bool = Field(default=True, env="CHECK_S3")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Global settings instance
settings = Settings()
