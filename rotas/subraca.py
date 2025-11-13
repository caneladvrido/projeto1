from pydantic import BaseModel
from fastapi import HTTPException, APIRouter
from connection import conexaoBanco

class sub_raca(BaseModel):
    nome: str
    bonus: str
    raça: int

rota_sub_raca = APIRouter(prefix='/sub_raca', tags = ['sub_raca'])
@rota_sub_raca.get("/")
def get_sub_raca():
    cursor = conexaoBanco.cursor()
    comando_sql = "select * from sub_raca"
    cursor.execute(comando_sql)
    resultado_consulta = cursor.fetchall()
    return resultado_consulta

@rota_sub_raca.post("/")
def post_sub_raca(item: sub_raca):
    cursor = conexaoBanco.cursor()
    comando_sql = "INSERT INTO racas (nome) VALUES (%(nome)s, (%(bonus)s, (%(raca)s)"
    cursor.execute(comando_sql, item.model_dump())
    conexaoBanco.commit()
    return cursor.lastrowid