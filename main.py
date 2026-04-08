from fastapi import FastAPI
from routes import router as BookRouter

app = FastAPI(title="Library API")

app.include_router(BookRouter, tags=["Books"], prefix="/books")


@app.get("/")
async def root():
    return {"message": "API de Livros Online"}
