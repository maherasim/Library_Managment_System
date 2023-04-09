from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from configparser import ConfigParser
from sqlalchemy import engine_from_config, create_engine


from alembic import context


config = context.config


if config.config_file_name is not None:
    fileConfig(config.config_file_name)

config = ConfigParser()
config.read('alembic.ini')
engine = engine_from_config(config['alembic'], prefix='sqlalchemy.')

engine = create_engine('mysql://root:12345678@localhost:3306/Library')



target_metadata = None


def run_migrations_online():
    engine = create_engine('')
    connection = engine.connect()
    context.configure(connection=connection, target_metadata=target_metadata)
    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
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
