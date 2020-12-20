import random

kullist = {"Ysf":"123123123", "Salmon":"321321321", "Volkan TAŞÇI":"asdasdas"}
shoplist = {"ütü":300, "laptop":1600, "çanta":150, "teleskop":4000, "piyano":5500 ,"yarı otomatik tüfek":9999, "Yiidoid":10000}
env = []

def giris(nick):
    if nick in kullist:
        if input("Şifre girin: ") == kullist.get(nick):
            print("Hoşgeldiniz {}".format(nick))
            alsvers(100*random.randrange(1,101), "")
        else:
            print("Yanlış şifre")
            giris(input("Kullanıcı adı girin: "))
    else: 
        print("Kullanıcı adı bulunamadı")
        giris(input("Kullanıcı adı girin: "))

def alsvers(bakiye, msj):
    print("="*25, "\n")
    for i in shoplist:
        print("{}  :  {}".format(i,  shoplist.get(i)), sep= "\n", end= "\n\n")
    print("="*25)
    print("Ürün almak için listeden bir eşya yazın.", "Çıkış için q girin.", "Bakiyeniz = {}".format(bakiye), msj, sep= "\n", end = "\n\n")
    sec = input("Seçiminiz: ")
    if sec in shoplist:
        if (bakiye >= shoplist.get(sec)):
            bakiye -= shoplist.get(sec)
            env.append(sec) 
            print("Eşya envantere eklendi.", "Envanteriniz:", "{}".format(env), sep="\n")
        else:
            print("Bakiyeniz yeterli değil.")
        print("Alışveriş menüsüne dönmek için entera basın, Çıkış için herhangi bir değer girin")
        if input("Seçiminiz: ") == "":
            alsvers(bakiye, "")
        else:
            quit()
        msj = ""
    elif sec == "q" or sec == "Q":
        print("Çıkış yapılıyor.")
        quit()
    else:
        alsvers(bakiye, "Seçilen eşya listede bulunmamaktadır.")
    
giris(input("Kullanıcı adı girin: "))