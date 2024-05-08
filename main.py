from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Optional
from Functions import *

app = FastAPI()

@app.get("/UserForGenre/{genre}")
async def get_user_for_genre(genre: str):
    result = UserForGenre(genre)
    return JSONResponse(content=result)

@app.get("/developer_reviews_analysis/{developer_name}")
async def get_developer_reviews(developer_name: str):
    result = developer_reviews_analysis(developer_name)
    return JSONResponse(content=result)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
