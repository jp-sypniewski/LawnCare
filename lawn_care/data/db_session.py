import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.orm import Session

from lawn_care.data.modelbase import SqlAlchemyBase

__factory = None


def global_init():
    global __factory

    if __factory:
        return

    username = 'username'
    password = 'password'
    db_name = 'lawncare'

    conn_str = 'mysql+mysqldb://' \
               + username + ':' + password + \
               '@localhost:3306/' + db_name

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import lawn_care.data.__all_models


def create_session() -> Session:
    global __factory

    session: Session = __factory()
    session.expire_on_commit = False

    return session
