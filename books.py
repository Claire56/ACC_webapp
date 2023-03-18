from fastapi import FastAPI

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Python for all', 'author':'Maria kyle','year': 2006},
    'book_2': {'title': 'AI principles', 'author':'Daniel Walu','year': 2008},
    'book_3': {'title': 'Scratch rocks', 'author':'claire kim','year': 2007},
    'book_4': {'title': 'Sci for all', 'author':'Kaf Josh','year': 2009},
    'book_4': {'title': 'Added here', 'author':'Penny Miles','year': 2019}

}

@app.put('/{book}')
def update_book(bk_title:str, bk_author:str, book:str):
    book = BOOKS[book]
    book.title = bk_title
    book.author = bk_author
    return f'{book} has been updated'


@app.get("/")
async def home():
    return BOOKS

@app.get("/home")
async def my_home():
    return {"message": "Hello Iam home "}

@app.get("/food")
async def food():
    return {"message": "Hello World of Food "}