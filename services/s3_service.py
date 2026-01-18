"""
AWS S3 service integration.
"""

from typing import Optional, BinaryIO, Dict, Any
import os


class S3Service:
    """Service for interacting with AWS S3."""
    
    def __init__(
        self,
        bucket_name: Optional[str] = None,
        aws_access_key_id: Optional[str] = None,
        aws_secret_access_key: Optional[str] = None,
        region_name: Optional[str] = None
    ):
        """
        Initialize S3 service.
        
        Args:
            bucket_name: S3 bucket name
            aws_access_key_id: AWS access key ID
            aws_secret_access_key: AWS secret access key
            region_name: AWS region name
        """
        self.bucket_name = bucket_name or os.getenv("AWS_S3_BUCKET_NAME")
        self._s3_client = None
        
        if aws_access_key_id and aws_secret_access_key:
            self._initialize_client(aws_access_key_id, aws_secret_access_key, region_name)
        elif os.getenv("AWS_ACCESS_KEY_ID") and os.getenv("AWS_SECRET_ACCESS_KEY"):
            self._initialize_client(
                os.getenv("AWS_ACCESS_KEY_ID"),
                os.getenv("AWS_SECRET_ACCESS_KEY"),
                region_name or os.getenv("AWS_REGION", "us-east-1")
            )
    
    def _initialize_client(
        self,
        aws_access_key_id: str,
        aws_secret_access_key: str,
        region_name: str = "us-east-1"
    ):
        """Initialize boto3 S3 client."""
        try:
            import boto3
            self._s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                region_name=region_name
            )
        except ImportError as e:
            raise ImportError(
                "boto3 not installed. Install with: pip install boto3"
            ) from e
    
    def upload_file(
        self,
        file_obj: BinaryIO,
        object_key: str,
        bucket_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Upload a file to S3.
        
        Args:
            file_obj: File-like object to upload
            object_key: S3 object key (path)
            bucket_name: S3 bucket name (uses default if not provided)
            
        Returns:
            Response dictionary
        """
        if not self._s3_client:
            raise RuntimeError("S3 client not initialized")
        
        bucket = bucket_name or self.bucket_name
        if not bucket:
            raise ValueError("Bucket name must be provided")
        
        self._s3_client.upload_fileobj(file_obj, bucket, object_key)
        return {"status": "success", "bucket": bucket, "key": object_key}
    
    def download_file(
        self,
        object_key: str,
        bucket_name: Optional[str] = None
    ) -> bytes:
        """
        Download a file from S3.
        
        Args:
            object_key: S3 object key (path)
            bucket_name: S3 bucket name (uses default if not provided)
            
        Returns:
            File contents as bytes
        """
        if not self._s3_client:
            raise RuntimeError("S3 client not initialized")
        
        bucket = bucket_name or self.bucket_name
        if not bucket:
            raise ValueError("Bucket name must be provided")
        
        response = self._s3_client.get_object(Bucket=bucket, Key=object_key)
        return response['Body'].read()
    
    def is_configured(self) -> bool:
        """Check if S3 is properly configured."""
        return self._s3_client is not None
