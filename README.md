# Open source Transactional emails service

## Stack

- Web framework: `FastAPI`
- ORM: `SQLAlchemy 2.0`
- Migrations: `alembic`
- Database: `Postgres`

## Workflow

- New models must be imported here: `app.db.base`

- New routes must be registered here `app.api.dispatcher`

- New admin views must be added here `app.api.dispatcher`

- New `permission_targets` and `permission_actions` are created in migrations and hardcoded.
Each target and action must be put in the specific enum `app.api.permissions.enums`