"""
Test script to verify FastAPI application can start correctly.
"""

import sys
from fastapi.testclient import TestClient

try:
    from main import app
    
    client = TestClient(app)
    
    # Test root endpoint
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    print("✓ Root endpoint working")
    
    # Test health endpoint
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    print("✓ Health endpoint working")
    
    print("\n✓ FastAPI application is working correctly!")
    
except Exception as e:
    print(f"✗ Error testing FastAPI application: {e}")
    sys.exit(1)
