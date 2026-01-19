# Changelog

## [1.1.0] - Enhanced Features

### Added
- **Docker Support**: Dockerfile and docker-compose.yml for containerized deployment
- **Configuration Management**: Pydantic-based settings with environment variable support
- **Enhanced Health Checks**: Detailed health endpoint with service status
- **Service Status Endpoints**: Individual status endpoints for Algolia and S3
- **CORS Middleware**: Cross-origin resource sharing support
- **App Info Endpoint**: Application information and dependency status

### Improved
- Better service initialization with dependency injection
- Enhanced error handling
- More comprehensive health monitoring
- Environment-based configuration

### Usage

#### Docker Deployment
```bash
docker-compose up -d
```

#### Health Checks
```bash
# Basic health check
curl http://localhost:8000/health

# Detailed health check with service status
curl http://localhost:8000/health/detailed

# Individual service status
curl http://localhost:8000/services/algolia/status
curl http://localhost:8000/services/s3/status
```

#### Configuration
Set environment variables in `.env`:
```env
DEBUG=false
ALGOLIA_APP_ID=your_app_id
ALGOLIA_API_KEY=your_api_key
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_REGION=us-east-1
AWS_S3_BUCKET_NAME=your_bucket
```

## [1.0.0] - Initial Release

### Features
- FastAPI application with Algolia and S3 integrations
- Resolved dependency conflicts
- Basic health check endpoint
- Service wrappers for Algolia and S3
