import os
from sqlalchemy.engine import create_engine
from sqlalchemy.pool import NullPool

def create_mssql_engine() -> create_engine:
    """Create a SQLAlchemy engine for MSSQL database.

    Returns:
        create_engine: A SQLAlchemy engine for MSSQL database.
    """
    mssql_host = os.environ["MSSQL_HOST"]
    mssql_user = os.environ["MSSQL_USER"]
    mssql_passwd = os.environ["MSSQL_PASSWD"]
    mssql_db = os.environ["MSSQL_DB"]

    mssql_driver = "SQL+Server+Native+Client+10.0"
    mssql_url = f"mssql+pyodbc://{mssql_user}:{mssql_passwd}@{mssql_host}:1433/{mssql_db}?driver={mssql_driver}"

    engine = create_engine(mssql_url, poolclass=NullPool)
    return engine

def create_postgresql_engine() -> create_engine:
    """Create a SQLAlchemy engine for PostgreSQL database.

    Returns:
        create_engine: A SQLAlchemy engine for PostgreSQL database.
    """
    postgresql_host = os.environ["POSTGRESQL_HOST"]
    postgresql_user = os.environ["POSTGRESQL_USER"]
    postgresql_passwd = os.environ["POSTGRESQL_PASSWD"]
    postgresql_db = os.environ["POSTGRESQL_DB"]

    postgresql_url = f"postgresql+psycopg2://{postgresql_user}:{postgresql_passwd}@{postgresql_host}/{postgresql_db}"

    engine = create_engine(postgresql_url, poolclass=NullPool)
    return engine

# Example usage
mssql_engine = create_mssql_engine()
postgresql_engine = create_postgresql_engine()
