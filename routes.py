from fastapi import APIRouter, Body, HTTPException, status
from models import BookModel
from database import collection
from bson import ObjectId

router = APIRouter()


@router.post(
    "/",
    response_description="Adicionar novo livro",
    status_code=status.HTTP_201_CREATED,
)
async def create_book(book: BookModel = Body(...)):
    new_book = await collection.insert_one(book.dict())
    return {"id": str(new_book.inserted_id)}


@router.get("/", response_description="Listar livros")
async def list_books():
    books = []
    cursor = collection.find()
    async for document in cursor:
        document["_id"] = str(document["_id"])
        books.append(document)
    return books


@router.delete("/{id}", response_description="Deletar livro")
async def delete_book(id: str):
    delete_result = await collection.delete_one({"_id": ObjectId(id)})
    if delete_result.deleted_count == 1:
        return {"message": "Livro excluído"}
    raise HTTPException(status_code=404, detail="Livro não encontrado")
