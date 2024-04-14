from routes.config import *
from model import *
from schemas import *
from flask_openapi3 import Tag
from sqlalchemy.exc import IntegrityError

corretor_tag = Tag(name="Corretor", description="cadastrar, consultar e excluir corretor")

import logging

logging.basicConfig(level=logging.DEBUG)


@app.post("/corretor", tags=[corretor_tag], responses={
    "200": CorretorSchema,
    "400": ErrorSchema,
    "409": ErrorSchema
})
def post_corretor(form: CorretorSchema):
    """ Cadastrar corretor
    """
    corretor = Corretor(
        nome = form.nome,
        cpf = form.cpf,
        telefone = form.telefone,
    )
    try:
        session = Session()
        session.add(corretor)
        session.commit()
        return apresenta_corretor(corretor), 200
    except IntegrityError as e:
        return {"message": "corretor já cadastrado"}, 409
    except Exception as e:
        return {"message": "não foi possível cadastrar o corretor"}, 400
    finally:
        session.close()
    

@app.get("/corretor", tags=[corretor_tag], responses={
    "200": CorretorViewSchema,
    "404": ErrorSchema,
    "400": ErrorSchema
})
def get_corretor(query: ConsultaCorretorSchema):
    """ Consultar corretor pelo id
    """
    try: 
        session = Session()
        corretor = session.query(Corretor).filter(Corretor.id == query.id).first()
        if not corretor:
            return {"message": "corretor não encontrado"}, 404
        return retorna_corretor(corretor), 200
    except Exception as e:
        return {"message": "erro ao buscar corretor"}, 400
    finally:
        session.close()


@app.delete("/corretor", tags=[corretor_tag], responses={
    "200": DeletaCorretorSchame,
    "400": ErrorSchema,
    "404": ErrorSchema
})
def delete_corretor(form: ConsultaCorretorSchema):
    """ Exclui o corretor pelo id
    """
    try:
        #Verifica se o corretor existe na base de dados
        session = Session()
        corretor = session.query(Corretor).filter(Corretor.id == form.id).first()
        if not corretor:
            return {"message": "corretor não encontrado"}, 404
        
        #verifica se existe cliente associado ao corretor que deseja a exclusão
        cliente = session.query(Cliente).filter(Cliente.corretor_id == corretor.id).first()
        #se o cliente não existir o corretor é deletado
        if not cliente:
            session.delete(corretor)
            session.commit()
            return {"corretor_excluído": apresenta_corretor(corretor)}, 200
        #caso o cliente exista, não é possível deletar o corretor
        return {"message": "não é possível deletar corretor associado a cliente"}, 400
        
    except Exception as e:
        return {"message": "não foi possível exlcuir o corretor"}, 400
    finally:
        session.close()