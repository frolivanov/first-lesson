import webbrowser as wb
da = ["DA", "Da", "da", "dA", "да", "Да", "дА", "ДА", "lf", "Lf", "LF", "lF"]
def open_vk():
    url = "https://vk.com/"
    vk = ["vk", "контакт", "контач", "вконтислав", "вк", "вконтакте"]
    op = input ("Что вы хотите открыть? ")
    try:
        if op in vk:
             wb.open(url)
    except: 
        print()
    print("Я не знаю такого сайта(9(")
def open_2():
    url1 = "https://store.steampowered.com/?l=russian"
    want = input("Хотите открыть еще один сайт? ")
    if want in da:
        ask = input("Вы любите играть играть в игры? ") 
    elif ask in da:
        wb.open(url1)
    
open_vk()
open_2()
