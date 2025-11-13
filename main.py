from fastapi import FastAPI
from rotas.personagens import rota_personagens
from rotas.raca import rota_raca

app= FastAPI()

app.include_router(rota_personagens)
app.include_router(rota_raca)
