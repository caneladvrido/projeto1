from pydantic import BaseModel
from fastapi import HTTPException, APIRouter
from connection import conexaoBanco

class personagens(BaseModel):
    nome: str
    idade: int
    classe: int
    raca: int
    antecedente: int

rota_personagens = APIRouter(prefix='/personagens', tags=['personagens'])

@rota_personagens.get("/")
def get_personagens():
    cursor = conexaoBanco.cursor(dictionary=True)
    comando_sql = "select * from Personagens"
    cursor.execute(comando_sql)
    resultado_consulta = cursor.fetchall()
    return resultado_consulta

@rota_personagens.post("/")
def post_personagens(item:personagens):
    cursor = conexaoBanco.cursor(dictionary=True)
    delimitar = "select * from Racas where id = %(raca)s"
    cursor.execute(delimitar)
    resultado_consulta = cursor.fetchone()

    if resultado_consulta is None:
        return {
            "mensagem" : "raça inexistente"
        }

    comando_sql = "INSERT INTO Personagens (nome, idade , classe , raca) VALUES (%(nome)s, %(idade)s, %(classe)s, %(raca)s, %(antecedente)s)"
    cursor.execute(comando_sql, item.model_dump())
    conexaoBanco.commit()
    return cursor.lastrowid
