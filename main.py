"""
FastAPI application with Algolia and AWS S3 integrations.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="FastAPI Dependency Fix", version="1.0.0")


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "FastAPI application is running"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
