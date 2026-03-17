from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    query: str

# DATA GIẢ (sau này thay bằng Drive)
DATA = """
Quy định mật khẩu:
- Tối thiểu 8 ký tự
- Có chữ hoa, chữ thường, số
- Đổi mỗi 90 ngày
"""

@app.post("/search")
def search(q: Query):
    if q.query.lower() in DATA.lower():
        return {
            "answer": DATA,
            "source": " IT"
        }
    else:
        return {
            "answer": "Không tìm thấy thông tin phù hợp trong hệ thống."
        }