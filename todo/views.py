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
            
        
    """
    return HttpResponse(html_response)


