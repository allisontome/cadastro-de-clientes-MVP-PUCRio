from pydantic import BaseModel, validator
from typing import List
from helpers.helper import valida_cpf, format_cpf


class CorretorSchema(BaseModel):
    """ Define como o corretor a ser inserido deve ser representado
    """
    nome: str = "escritorio"
    cpf: str = "301.119.140-94"
    telefone: str = "81988552233"
    @validator('cpf')
    def cpf_validator(cls, cpf):
        #Removendo caracteres não numericos
        cpf = ''.join(filter(str.isdigit, cpf))

        #validando cpf
        if not valida_cpf(cpf):
            raise ValueError('CPF inválido')
        return cpf


class CorretorViewSchema(BaseModel):
    """ Define como o corretor é retornado
    """
    id: int = 1
    nome: str = "escritorio"
    cpf: str = "301.119.140-94"
    telefone: str = "81988552233"

class ListaCorretoresSchema(BaseModel):
    corretores: List[CorretorViewSchema]


class ConsultaCorretorSchema(BaseModel):
    id: int = 1

class DeletaCorretorSchame(BaseModel):
    corretor_excluido: CorretorSchema

def retorna_corretor(corretor):
    cpf_formatado = format_cpf(corretor.cpf)
    print(corretor)
    return {
        "id": corretor.id,
        "nome": corretor.nome,
        "cpf": cpf_formatado,
        "telefone": corretor.telefone
    }

def apresenta_corretor(corretor):
    cpf_formatado = format_cpf(corretor.cpf)

    return {
        "nome": corretor.nome,
        "cpf": cpf_formatado,
        "telefone": corretor.telefone
    }

def lista_corretores(corretores):
    return [{"id": corretor.id, "nome": corretor.nome, "cpf": corretor.cpf, "telefone": corretor.telefone} for corretor in corretores]