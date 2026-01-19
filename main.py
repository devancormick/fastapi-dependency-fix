"""
FastAPI application with Algolia and AWS S3 integrations.
Enhanced version with health checks and service status.
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import os

from config import settings
from services.algolia_service import AlgoliaService
from services.s3_service import S3Service

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="FastAPI application with resolved Algolia and AWS S3 dependencies"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Service instances (lazy initialization)
_algolia_service: AlgoliaService = None
_s3_service: S3Service = None


def get_algolia_service() -> AlgoliaService:
    """Get or create Algolia service instance."""
    global _algolia_service
    if _algolia_service is None:
        _algolia_service = AlgoliaService()
    return _algolia_service


def get_s3_service() -> S3Service:
    """Get or create S3 service instance."""
    global _s3_service
    if _s3_service is None:
        _s3_service = S3Service()
    return _s3_service


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "FastAPI application is running",
        "version": settings.app_version,
        "services": {
            "algolia": "configured" if settings.algolia_app_id else "not configured",
            "s3": "configured" if settings.aws_access_key_id else "not configured"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


@app.get("/health/detailed")
async def detailed_health_check(
    algolia: AlgoliaService = Depends(get_algolia_service),
    s3: S3Service = Depends(get_s3_service)
):
    """Detailed health check with service status."""
    health_status = {
        "status": "healthy",
        "services": {}
    }
    
    # Check Algolia
    if settings.check_algolia:
        try:
            algolia_configured = algolia.is_configured()
            health_status["services"]["algolia"] = {
                "status": "ok" if algolia_configured else "not_configured",
                "configured": algolia_configured
            }
        except Exception as e:
            health_status["services"]["algolia"] = {
                "status": "error",
                "error": str(e)
            }
    
    # Check S3
    if settings.check_s3:
        try:
            s3_configured = s3.is_configured()
            health_status["services"]["s3"] = {
                "status": "ok" if s3_configured else "not_configured",
                "configured": s3_configured
            }
        except Exception as e:
            health_status["services"]["s3"] = {
                "status": "error",
                "error": str(e)
            }
    
    # Overall status
    service_statuses = [s.get("status") for s in health_status["services"].values()]
    if "error" in service_statuses:
        health_status["status"] = "degraded"
    
    return health_status


@app.get("/services/algolia/status")
async def algolia_status(algolia: AlgoliaService = Depends(get_algolia_service)):
    """Get Algolia service status."""
    return {
        "configured": algolia.is_configured(),
        "app_id": settings.algolia_app_id if algolia.is_configured() else None
    }


@app.get("/services/s3/status")
async def s3_status(s3: S3Service = Depends(get_s3_service)):
    """Get S3 service status."""
    return {
        "configured": s3.is_configured(),
        "region": settings.aws_region if s3.is_configured() else None,
        "bucket": settings.aws_s3_bucket_name if s3.is_configured() else None
    }


@app.get("/info")
async def app_info():
    """Get application information."""
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "debug": settings.debug,
        "dependencies": {
            "algolia": "configured" if settings.algolia_app_id else "not configured",
            "aws_s3": "configured" if settings.aws_access_key_id else "not configured"
        }
    }
