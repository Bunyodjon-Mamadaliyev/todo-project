from django.shortcuts import HttpResponse

def home_page(request):
    html_response = """
        <style>
            textarea{
            margin-top: 10px;
            margin-left: 10px;
            }
            input[type="date"] {
            margin-top: 10px;
            }
            select{
            margin-top: 10px;
            }
            button{
            margin-top: 10px;
            }
            .v{
                display: flex;
            }
            .v .Vazifa{
                line-height: 0.1;
            }
            .v .Tavsif{
                margin-left: 15px;
                line-height: 0.1; 
            }
            .v .Muhimlik{
                margin-left: 15px;
                line-height: 0.1;
            }
            .v .Muddat{
                margin-left: 15px;
                line-height: 0.1;
            }
            .v .Holat{
                margin-left: 15px;
                line-height: 0.1;
            }
            
        </style>
        <h1>Yangi vazifa yeratish</h1>
        <div>Vazifa nomi: <input type = "text"> <br>
        <div>Tavsif: <textarea placeholder></textarea>
        <div>Muddati: <input type = "date"><br>
        <label for="priority">Muhimlik darajasi:</label>
        <select id="priority" name="priority">
            <option value="low">Past</option>
            <option value="medium">O'rta</option>
            <option value="high">Yuqori</option>
        </select><br>
        <button type="submit">Vazifani saqlash</button>
        
        
            <h2>Mavjud vazifalar</h2>
    <div class="v">
        <div class="Vazifa">
            <h4>Vazifa</h4>
            <h6>Hisobot tayorlash</h6>
            <h6>Mijoz bilan uchrashuv</h6>
            <h6>Prizentatsiya tayorlash</h6>
            <h6>Xodimlar uchun trening</h6>
            <h6>Loyiha hujjatlarini yangilash</h6>
        </div>
        <div class="Tavsif">
            <h4>Tavsif</h4>
            <h6>Oliy moliyaviy hisobotni tayyorlash va topshirish</h6>
            <h6>Yangi loyiha bo'yich mijoz bilan muzokaralar o'tkazish</h6>
            <h6>Yangi mahsulot uchun taqdimot slaydlarni tayyorlash</h6>
            <h6>Yangi dasturiy taminot bo'yicha xodimlarga qo'llanma berish</h6>
            <h6>Joriy loyihani texnik hujjatlarini yangilash va arxivlash</h6>
        </div>
        <div class="Muhimlik">
            <h4>Muhimlik</h4>
            <h6>Yuqori</h6>
            <h6>O'rta</h6>
            <h6>Past</h6>
            <h6>O'rta</h6>
            <h6>Past</h6>
        </div>
        <div class="Muddat">
            <h4>Muddat</h4>
            <h6>2023-05-31</h6>
            <h6>2023-05-25</h6>
            <h6>2023-06-05</h6>
            <h6>2023-06-10</h6>
            <h6>2023-06-15</h6>
        </div>
        <div class="Holat">
            <h4>Holat</h4>
            <h6>Bajarilmoqda</h6>
            <h6>Rejalashtirilgan</h6>
            <h6>Bajarilmoqda</h6>
            <h6>Rejalashtirilgan</h6>
            <h6>Bajarilmoqda</h6>
        </div>
    </div>
        
    """
    return HttpResponse(html_response)


