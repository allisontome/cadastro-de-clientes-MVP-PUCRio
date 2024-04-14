from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import os

from model.base import Base
from model.cliente import Cliente
from model.corretor import Corretor

db_path = "database/"

""" Verificando se o path existe
"""
if not os.path.exists(db_path):
    """ caso não exista ele é criado
    """
    os.makedirs(db_path)

db_url = 'sqlite:///%s/db.sqlite3' % db_path

"""Criando a engine do banco
"""
engine = create_engine(db_url, echo=False)

""" Criando a session para comunicação com o banco
"""
Session = sessionmaker(bind=engine)

""" Verificar se o banco já existe
    Caso não exista ele é criado
""" 
if not database_exists(engine.url):
    create_database(engine.url)

""" Carregando as tabelas no banco de dados
"""
Base.metadata.create_all(engine)
"""Definindo corretor default da aplicação como escritório
"""