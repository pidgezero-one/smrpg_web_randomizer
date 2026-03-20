# Technology Stack

**Analysis Date:** 2026-03-20

## Languages

**Primary:**
- Python 3.13 - Backend application, randomizer logic, Django framework
  - Location: `smrpg_web_randomizer/`, `randomizer/`
  - Used for: Web application, patch generation, game data processing

## Runtime

**Environment:**
- Python 3.13-slim (Docker base image)
- Virtual environment: `patchvenv/` (development)

**Package Manager:**
- pip (Python Package Installer)
- Lockfile: Not detected (direct requirements.txt used)

## Frameworks

**Core Web Framework:**
- Django 5.1.7 - Web application framework
  - Configuration: `smrpg_web_randomizer/settings.py`
  - Version requirement: 5.1.7
  - WSGI application: `smrpg_web_randomizer/wsgi.py`

**Application Server:**
- Gunicorn 23.0.0 - Production WSGI HTTP server
  - Command: `gunicorn smrpg_web_randomizer.wsgi:application --bind 0.0.0.0:8000`
  - Used in production Docker deployment

**Testing:**
- pytest 8.3.5 - Test runner framework
  - Config: `pytest.ini` or command-line (not detected)

**Database ORM:**
- Django ORM (built-in) - Object-relational mapping
  - Models: `randomizer/models.py` (Seed, Patch)

## Key Dependencies

**Critical Core:**
- jsonfield2 4.0.0.post0 - JSON field support for Django models
  - Location: `randomizer/models.py` (spoiler JSONField)
- PyYAML 6.0.2 - YAML parsing and serialization
  - Used for: Configuration, game data
- Markdown 3.7 - Markdown parsing
  - Used for: Documentation/help text rendering

**Game Processing:**
- smrpgpatchbuilder 4.1.18 - SMRPG patch building library
  - Purpose: Generates patches for game ROM
  - Custom package from project
- Wii.py 0.1 - Wii-related utilities
  - Purpose: Game file handling
- nlzss 0.1.2 - NLZSS compression algorithm
  - Purpose: Game data compression/decompression
- python-bps 0.1 - BPS patching library
  - Source: `git+https://gitlab.com/pidgezero_one/python-bps.git@0.1#egg=python-bps`
  - Purpose: Binary patch creation and application

**Cryptography & Security:**
- pycryptodome 3.21.0 - Cryptographic library
  - Purpose: Encryption/decryption for game data
  - Provides AES, SHA, and other algorithms

**Data Processing:**
- Pillow 10.4.0 - Python Imaging Library
  - Purpose: Image processing for sprite/palette manipulation
- scipy (no version pinned) - Scientific computing
  - Purpose: Mathematical operations for randomization logic

**Utilities:**
- Python standard library modules:
  - binascii, hashlib, json, logging, queue, random, string, tempfile, shutil, threading, time
  - urllib (network operations)
  - copy, collections, os, sys, re

## Configuration

**Environment Variables (from settings.py):**
- `DJANGO_SETTINGS_MODULE` - Points to `smrpg_web_randomizer.settings`
- `SECRET_KEY` - Django secret key (required for production)
- `DEBUG` - Debug mode flag (0 for production, 1 for development)
- `DJANGO_ALLOWED_HOSTS` - Space-separated allowed hosts
- `CSRF_TRUSTED_ORIGINS` - Space-separated CSRF trusted origins
- `SQL_ENGINE` - Database engine (e.g., "postgresql")
- `SQL_DATABASE` - Database name (default: "smrpg")
- `SQL_USER` - Database user (default: "smrpg")
- `SQL_PASSWORD` - Database password
- `SQL_HOST` - Database host (default: "localhost")
- `SQL_PORT` - Database port (default: "5432")
- `STATIC_URL` - Static files URL (default: "/static/")
- `STATIC_ROOT` - Static files directory (default: "staticfiles/")
- `TIME_ZONE` - Application timezone (default: "UTC")
- `BETA` - Beta site flag (0 or 1)

**Local Development Alternative:**
- `local_settings.py` - Optional Python module for development configuration
  - Can override DATABASES, DEBUG, ALLOWED_HOSTS, etc.
  - Loaded via try/except import in settings.py

**Docker Configuration Files:**
- `.env.dev` - Development environment variables
- `.env.dev.db` - Development database configuration
- `.env.prod` - Production environment variables
- `.env.prod.db` - Production database configuration
- `.env.prod.nginx` - Nginx proxy configuration

**Build & Static Files:**
- Dockerfile - Development Docker image (Python 3.13-slim)
- Dockerfile.prod - Production Docker image with multi-stage build
- entrypoint.sh - Development entry script
- entrypoint.prod.sh - Production entry script

## Database

**Development:**
- SQLite 3 (default)
  - File: `db.sqlite3` at project root
  - Engine: `django.db.backends.sqlite3`

**Production:**
- PostgreSQL 17
  - Via Docker service in compose files
  - Connection pooling: Not detected (direct Django connection)
  - Healthcheck: pg_isready command with 5s interval

**ORM:**
- Django ORM (built-in models and migrations)
- Migrations: `randomizer/migrations/`

**Models:**
- `Seed` - Stores generated randomizer seeds with flags, version, hash, spoiler data
- `Patch` - Stores ROM patches by region and SHA1
- JSONField used for spoiler data storage

## File Storage

**Static Files:**
- Location: `randomizer/static/randomizer/`
  - CSS: `css/`
  - JavaScript: `js/`
  - Images: `images/`, `img/`, `patches/`
  - Palette previews: Auto-generated in `images/palette_previews/`

**Upload Handling:**
- Max upload size: 25 MB (DATA_UPLOAD_MAX_MEMORY_SIZE)
- Purpose: Support WAD file uploads

**Generated Files:**
- Patches: Stored in database, streamed as downloads
- Temporary: `tempfile` module used during generation

## Server & Proxy

**Production Deployment:**
- Gunicorn application server (Python WSGI)
- Nginx reverse proxy (separate Docker service)
- Both behind Docker compose networking
- Static volume shared between Gunicorn and Nginx
- HTTPS support via X-Forwarded-Proto header detection

## Monitoring & Logging

**Logging Configuration:**
- Handler: Console/StreamHandler to stdout/stderr
- Levels:
  - Root logger: WARNING in production, DEBUG in development
  - randomizer module: ERROR in development
  - Console output captured by Docker
- No external logging service configured

**Observability:**
- No error tracking service (Sentry, Rollbar, etc.) detected
- No APM/performance monitoring detected
- No metrics collection detected

## CI/CD & Version Control

**Version Control:**
- Git repository (`.git/` directory present)
- GitHub integration (`.github/` directory with workflows)
- Current branch: `v9-wip`
- Main branch: `master`

**Versioning:**
- Application version: `9.0.0` (from `randomizer/main.py`)
- Semantic versioning used (MAJOR.MINOR.PATCH)

**Build System:**
- Docker/Docker Compose for containerization
- No detected CI service integrations (GitHub Actions not fully explored)

## Development Tools

**Type Checking:**
- Pyright configuration: `pyrightconfig.json`
- Purpose: Python static type analysis

**Code Quality:**
- pytest for testing (framework installed, no config file detected)

## Platform Requirements

**Development:**
- Python 3.13
- Docker and Docker Compose
- Git
- Standard build tools (gcc for pip wheel compilation)
- netcat-openbsd (for database healthchecks)

**Production:**
- Docker and Docker Compose
- PostgreSQL 17 database
- 25 MB+ available memory for WAD uploads
- Network access (reverse proxy to Gunicorn via Docker networking)

**Deployment Target:**
- Docker containers (Linux-based)
- Python 3.13-slim base image
- Multi-stage Docker builds for optimized size
- Non-root user execution (app user in production)

---

*Stack analysis: 2026-03-20*
