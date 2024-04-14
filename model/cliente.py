from model.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

class Cliente(Base):

    __tablename__ = 'cliente'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column(String(150), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    telefone = Column(String(11), nullable=True)
    rua = Column(String(150), nullable=False)
    numero = Column(String(10), nullable=False)
    bairro = Column(String(20), nullable=False)
    cidade = Column(String(30), nullable=False)
    uf = Column(String(20), nullable=False)
    cep = Column(String(15), nullable=False)
    corretor_id = Column(Integer, ForeignKey('corretor.id'), nullable=False)
    corretor = relationship("Corretor", backref=backref('clientes', cascade='all, delete-orphan'))

    def __init__(self, nome, cpf, telefone, rua, numero, bairro, cidade, uf, cep, corretor_id):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
        self.corretor_id = corretor_id