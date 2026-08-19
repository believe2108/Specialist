from datetime import datetime
from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel, Field


class Book(BaseModel):
    title: str = Field(min_length=2, description="Название книги")
    author: str = Field(min_length=2, description="Автор книги")
    published_year: Optional[int] = Field(default=0, ge=1, le=datetime.now().year)

class BookResponse(BaseModel):
    book_id: int
    book: Book

LIBRARY: Dict[int, BookResponse] = {
    1: BookResponse(book_id=1, book=Book(title="1984", author="Джордж Оруэлл", published_year=1949)),
    2: BookResponse(book_id=2, book=Book(title="Властелин колец", author="Джон Р. Р. Толкин")),
    3: BookResponse(book_id=3, book=Book(title="ForTest", author="Test Man", published_year=2009))
}

app = FastAPI()

@app.get("/books", summary="Получения книг в библиотеке")
async def get_books() -> List[BookResponse]:
    return list(LIBRARY.values())


@app.get("/books/{book_id}", summary="Получения книги по ID")
async def get_book(book_id: int) -> BookResponse | None:
    try:
        book = LIBRARY[book_id]
        return book
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Книга с ID: {book_id} не найдена")


@app.post("/books", summary="Добавление книги в библиотеку", response_model=BookResponse)
async def create_book(book: Book) -> BookResponse:
    new_id = len(LIBRARY) + 1
    new_book = BookResponse(book_id=new_id, book=book)
    LIBRARY[new_id] = new_book
    return new_book


@app.put("/books/{book_id}", summary="Обновление данных по ID книги")
async def update_book(book_id: int, book_data: Book) -> BookResponse:
    if book_id not in LIBRARY:
        raise HTTPException(status_code=404, detail=f"Книга с ID {book_id} не найдена")
    LIBRARY[book_id].book.title = book_data.title
    LIBRARY[book_id].book.author = book_data.author
    if book_data.published_year:
        LIBRARY[book_id].book.published_year = book_data.published_year
    return LIBRARY[book_id]


@app.delete("/books/{book_id}", summary="Удаление книги из библиотеки ID")
async def delete_book(book_id: int) -> str:
    if book_id not in LIBRARY:
        raise HTTPException(status_code=404, detail=f"Книга с ID {book_id} не найдена")
    del LIBRARY[book_id]
    return f"Книга с ID: {book_id} успешно удалена"


if __name__ == "__main__":
    uvicorn.run("Books:app", port=8000)
