from pydantic import BaseModel
from fastapi import HTTPException, APIRouter
from connection import conexaoBanco

class raca(BaseModel):
    nome: str

rota_raça = APIRouter(prefix='/raca', tags = ['raca'])
@rota_raça.get("/")
def get_raça():
    cursor = conexaoBanco.cursor(dictionary=True)
    comando_sql = "select * from Racas"
    cursor.execute(comando_sql)
    resultado_consulta = cursor.fetchall()
    return resultado_consulta

@rota_raça.post("/")
def post_raça(item: raca):
    cursor = conexaoBanco.cursor(dictionary=True)
    comando_sql = "INSERT INTO Racas (nome) VALUES (%(nome)s)"
    cursor.execute(comando_sql, item.model_dump())
    conexaoBanco.commit()
    return cursor.lastrowid
