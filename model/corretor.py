from model.base import Base
from sqlalchemy import Column, String, Integer

class Corretor(Base):

    __tablename__ = 'corretor'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column(String(150), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    telefone = Column(String(11), nullable=True)

    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
