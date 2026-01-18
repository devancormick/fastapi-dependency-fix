"""
Test script to verify dependency installations and imports work correctly.
"""

import sys


def test_imports():
    """Test that all required packages can be imported."""
    errors = []
    
    # Test FastAPI
    try:
        import fastapi
        print(f"✓ FastAPI {fastapi.__version__}")
    except ImportError as e:
        errors.append(f"FastAPI import failed: {e}")
        print(f"✗ FastAPI import failed: {e}")
    
    # Test Algolia
    try:
        from algoliasearch.search_client import SearchClient
        print("✓ Algolia SDK imported successfully")
    except ImportError as e:
        errors.append(f"Algolia SDK import failed: {e}")
        print(f"✗ Algolia SDK import failed: {e}")
    
    # Test boto3
    try:
        import boto3
        print(f"✓ boto3 {boto3.__version__}")
    except ImportError as e:
        errors.append(f"boto3 import failed: {e}")
        print(f"✗ boto3 import failed: {e}")
    
    # Test botocore
    try:
        import botocore
        print(f"✓ botocore {botocore.__version__}")
    except ImportError as e:
        errors.append(f"botocore import failed: {e}")
        print(f"✗ botocore import failed: {e}")
    
    # Test shared dependencies
    try:
        import urllib3
        print(f"✓ urllib3 {urllib3.__version__}")
    except ImportError as e:
        errors.append(f"urllib3 import failed: {e}")
        print(f"✗ urllib3 import failed: {e}")
    
    try:
        import requests
        print(f"✓ requests {requests.__version__}")
    except ImportError as e:
        errors.append(f"requests import failed: {e}")
        print(f"✗ requests import failed: {e}")
    
    # Test service imports
    try:
        from services.algolia_service import AlgoliaService
        print("✓ AlgoliaService imported successfully")
    except ImportError as e:
        errors.append(f"AlgoliaService import failed: {e}")
        print(f"✗ AlgoliaService import failed: {e}")
    
    try:
        from services.s3_service import S3Service
        print("✓ S3Service imported successfully")
    except ImportError as e:
        errors.append(f"S3Service import failed: {e}")
        print(f"✗ S3Service import failed: {e}")
    
    if errors:
        print(f"\n{len(errors)} error(s) found:")
        for error in errors:
            print(f"  - {error}")
        return False
    
    print("\n✓ All imports successful - no dependency conflicts detected!")
    return True


if __name__ == "__main__":
    print("Testing dependency installations...\n")
    success = test_imports()
    sys.exit(0 if success else 1)
