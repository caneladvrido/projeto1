from fastapi import FastAPI
from rotas.personagens import personagens

app= FastAPI()

app.include_router(rota_personagens)
app.include_router(rota_raça)
