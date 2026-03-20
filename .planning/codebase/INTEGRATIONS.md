# Integrations

## Databases

### PostgreSQL 17 (Production)
- Configured via environment variables: `SQL_ENGINE`, `SQL_DATABASE`, `SQL_USER`, `SQL_PASSWORD`, `SQL_HOST`, `SQL_PORT`
- Used in Docker production setup via `docker-compose.prod.yml`
- Driver: `psycopg2-binary==2.9.10`

### SQLite (Development)
- Default fallback when no SQL_ENGINE env var or `local_settings.py` is present
- File: `db.sqlite3` in project root

### Database Models
- `randomizer/models.py` — two models:
  - `Seed` — stores generated seed metadata (hash, seed number, version, flags, spoiler JSON)
  - `Patch` — stores generated ROM patches per region, linked to Seed via FK

## External Libraries (Non-PyPI)

### python-bps
- Git dependency: `git+https://gitlab.com/pidgezero_one/python-bps.git@0.1`
- BPS patch format library for ROM patching

### smrpgpatchbuilder
- PyPI package (`smrpgpatchbuilder==4.1.18`)
- Core patch building library — provides management commands and patch generation tools
- Installed in `patchvenv/`

### Wii.py
- WAD file handling for Wii Virtual Console ROM packing
- Used in `randomizer/views.py` for the pack endpoint

### nlzss
- LZSS compression/decompression for SNES ROM data
- Used in `randomizer/views.py`

## Authentication

- Django built-in auth (included in INSTALLED_APPS)
- No external auth providers (OAuth, SSO, etc.)
- Admin interface available at standard Django admin URL

## API Endpoints

### Web Routes (`randomizer/urls.py`)
- `GET /` — About/home page
- `GET /randomize` — Randomizer form page
- `POST /seed` — Generate a new seed
- `GET /seed/stream` — SSE stream for generation progress
- `GET /h/<hash>` — View seed by hash
- `GET /hash/<hash>/<region>` — Download patch for seed
- `POST /pack` — Pack ROM into Wii WAD format

### REST API
- `POST /api/v1/generate` — Programmatic seed generation
- `GET /api/v1/flags` — Get available flags/options

## Infrastructure

### Docker
- Development: `docker-compose.yml` (Django + SQLite)
- Production: `docker-compose.prod.yml` (Django + Gunicorn + Nginx + PostgreSQL)
- `Dockerfile` / `Dockerfile.prod` — Python 3.13-slim based images
- `entrypoint.sh` / `entrypoint.prod.sh` — startup scripts

### Nginx
- Reverse proxy in production (`nginx/` directory)
- Serves static files directly, proxies app requests to Gunicorn

### Static Files
- Served by Django in development, Nginx in production
- `STATIC_ROOT` configurable via env var
- Max upload size: 25 MB (for WAD file packing)

## Environment Variables

| Variable | Purpose |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | Debug mode toggle |
| `DJANGO_ALLOWED_HOSTS` | Allowed host headers |
| `CSRF_TRUSTED_ORIGINS` | Trusted CSRF origins |
| `SQL_ENGINE` | Database engine (set to "postgresql" for prod) |
| `SQL_DATABASE`, `SQL_USER`, `SQL_PASSWORD`, `SQL_HOST`, `SQL_PORT` | PostgreSQL connection |
| `STATIC_URL`, `STATIC_ROOT` | Static file serving |
| `TIME_ZONE` | Server timezone |
| `BETA` | Beta site flag |

## What's NOT Integrated
- No external monitoring (Sentry, Datadog, etc.)
- No caching layer (Redis, Memcached)
- No task queue (Celery)
- No email sending
- No CDN
- No CI/CD pipeline (no GitHub Actions workflows found)
- No external webhooks or third-party API calls
