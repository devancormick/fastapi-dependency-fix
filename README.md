# FastAPI Dependency Fix

This project fixes dependency conflicts between Algolia Python SDK and AWS S3 packages (boto3/botocore) in a FastAPI backend application.

## Problem

The issue occurs during `pip install`, where Algolia Python SDK and AWS S3 packages (boto3/botocore) conflict and fail to install correctly.

## Solution

Dependency conflicts have been resolved by:
1. Pinning compatible versions of core dependencies
2. Ensuring urllib3, requests, and certifi versions are compatible across both packages
3. Using version ranges that allow flexibility while maintaining compatibility

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

API documentation: `http://localhost:8000/docs`

## Configuration

Copy `env.example` to `.env` and fill in your credentials:

```bash
cp env.example .env
```

## Resolved Dependencies

- **FastAPI**: >=0.104.0
- **Algolia SDK**: >=3.1.0,<4.0.0
- **boto3**: >=1.28.0,<2.0.0
- **botocore**: >=1.31.0,<2.0.0
- **urllib3**: >=1.26.0,<3.0.0 (shared dependency)
- **requests**: >=2.31.0,<3.0.0 (shared dependency)

These versions have been tested and verified to work together without conflicts.

## Testing

Test that both services can be imported:

```python
from services.algolia_service import AlgoliaService
from services.s3_service import S3Service
```

Both imports should work without errors.

## Project Structure

```
fastapi-dependency-fix/
├── main.py                 # FastAPI application
├── services/               # Service integrations
│   ├── __init__.py
│   ├── algolia_service.py  # Algolia service
│   └── s3_service.py       # AWS S3 service
├── requirements.txt        # Resolved dependencies
├── env.example            # Environment variables template
└── README.md              # This file
```
