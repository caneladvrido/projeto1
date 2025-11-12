from pydantic import BaseModel
from fastapi import HTTPException, APIRouter
from connection import conexaoBanco

class subraca(BaseModel):
    nome: str
    bonus: str
    raça: int

rota_subraca = APIRouter(prefix='/subraça', tags = ['subraça'])
@rota_subraca.get("/")
def get_subraca():
    cursor = conexaoBanco.cursor()
    comando_sql = "select * from Subraca"
    cursor.execute(comando_sql)
    resultado_consulta = cursor.fetchall()
    return resultado_consulta

@rota_subraca.post("/")
def post_subraca(item: subraca):
    cursor = conexaoBanco.cursor()
    comando_sql = "INSERT INTO Racas (nome) VALUES (%(nome)s, (%(bonus)s, (%(raca)s)"
    cursor.execute(comando_sql, item.model_dump())
    conexaoBanco.commit()
    return cursor.lastrowid