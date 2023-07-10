# IMPORTAR
from fastapi import FastAPI

# INSTANCIAR 
app = FastAPI()

#DECORADOR DE ROTA (TRATA REQ QUE VAO PARA A ROTA / USANDO GET)
@app.get("/")
#DEFININDO FUNCAO DA ROTA
def hello_root():
    #RETORNO DA ROTA
    return {"message": "Hello Word"}