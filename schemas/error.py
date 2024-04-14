from pydantic import BaseModel

class ErrorSchema(BaseModel):
    """ Schema de apresentação da mensagem de erro
    """
    message: str