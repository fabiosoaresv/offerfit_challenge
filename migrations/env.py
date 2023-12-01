from alembic import context
from repositories.database import PostgresConnection

# Configurar a URL do SQLAlchemy com base nas configurações do seu projeto
url = "postgresql://postgres:postgres@localhost:5432/offerfit_development"

# Inicializar uma instância da sua classe PostgresConnection
postgres_connection = PostgresConnection()

# Usar a instância para estabelecer a conexão
postgres_connection.connect()

# Adicionar a conexão ao contexto do Alembic
context.configure(
    url=url,
    target_metadata=None,
    #literal_binds=True,
    dialect_opts={"paramstyle": "named"},
    conn=postgres_connection.connection,
    as_sql=True
)

# Marcar a conexão para fechar ao finalizar o ambiente
def run_migrations_offline():
    context.configure(
        url=url,
        target_metadata=None,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

with context.begin_transaction():
    run_migrations_offline()
