from fastapi import FastAPI , Body

app = FastAPI()

BOOKS = [
    {'title': 'Python for all', 'author':'Maria kyle','year': 2006},
    {'title': 'AI principles', 'author':'Daniel Walu','year': 2008},
    {'title': 'Scratch rocks', 'author':'claire kim','year': 2007},
    {'title': 'Sci for all', 'author':'Kaf Josh','year': 2009},
    {'title': 'Added here', 'author':'Penny Miles','year': 2019}
]

@app.get("/")
async def home():
    return BOOKS

@app.get("/books/{book_title}")
async def get_one_book(book_title):
    for book in BOOKS:
        if book.title == book_title:
            return book

@app.post("/books/add_book")
async def add_book(new_book = Body()):
    BOOKS.append(new_book)


@app.put('/books/update_book')
def update_book(update_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.get('title').casefold() :
            BOOKS[i] = update_book

@app.delete('/books/delete_book/{book_title}')
def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold() :
            BOOKS.pop(i)
            break

    


    

