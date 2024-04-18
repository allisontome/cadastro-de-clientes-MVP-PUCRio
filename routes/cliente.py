from routes.config import app
from flask_openapi3 import Tag
from sqlalchemy.exc import IntegrityError
from schemas import *
from model import *

import logging

logging.basicConfig(level=logging.DEBUG)

cliente_tag = Tag(name="Cliente", description="Consultar, incluir, alterar e deletar cliente")


@app.post("/cliente", tags=[cliente_tag], responses={
    "200": ClienteCompletoSchema,
    "404": ErrorSchema,
    "400": ErrorSchema,
    "409": ErrorSchema
})
def post_cliente(form: ClienteSchema):
    """ Cadastra um novo cliente no banco de dados
    """
    logging.debug(form.nome)

    cliente = Cliente(
        nome = form.nome,
        cpf = form.cpf,
        telefone = form.telefone,
        rua = form.rua,
        numero = form.numero,
        bairro = form.bairro,
        cidade = form.cidade,
        uf = form.uf,
        cep = form.cep,
        corretor_id = form.corretor_id
    )
    try:
        session = Session()
        corretor = session.query(Corretor).filter(Corretor.id == form.corretor_id).first()
        if not corretor:
            return {"message": "corretor não cadastrado"}, 404
        session.add(cliente)
        session.commit()
        return retorna_cliente(cliente, corretor), 200
    except IntegrityError as e:
        return {"message": "Cliente já casdastrado"}, 409
    except Exception as e:
        return {"message": "Não foi possível executar"}, 400
    finally:
        session.close()
    


@app.get('/cliente', tags=[cliente_tag], responses={
    "200": ClienteCompletoSchema,
    "400": ErrorSchema,
    "404": ErrorSchema
})
def get_cliente(query: ConsultaClienteSchema):
    """ Consulta cliente cadastrado no banco pelo cpf
    """
    try:
        session = Session()
        cliente = session.query(Cliente).filter(Cliente.cpf == query.cpf).first()
        if not cliente:
            return {"message": "cliente não encontrado"}, 404
    except Exception as e:
        return {"message": "não foi possível buscar cliente"}, 400
    finally:
        session.close()
    
    corretor_id = cliente.corretor_id

    try:
        session = Session()
        corretor = session.query(Corretor).filter(Corretor.id == corretor_id).first()
    except Exception as e:
        return {"message": "erro ao buscar corretor"}, 400
    finally:
        session.close()
    
    return retorna_cliente(cliente, corretor)
    

@app.delete("/cliente", tags=[cliente_tag], responses={
    "200": ClienteViewSchema,
    "400": ErrorSchema,
    "404": ErrorSchema
})
def delete_cliente(query: ClienteIdSchema):
    """ Deleta cliente pelo id
    """
    try:
        session = Session()
        cliente = session.query(Cliente).filter(Cliente.id == query.id).first()
        
        if not cliente:
            return {"message": "cliente não encontrato"}, 404
        
        session.delete(cliente)
        session.commit()
    except Exception as e:
        return {"message": "não foi possível excluir cliente no momento"}, 400
    
    return {"cliente excluído": apresenta_cliente(cliente)}, 200


@app.put("/cliente", tags=[cliente_tag], responses={
    "200": ClienteCompletoSchema,
    "400": ErrorSchema,
    "404": ErrorSchema
})
def put_cliente(form: ClienteEditSchema):
    """ Atualiza os dados do cliente, menos o cpf
    """
    try: 
        session = Session()
        cliente = session.query(Cliente).filter(Cliente.id == form.id).first()

        if not cliente:
            return {"message": "cliente não encontrado"}, 404

        cliente.nome = form.nome
        cliente.telefone = form.telefone
        cliente.rua = form.rua
        cliente.numero = form.numero
        cliente.bairro = form.bairro
        cliente.cidade = form.cidade
        cliente.uf = form.uf
        cliente.cep = form.cep

        if form.corretor_id:
            corretor = session.query(Corretor).filter(Corretor.id == form.corretor_id).first()
            if not corretor:
                return {"message": "Corretor não encontrado"}, 404
            cliente.corretor_id = form.corretor_id
        session.commit()
            
        return retorna_cliente(cliente, corretor), 200
    
    except Exception as e:
        return {"message": f"{e}"}, 400
    finally:
        session.close()
    