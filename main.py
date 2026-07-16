# Importa a classe FastAPI da biblioteca fastapi
from fastapi import FastAPI

# Cria a instância principal da aplicação FastAPI
app = FastAPI()

# Define a rota para o método HTTP GET no caminho raiz ("/")
@app.get("/")
def hello_world():
    # Retorna o dicionário JSON com a mensagem de boas-vindas
    return {"mensagem": "Olá, mundo! 🌍"}
