# External Integrations

**Analysis Date:** 2026-03-20

## APIs & External Services

**None Detected** - This is a standalone web application with no external API dependencies for its core web service functionality.

Game-related tools in the `tools/` directory support optional SNI (Serial Network Interface) protocol integration:
- SNI Server - Optional gRPC-based communication for real hardware/emulator integration (used in development tools only, not web service)
  - SDK/Client: `snirk` >=0.2.1
  - Usage: Game state monitoring, item tracking for speedrunning/development (`tools/sni_test.py`, `tools/sni_monitor.py`, `tools/sni_autotracker.py`)

## Data Storage

**Databases:**
- PostgreSQL 17 (production)
  - Connection: Environment variables `SQL_ENGINE`, `SQL_DATABASE`, `SQL_USER`, `SQL_PASSWORD`, `SQL_HOST`, `SQL_PORT`
  - Client: Django ORM via psycopg2-binary 2.9.10
  - Configured in: `smrpg_web_randomizer/settings.py`

- SQLite 3 (development fallback)
  - Local file-based database at `db.sqlite3`
  - Used when PostgreSQL is not configured

**File Storage:**
- Local filesystem only
  - Static files: served by Nginx from `staticfiles/` volume
  - Temporary files: generated during seed/patch creation (managed via `tempfile` module)
  - ROM files: uploaded by user, processed, and discarded (no persistence)

**Caching:**
- Django in-memory caching via Django settings
- No external cache service (Redis/Memcached) detected

## Authentication & Identity

**Auth Provider:**
- Custom/Django built-in only
  - Implementation: Django's built-in authentication system (`django.contrib.auth`)
  - Uses Django admin for internal access
  - CSRF protection enabled via `django.middleware.csrf.CsrfViewMiddleware`
  - No external OAuth, SSO, or third-party authentication

## Monitoring & Observability

**Error Tracking:**
- None detected - No external error tracking service (Sentry, Rollbar, etc.) integrated

**Logs:**
- Python logging to stdout/stderr via `logging.StreamHandler`
- Configured in `smrpg_web_randomizer/settings.py` (lines 129-163)
- Development: Console output with debug filtering
- Production: WARNING level and above logged to stdout for container log capture
- Application-specific logging at `randomizer.*` package level

## CI/CD & Deployment

**Hosting:**
- Docker container-based deployment
- Orchestrated via Docker Compose
- Nginx + Gunicorn architecture

**CI Pipeline:**
- None detected - No GitHub Actions, GitLab CI, or other CI service configured

**Containerization:**
- Development: `docker-compose.yml` with volume mounts for hot-reload
- Production: `docker-compose.prod.yml` with multi-stage builds
- Nginx container for reverse proxy
- PostgreSQL container with health checks

## Environment Configuration

**Required env vars (Production):**
- `DJANGO_SETTINGS_MODULE=smrpg_web_randomizer.settings` (set in `wsgi.py`)
- `SQL_ENGINE=postgresql` (to enable PostgreSQL)
- `SQL_DATABASE` - Database name
- `SQL_USER` - Database user
- `SQL_PASSWORD` - Database password
- `SQL_HOST` - Database hostname
- `SQL_PORT` - Database port (default 5432)
- `SECRET_KEY` - Django secret key for session/CSRF tokens
- `DEBUG` - Debug mode flag (0/1, must be 0 in production)
- `ALLOWED_HOSTS` - Comma/space-separated domain list
- `STATIC_URL` - Static file URL prefix (default `/static/`)
- `STATIC_ROOT` - Static file directory path
- `CSRF_TRUSTED_ORIGINS` - Origins allowed for CSRF protection when behind proxy

**Optional env vars:**
- `BETA` - Beta site flag (0/1)
- `TIME_ZONE` - Application timezone (default UTC)

**Secrets location:**
- Environment variables passed via Docker `.env` files:
  - `.env.dev` - Development Django settings
  - `.env.dev.db` - Development database credentials
  - `.env.prod` - Production Django settings
  - `.env.prod.db` - Production database credentials
  - `.env.prod.nginx` - Nginx environment (headers, cache settings, etc.)
- Alternative: `local_settings.py` for local development (not committed)

## Webhooks & Callbacks

**Incoming:**
- None detected - Web service does not accept incoming webhooks

**Outgoing:**
- None detected - Web service does not send webhooks to external services

## Game ROM Processing

**ROM Input/Output:**
- Receives uploaded ROM files from users via HTTP POST (multipart/form-data)
- Processes ROMs using custom game logic and patch builders
- Returns patched ROM files or patches for user download
- No external ROM storage or cloud service

**Patch Storage:**
- Seeds and patches stored in PostgreSQL database (models in `randomizer/models.py`):
  - `Seed` model: seed value, hash, version, flags, spoiler data
  - `Patch` model: region-specific BPS patches linked to seeds

---

*Integration audit: 2026-03-20*
