from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key="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")

class Query(BaseModel):
    query: str

# DATA mẫu (sau thay bằng Drive)
DATA = """


19.	Cách tính ca đêm và thêm giờ vào ban đêm 
Làm việc vào ca đêm (từ 22h đến 6h sáng hôm sau) mức lương = 130% lương cơ bản 
Làm thêm giờ vào ban đêm, trước đó không làm thêm giờ ban ngày, mức lương thêm giờ = 200% lương cơ bản
Làm thêm giờ vào ban đêm mà trược đó có làm thêm giờ vào ban ngày, mức lương thêm giờ = 210% lương cơ bản 
Làm thêm giờ vào ban đêm ngày nghỉ hàng tuần, mức lương thêm giờ = 270% lương cơ bản 
Làm thêm giờ ban đêm ngày nghỉ lễ, nghỉ có hưởng lương, mức thêm giờ = 390% lương cơ bản 
20.	
Tháng làm việc của công ty sẽ bắt đầu từ ngày 21 tháng trước đến ngày 20 tháng này. Phiếu lương được gửi vào địa chỉ mall của người lao động 1 ngày trước ngày chi trả lương. Người lao động kiểm tra phiếu lương, nếu có sai lệch hoặc thắc mắc sẽ liên hệ với Phòng Hành chính để được giải đáp
21.	
Tiền lương được chi trả bằng chuyển khoản qua ngân hàng techcombank
 Ngày trả lương là ngày 25;  nếu ngày 25 là ngày nghỉ thì ngày trả lương sẽ là ngày làm việc tiếp theo
22.	
Các bạn có thể kiểm tra dữ liệu chấm công bằng cách đăng nhập vào trang web của công ty synztec.grear.host. đường link trang web công ty sẽ gửi tin nhắn riêng cho từng người lao động.
23. 
các chế độ phúc lợi khác 
Sau khi kết thúc thử việc, người lao động sẽ được hưởng những chế độ sau 
Kết hôn
-	NLĐ làm việc từ 2 tháng đến dưới 1 năm kết hốn lần 1 mức tiền mừng công ty là 500.000
-	 NLĐ làm việc từ 1 năm đến 3 năm kết hôn lần 1 mức tiền mừng cty là 700.000
-	 NLĐ làm việc trên 3 năm kết hôn lần 1 mức tiền mừng cty là 1.000.000
-	NLĐ kết hôn lần thứ 2, mức tiền mừng công ty là 300.000
-	Con NLĐ mức tiền mừng cty là 200.000 đồng/người

24.	 Chế độ sinh con
-	LĐ nữ sinh con lần 1, mức tiền mừng công ty là 500.000 đồng
-	LĐ nữ sinh con lần 2, mức tiền mừng công ty là 300.000 đồng
-	Sinh đôi trở lên, mức tiền mừng công ty là 300 đồng/ cháu
-	Vợ lao động nam sinh con, tiền mừng là 300.000 đồng

25.	Thăm bệnh
Tai nạn nằm viện từ 7 ngày đến dưới 15 ngày, mức tiền hỏi thăm là 1.000.000 đồng 
Phẫu thuật do tai nạn, nằm viện từ 7 ngày đến dưới 15 ngày, mức tiền hỏi thăm là 1.000.000 đồng
Phuẫ thuật do tai nạn sinh hoạt từ 7 ngày trởi lên, mức tiền hỏi thăm là 500.000 đồng 
Phẫu thuật do bệnh (không phải bệnh hiểm nghèo), mức tiền hỏi thăm là 500.000 đồng

26.	 Phúng viếng:
-	đối tượng là công nhân viên, tiền phúng viếng công ty là 5.000.000, 
-	Vợ, chồng con, tiền phúng viếng công ty là 1.000.000,
-	Bố mẹ 2 bên, tiền phúng viếng công ty là 1.000.000, 
-	Anh chị em ruột,tiền phúng viếng công ty là 300.000, 
-	ông bà ruột nội ngoại 2 bên, tiền phúng viếng công ty là 300.000

27.	Tri ân công nhân viên
-	Nhân viên làm việc có thâm niên 10 năm, mức tiền tri ân là 2.000.000
-	Nhân viên làm việc có thâm niên 15 năm, mức tiền tri ân là 1.000.000
-	Nhân viên làm việc có thân niên 20 năm, mức tiền tri ân là 3.000.000
-	Nhân viên làm việc có thân niên 25 năm, mức tiền tri ân là 2.000.000
-	Nhân viên làm việc có thân niên 30 năm, mức tiền tri ân là 5.000.000
-	Nhân viên nghỉ hưu, mức tiền tri ân là 1.000.000

Trên đây là thông tin về lương và các chế độ phúc lợi của công ty. Cảm ơn các bạn đã lắng nghe 


"""

@app.post("/search")
def search(q: Query):

    prompt = f"""
Dựa vào dữ liệu sau:

{DATA}

Trả lời câu hỏi: {q.query}

Nếu không có thì trả:
"Không tìm thấy thông tin phù hợp trong hệ thống."
"""

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "answer": res.choices[0].message.content
    }
