# FastAPI Backend – Arquitectura Limpia

## Descripción
Backend construido con FastAPI siguiendo arquitectura hexagonal,
repositorios, casos de uso y migraciones con Alembic.

## Levantar el proyecto
```bash
pip install -r requirements.txt
alembic upgrade head
uvicorn src.main:app --reload