# Technology Stack

**Analysis Date:** 2026-03-20

## Languages

**Primary:**
- Python 3.13.7 - Primary application language for the entire project
- HTML/CSS - Frontend templates served by Django

## Runtime

**Environment:**
- Python 3.13 (specified in `Dockerfile` and `Dockerfile.prod`)

**Package Manager:**
- pip - Python dependency management
- Lockfile: `requirements.txt` (pinned versions)

## Frameworks

**Core:**
- Django 5.1.7 - Web framework for URL routing, views, models, and templates
- Configuration: `smrpg_web_randomizer/settings.py` with environment-based configuration

**Testing:**
- pytest 8.3.5 - Python test runner and framework
- No test configuration file detected; tests run via `pytest` command

**Build/Dev:**
- gunicorn 23.0.0 - WSGI application server for production
- Docker - Containerization for consistent deployment

## Key Dependencies

**Critical:**
- Django 5.1.7 - Web framework with admin interface, ORM, authentication, and template system
- psycopg2-binary 2.9.10 - PostgreSQL database adapter for production environment
- gunicorn 23.0.0 - Production application server

**Game/ROM Processing:**
- Wii.py 0.1 - Nintendo Wii game/ROM manipulation
- smrpgpatchbuilder 4.1.18 - Custom Super Mario RPG patch building utility
- python-bps 0.1 - BPS (Binary Patch Script) patch application from GitLab
- nlzss 0.1.2 - LZ77-based compression algorithm (used for Wii game data)
- pycryptodome 3.21.0 - Cryptographic functions for ROM/patch handling

**Data Processing:**
- PyYAML 6.0.2 - YAML parsing for configuration and data files
- Markdown 3.7 - Markdown rendering for documentation
- Pillow 10.4.0 - Image processing (likely for sprite/palette manipulation)
- scipy - Scientific computing (used for randomization algorithms)
- jsonfield2 4.0.0.post0 - Extended JSON field support for Django models

**Tools (Optional):**
- snirk >=0.2.1 - gRPC client for SNI protocol (real hardware/emulator communication) in `tools/`
- websockets >=12.0 - WebSocket server support for SNI autotracker in `tools/`

## Configuration

**Environment:**
- Configuration via environment variables (Docker) or `local_settings.py` (local development)
- Key environment variables:
  - `DJANGO_SETTINGS_MODULE` - Set to `smrpg_web_randomizer.settings`
  - `DEBUG` - Enable/disable debug mode (0/1)
  - `SECRET_KEY` - Django secret key
  - `ALLOWED_HOSTS` - Space-separated list of allowed hosts
  - `SQL_ENGINE` - Database engine (`postgresql` for production)
  - `SQL_DATABASE`, `SQL_USER`, `SQL_PASSWORD`, `SQL_HOST`, `SQL_PORT` - PostgreSQL connection
  - `STATIC_URL`, `STATIC_ROOT` - Static file configuration
  - `BETA` - Beta site flag (0/1)
  - `TIME_ZONE` - Application timezone

**Build:**
- `Dockerfile` - Development container (Python 3.13-slim, volume mounts)
- `Dockerfile.prod` - Multi-stage production build with optimized layer caching

## Database

**Development:**
- SQLite 3 (default fallback via `db.sqlite3`)

**Production:**
- PostgreSQL 17 - Specified in `docker-compose.prod.yml`
- Connection via psycopg2-binary through Django ORM
- Healthcheck configured for container orchestration

## Platform Requirements

**Development:**
- Python 3.13
- Virtual environment (patchvenv)
- Docker and Docker Compose for containerized local development
- System dependencies: gcc, git, netcat-openbsd (in containers)

**Production:**
- Docker and Docker Compose
- PostgreSQL 17 container
- Nginx reverse proxy container (see `docker-compose.prod.yml`)
- Multi-container orchestration with internal networking

## Deployment

**Web Server:**
- Nginx - Reverse proxy and static file serving (`nginx/nginx.conf`)
- Gunicorn - WSGI application server bound to port 8000

**Containerization:**
- Docker Compose for local development (`docker-compose.yml`)
- Docker Compose for production (`docker-compose.prod.yml`)
- Multi-stage Dockerfile builds for production optimization
- Volume mounting for development hot-reload
- Internal networking for secure database communication

---

*Stack analysis: 2026-03-20*
