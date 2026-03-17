from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Query(BaseModel):
    query: str

FILE_LINK = "https://drive.google.com/uc?export=download&id=1cjy-vLebKdu7XgXz8EHevtc2V_HlVrAi"

def get_file_ids():
    return [FILE_LINK]

def load_data():
    text = ""
    for file_url in get_file_ids():
        try:
            r = requests.get(file_url)
            text += r.text + "\n"
        except:
            pass
    return text

DATA = load_data()

@app.post("/search")
def search(q: Query):
    if q.query.lower() in DATA.lower():
        return {"answer": "Có trong tài liệu Drive"}
    return {"answer": "Không thấy"}