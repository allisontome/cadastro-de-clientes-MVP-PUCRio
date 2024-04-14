from flask_openapi3 import OpenAPI, Tag
from flask_cors import CORS
from flask import redirect

app = OpenAPI(__name__)
CORS(app)

doc_tag = Tag(name='Documentação', description='Página de documentação da API')

@app.get("/", tags=[doc_tag])
def doc():
    """ Página de documentação da API
    """
    return redirect("/openapi")