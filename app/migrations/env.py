from logging.config import fileConfig
import sys
from os.path import abspath, dirname
from sqlalchemy import engine_from_config, pool
from alembic import context

# Добавляем путь к проекту
sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))

# Импортируем ЕДИНУЮ Base и модели


from app.config import settings

from app.database import Base
from app.users.models import User      # Модели пользователей
from app.task.models import Task

config = context.config
config.set_main_option("sqlalchemy.url", f"{settings.DATABASE_URL}?async_fallback=True")



if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Используем метаданные единой Base
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()