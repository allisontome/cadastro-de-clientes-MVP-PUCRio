from pydantic import BaseModel, validator
from helpers.helper import valida_cpf, format_cpf
from schemas.corretor import CorretorViewSchema

class ClienteSchema(BaseModel):
    """ Define como o cliente a ser inserido deve ser representado
    """
    nome: str = "allison tomé"
    cpf: str = "301.119.140-94"
    telefone: str = "81985693265"
    rua: str = "rua um"
    numero: str = "25"
    bairro: str = "bairro"
    cidade: str = "cidade"
    uf: str = "Pernambuco" or "PE"
    cep: str = "55800000"
    corretor_id: int = 1

    @validator('cpf')
    def cpf_validator(cls, cpf):
        #Removendo caracteres não numericos
        cpf = ''.join(filter(str.isdigit, cpf))

        #validando cpf
        if not valida_cpf(cpf):
            raise ValueError('CPF inválido')
        return cpf
    
class ClienteViewSchema(BaseModel):
    """Representa como um cliente cadastrado é retornado
    """
    nome: str = "allison tomé"
    cpf: str = "111******55"


class ConsultaClienteSchema(BaseModel):
    """Define o parametro para consultar o cliente no banco
    """
    cpf: str = "301.119.140-94"

    @validator('cpf')
    def cpf_validator(cls, cpf):
        #Removendo caracteres não numericos
        cpf = ''.join(filter(str.isdigit, cpf))

        #validando cpf
        if not valida_cpf(cpf):
            raise ValueError('CPF inválido')
        return cpf

class EnderecoSchema(BaseModel):
    """ Schema base do endereço
    """
    rua: str
    numero: str
    bairro: str
    cidade: str
    uf: str
    cep: str

class ClienteCompletoSchema(BaseModel):
    """ Representação completa de como o cliente é retornado da base
    """
    id: int = 1
    nome: str = "allison tomé"
    cpf: str = "301.119.140-94"
    telefone: str = "81985693265"
    endereco_completo: str
    endereco_split: EnderecoSchema
    corretor: CorretorViewSchema

class ClienteIdSchema(BaseModel):
    """ Representa o parametro para deleção do cliente
    """
    id: int = 1

class ClienteEditSchema(BaseModel):
    """ Define como o cliente a ser inserido deve ser representado
    """
    id: int = 1
    nome: str = "allison tomé"
    telefone: str = "81985693265"
    rua: str = "rua um"
    numero: str = "25"
    bairro: str = "bairro"
    cidade: str = "cidade"
    uf: str = "Pernambuco" or "PE"
    cep: str = "55800000"
    corretor_id: int = 1

def apresenta_cliente(cliente):
    cpf_formatado = format_cpf(cliente.cpf)

    return {
        "nome": cliente.nome,
        "cpf": cpf_formatado,
    }

def format_endereco_completo(cliente):
    endereco_completo = f"{cliente.rua}, {cliente.numero}, {cliente.bairro}, {cliente.cidade} - {cliente.uf}, {cliente.cep}"
    return endereco_completo

def retorna_cliente(cliente, corretor):
    cpf_formatado = format_cpf(cliente.cpf)
    cpf_corretor_formatado = format_cpf(corretor.cpf)
    endereco_completo = format_endereco_completo(cliente)

    return {
        "id": cliente.id,
        "nome": cliente.nome,
        "cpf": cpf_formatado,
        "telefone": cliente.telefone,
        "endereco_completo": endereco_completo,
        "endereco_split": {
            "rua": cliente.rua,
            "numero": cliente.numero,
            "bairro": cliente.bairro,
            "cidade": cliente.cidade,
            "uf": cliente.uf,
            "cep": cliente.cep
        },
        "corretor": {
            "id": corretor.id,
            "nome": corretor.nome,
            "cpf": cpf_corretor_formatado,
            "telefone": corretor.telefone
        }
    }
