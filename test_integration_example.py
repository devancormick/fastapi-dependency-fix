"""
Integration test example demonstrating the fix works correctly.
This demonstrates both Algolia and AWS S3 can coexist without conflicts.
"""

import sys
import os
from typing import Optional


def test_dependency_resolution():
    """Test that all dependencies can be installed and imported together."""
    print("=" * 60)
    print("DEPENDENCY RESOLUTION TEST")
    print("=" * 60)
    
    errors = []
    
    # Test core FastAPI dependencies
    print("\n1. Testing FastAPI dependencies...")
    try:
        import fastapi
        import uvicorn
        import pydantic
        print(f"   ✓ FastAPI {fastapi.__version__}")
        print(f"   ✓ Uvicorn {uvicorn.__version__}")
        print(f"   ✓ Pydantic {pydantic.__version__}")
    except ImportError as e:
        errors.append(f"FastAPI dependencies: {e}")
        print(f"   ✗ Error: {e}")
    
    # Test Algolia SDK
    print("\n2. Testing Algolia SDK...")
    try:
        from algoliasearch.search_client import SearchClient
        print("   ✓ Algolia SDK imported successfully")
        print("   ✓ SearchClient available")
    except ImportError as e:
        errors.append(f"Algolia SDK: {e}")
        print(f"   ✗ Error: {e}")
    
    # Test AWS S3 dependencies
    print("\n3. Testing AWS S3 dependencies...")
    try:
        import boto3
        import botocore
        print(f"   ✓ boto3 {boto3.__version__}")
        print(f"   ✓ botocore {botocore.__version__}")
    except ImportError as e:
        errors.append(f"AWS S3 dependencies: {e}")
        print(f"   ✗ Error: {e}")
    
    # Test shared dependencies
    print("\n4. Testing shared dependencies...")
    try:
        import urllib3
        import requests
        print(f"   ✓ urllib3 {urllib3.__version__}")
        print(f"   ✓ requests {requests.__version__}")
    except ImportError as e:
        errors.append(f"Shared dependencies: {e}")
        print(f"   ✗ Error: {e}")
    
    # Test service classes
    print("\n5. Testing service classes...")
    try:
        from services.algolia_service import AlgoliaService
        from services.s3_service import S3Service
        print("   ✓ AlgoliaService imported")
        print("   ✓ S3Service imported")
    except ImportError as e:
        errors.append(f"Service classes: {e}")
        print(f"   ✗ Error: {e}")
    
    # Summary
    print("\n" + "=" * 60)
    if errors:
        print(f"❌ FAILED: {len(errors)} error(s) found")
        for error in errors:
            print(f"   - {error}")
        return False
    else:
        print("✅ SUCCESS: All dependencies resolved correctly!")
        print("   No conflicts detected between Algolia and AWS S3 packages.")
        return True


def test_service_initialization():
    """Test that services can be initialized (without actual API calls)."""
    print("\n" + "=" * 60)
    print("SERVICE INITIALIZATION TEST")
    print("=" * 60)
    
    errors = []
    
    # Test Algolia Service initialization
    print("\n1. Testing AlgoliaService initialization...")
    try:
        from services.algolia_service import AlgoliaService
        
        # Initialize without credentials (should not raise import errors)
        service = AlgoliaService()
        print("   ✓ AlgoliaService can be instantiated")
        
        # Test with mock credentials
        service_with_creds = AlgoliaService(
            app_id="test_app_id",
            api_key="test_api_key"
        )
        print("   ✓ AlgoliaService accepts credentials")
        
    except Exception as e:
        errors.append(f"AlgoliaService initialization: {e}")
        print(f"   ✗ Error: {e}")
    
    # Test S3 Service initialization
    print("\n2. Testing S3Service initialization...")
    try:
        from services.s3_service import S3Service
        
        # Initialize without credentials (should not raise import errors)
        service = S3Service()
        print("   ✓ S3Service can be instantiated")
        
        # Test with mock credentials
        service_with_creds = S3Service(
            bucket_name="test-bucket",
            aws_access_key_id="test_key",
            aws_secret_access_key="test_secret"
        )
        print("   ✓ S3Service accepts credentials")
        
    except Exception as e:
        errors.append(f"S3Service initialization: {e}")
        print(f"   ✗ Error: {e}")
    
    # Summary
    print("\n" + "=" * 60)
    if errors:
        print(f"❌ FAILED: {len(errors)} error(s) found")
        for error in errors:
            print(f"   - {error}")
        return False
    else:
        print("✅ SUCCESS: Both services can be initialized!")
        print("   Ready for integration into FastAPI application.")
        return True


def test_fastapi_integration():
    """Test that FastAPI app works with both services."""
    print("\n" + "=" * 60)
    print("FASTAPI INTEGRATION TEST")
    print("=" * 60)
    
    try:
        from fastapi.testclient import TestClient
        from main import app
        
        client = TestClient(app)
        
        # Test root endpoint
        print("\n1. Testing root endpoint...")
        response = client.get("/")
        assert response.status_code == 200
        assert "message" in response.json()
        print("   ✓ Root endpoint working")
        
        # Test health endpoint
        print("\n2. Testing health endpoint...")
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"
        print("   ✓ Health endpoint working")
        
        print("\n" + "=" * 60)
        print("✅ SUCCESS: FastAPI application runs correctly!")
        print("   Both Algolia and S3 services can be integrated.")
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        return False


def main():
    """Run all integration tests."""
    print("\n" + "=" * 60)
    print("INTEGRATION TEST SUITE")
    print("Demonstrating Fixed Dependency Conflicts")
    print("=" * 60)
    
    results = []
    
    # Test 1: Dependency resolution
    results.append(("Dependency Resolution", test_dependency_resolution()))
    
    # Test 2: Service initialization
    results.append(("Service Initialization", test_service_initialization()))
    
    # Test 3: FastAPI integration
    results.append(("FastAPI Integration", test_fastapi_integration()))
    
    # Final summary
    print("\n" + "=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)
    
    all_passed = all(result[1] for result in results)
    
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 ALL TESTS PASSED!")
        print("Dependency conflict fix verified and working correctly.")
        print("\nThe fix ensures:")
        print("  • Algolia SDK installs without conflicts")
        print("  • AWS S3 (boto3/botocore) installs without conflicts")
        print("  • Both can coexist in the same environment")
        print("  • FastAPI application runs correctly")
        return 0
    else:
        print("❌ SOME TESTS FAILED")
        print("Please review the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
