from pydantic import BaseModel
from fastapi import HTTPException, APIRouter
from connection import conexaoBanco

class raca(BaseModel):
    nome: str

rota_raca = APIRouter(prefix='/raca', tags = ['raca'])
@rota_raca.get("/")
def get_raca():
    cursor = conexaoBanco.cursor()
    comando_sql = "select * from Racas"
    cursor.execute(comando_sql)
    resultado_consulta = cursor.fetchall()
    return resultado_consulta

@rota_raca.post("/")
def post_raca(item: raca):
    cursor = conexaoBanco.cursor()
    comando_sql = "INSERT INTO Racas (nome) VALUES (%(nome)s)"
    cursor.execute(comando_sql, item.model_dump())
    conexaoBanco.commit()
    return cursor.lastrowid
