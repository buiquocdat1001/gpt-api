from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key="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")

class Query(BaseModel):
    query: str

# DATA mẫu (sau thay bằng Drive)
DATA = """
TIỀN LƯƠNG VÀ CHẾ ĐỘ PHÚC LỢI 
Lương và phúc lợi là các khoản thu nhập và hỗ trợ mà người lao động nhận được từ công ty nhằm ghi nhận công sức làm việc và tạo động lực gắn bó bao gồm 6 nội dung liên quan đến hợp đồng lao động, lương và trợ cấp phúc lợi. Chúng ta sẽ cùng tìm hiểu từng nội dung nhé
3.	Hợp đồng lao động
Hợp đồng lao động có 2 bản giá trị tương đương, công ty lưu giữ 1 bản, NLĐ tự quản lý 1 bản. 
Hợp đồng lao động kí lần đầu tiền bao gồm thời gian thử việc và 1 năm làm việc chính thức, thời gian làm việc chính thức có hiệu lực sau khi hết thời gian thử việc, học việc. 
Sau khi hợp đồng lao động lần 1 hết hiệu lực, công ty và người lao động sẽ gia hạn hợp đồng lần 2 có thời hạn 24 tháng 
Hết hạn hợp đồng lần 2 công ty và người lao động đồng tiếp tục gia hạn lần 3, hợp đồng lần 3 sẽ không xác định thời hạn.
Thời gian học việc đối với công nhân là 1 tháng làm việc, đối với nhân viên là 2 tháng. 
4.  Lương chính và phụ cấp lương
Lương bao gồm: lương cơ bản, lương kỹ năng, phụ cấp thâm niên, phụ cấp trách nhiệm, phụ cấp phiên dịch, lương thêm giờ 
Trong đó lương cơ bản, lương kỹ năng, pc thâm niên, trách nhiệm được gọi là lương chính và là căn cứ tính bảo hiểm. 
phụ cấp các loại sẽ không được tính vào bảo hiểm.
5.	Đối với công nhân, lương thử việc và chính thức là 5.900.000 
Nhân viên lương thử việc = 95% lương thỏa thuận khi phỏng vấn. lương chính thức bằng 100% lương thỏa thuận
6.	Các loại phụ cấp lương bao gồm
– phụ cấp thâm niên
Bắt đầu từ năm làm việc thứ 2 trở đi các bạn sẽ có phụ cấp thâm niên. 
Ở năm thứ 2, mỗi tháng phụ cấp thâm niên là 50k/ tháng làm việc, năm thứ 3, 4 phụ cấp thâm niên là 30k/ thángvà từ năm thứ 5 trở đi, phụ cấp thâm niên là 20k/ tháng. Phụ cấp thâm niên sẽ được cộng trực tiếp vào lương chính. 
7.	
Phụ cấp trách nhiệm cho trả cho nhân viên quản lý
Phụ cấp kỹ năng kĩ thuật chi trả cho nhân viên bộ phận FC dựa trên đánh giá kĩ năng sau 1 năm làm việc.
Phụ cấp phiên dịch chi trả cho nhân viên sử dụng tiếng Nhật, tiếng Trung trong công việc hàng ngày. 

8.	 Trợ cấp các loại
Ngoài lương chính, các bạn sẽ được hỗ trợ phụ cấp chuyên cần, đi lại, nuôi con nhỏ và thuê nhà
Phụ cấp chuyên cần được chia làm 2 mức chi trả: mức chi trả cho ca hành chính là 350.000 / tháng, ca sáng, chiều, đêm là 400.000/ tháng 
9.	Các bạn sẽ bị trừ phụ cấp chuyên cần khi đi làm muộn, về sớm, nghỉ ốm hoặc nghỉ không lương. 
Trợ cấp chuyên cần sẽ bị trừ mất ½ nếu đi muộn, về sớm 2 buổi/tháng hoặc nghỉ không lương, nghỉ ốm 1 buổi/tháng 
Trợ cấp chuyên cần sẽ bị trừ hết nếu đi muộn về sớm qá 2 buổi trên tháng  hoặc nghỉ không lương, nghỉ ốm 2 buổi/ tháng 
10.	 Phụ cấp đi lại
Phụ cấp đi lại được chi trả cho NLĐ sử dụng phương tiện cá nhân để đi đến nơi làm việc. Tiền phụ cấp đi lại được tính bằng 20 lít xăng/ người/ tháng. Giá xăng được sử dụng để tính phụ cấp hàng tháng là xăng A95 do cơ quan chức năng của chính phủ công bố vào trước 1 ngày của tháng tính lương.
Nhân viên sử dụng xe buýt của công ty sẽ không được hưởng phụ cấp đi lại 
11.	
Công ty chi trả tiền phụ cấp đi lại cho NLĐ vào những ngày làm thêm,  tiền trợ cấp trả thêm = tiền xăng 1 tháng / 24 ngày * số ngày đi làm thêm
Công ty không chi trả tiền Phụ cấp đi lại cho Người Lao Động vào những ngày nghỉ làm (trừ trường hợp nghỉ phép hằng năm : Tiền Phụ cấp đi lại giảm trừ = Tiền phụ cấp đi lại 1 tháng : 24 ngày x số ngày nghỉ làm
12.	Các loại phụ cấp khác
Hỗ trợ thuê nhà là 50k/ tháng đối với công nhân viên có hộ khẩu thường trú cách công ty trên 20km và có thuê nhà trọ
Hỗ trợ nuôi con nhỏ là 50k/ cháu từ 6 tháng tuổi đến tròn 6 tuổi. Hỗ trợ nuôi con nhỏ chi trả cho cả cha và mẹ. 
13. Thưởng hàng tháng 
Thưởng công đoạn: công nhân viên làm việc trực tiếp tại các công đoạn sản xuất nhận mức thường từ 80.000 – 480.000 / tháng. Tiền thưởng sẽ thay đổi khi thay đổi vị trí làm việc. nhân viên văn phòng không được nhận tiền thưởng công đoạn. 
14.	Thưởng ca đêm: 15.000/ ca làm việc 
Thưởng năng suất kiểm tra cho công nhân kiểm tra được đánh giá tay nghề 
15.	Nâng lương hàng năm
Hàng năm công ty sẽ ký quyết định tăng lương. Thời điểm xét tăng lương vào ngày 1 tháng 1 hàng năm. Mức tăng lương bao gồm tăng lương cơ bản và tăng lương hiệu suất.
 Tăng lương cơ bản là việc tăng lương trên cơ sở biến động về giá cả thị trường và căn cứ quy định về lương tối thiểu vùng do chính phủ ban hành. 
Tăng lương hiệu suất được thực hiện căn cứ thành tích nâng cao năng lực của người lao động trong 1 năm trước và kết quả đánh giá nhân sự của người lao động.
16.	Thưởng hàng năm
Tiền thưởng hàng năm được chi trả thành 2 lần, chi trả lần 1 vào tháng 7 là 1 tháng lương, chi trả cho NLĐ làm việc đủ 6 tháng đầu năm . Chi trả lần 2 vào trước tết âm lịch, mức tiền thưởng bằng tiền thưởng cả năm – 1 tháng lương đã chi trả vào tháng 7. Mức thưởng phụ thuộc vào kết quả kinh doanh trong năm của công ty. 


17.	Cách tính lương và thông báo lương 
1 tháng công ty làm 24 ngày công,  
Lương ngày = lương chính chia cho 24 ngày 
Lương giờ = lương ngày chia 8 giờ 
Các bạn có thể tự tính lương thực lĩnh của mình bằng cách cộng các loại lương với các loại trợ cấp, thêm giờ, sau đó trừ đi phần bảo hiểm = 10,5% lương và 20.00 đoàn phí. Mức lương này sẽ được gửi vào tài khoản cá nhân của người lao động 

18.	Cách tính lương thêm giờ cho các ca làm việc ban ngày ( ca hành chính, ca sáng, ca chiều) như sau
-	Thêm giờ vào các ngày làm việc bình thường của công ty, mức lương thêm giờ = 150% lương cơ bản 
-	Thêm giờ vào các ngày nghỉ cuối tuần, mức lương thêm giờ  = 200% mức lương cơ bản 
-	Thêm giờ vào các ngày nghỉ lễ, nghỉ có hưởng lương = 300% mức lương cơ bản 

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