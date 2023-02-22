# Open source Transactional emails service

## Stack

- Web framework: `FastAPI`
- ORM: `SQLAlchemy 2.0`
- Migrations: `alembic`
- 

## Workflow

New models must be imported here: `app.db.base`

New routes must be registered here `app.api.dispatcher`

New admin views must be added here `app.api.dispatcher`