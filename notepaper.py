from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
import tkinter
import random
import requests
from bs4 import BeautifulSoup
from threading import Thread
from time import sleep
import datetime
from tkinter import messagebox
import os

root = Tk()
root.title("NOTEPAPER - by OlcaySoftware(Windows)")
photoicon = PhotoImage(file = "icons/notepaper.png")
root.iconphoto(False, photoicon)
root.geometry("900x550+200+90")
root.resizable(False,False)

#----------------------------------------#state=DISABLED
#----------------------------------------#
#baslik icin frame - tum notlar basligi
baslik = Frame(root,bg="#87cefa")
baslik.place(relx=0.02,rely=0,relwidth=0.25,relheight=0.3)

TumNotlar = Label(baslik,bg="#87cefa",fg="grey",font="Arial 15 bold")
TumNotlar.pack()


with open("log/notlar.txt", "r") as search:
    notSayisi = search.read().count("\n")
    toplam_not = "Tüm Notlar\n({})".format(str(notSayisi))
    TumNotlar["text"] = toplam_not
#---------------------------------------------------------#
#---------------------------------------------------------#
#frame

frame = Frame(root,bg="#87cefa")
frame.place(relx=0.02,rely=0.1,relwidth=0.25,relheight=0.5)

#---------------------------------------------------------#
#---------------------------------------------------------#
#frame2


def add_note():

    frame6 = Frame(root,bg="gray")
    frame6.place(relx=0.27,rely=0.2,relwidth=0.73,relheight=0.1)

    baslik_lab = Label(frame6,text="NOT BAŞLIGI:",font="Arial 10 bold",bg="gray",fg="white")
    baslik_lab.pack(padx=25,side=LEFT)
    not_basligi = Entry(frame6,bd=2,relief=FLAT)
    not_basligi.pack(padx=5,pady=10,side=LEFT)

    dt_lab = Label(frame6,text="TARİH SEÇİNİZ",font="Arial 10 bold",bg="gray",fg="white")
    dt_lab.pack(side=LEFT)
    dt = DateEntry(frame6,width=10,background="gray",foreground="white",borderwidth=1,locale = "de_DE")
    dt._top_cal.overrideredirect(False)
    dt.pack(padx=10,pady=10,side=LEFT)
    def save():
        if not_basligi.get():
            sor=not_basligi.get()
            dosya_isim = "mynotes/{}.txt".format(sor)
            tarih = dt.get()
            mesaj = metin_alani.get("1.0","end")
       

            with open(dosya_isim,"w") as dosya:

                dosya.write(
                    "Date:{}\n---------------\n{}\nBY NOTEPAPER - OLCAYSOFTWARE".format(tarih,mesaj))
                dosya.close()

            notlarim_bolumu = open("log/notlar.txt","a")
            yaz = "{}\n".format(sor)
            ekle = notlarim_bolumu.write(yaz)
            notlarim_bolumu.close()
            messagebox.showinfo("KAYIT BAŞARILI","NOTUNUZ BAŞARILI BİR ŞEKİLDE KAYDEDİLDİ")
        else:
            messagebox.showerror("İŞLEM HATASI","BOŞ VEYA EKSİK ALANLAR VAR\nLÜTFEN BİLGİLERİ KONTROL EDİNİZ!\n(not başlıgı)")



    savebtn = Button(frame6,text="Save",bg="green",fg="white",relief=FLAT,command=save)
    savebtn.pack(padx=15,pady=10,side=LEFT)

    frame7 = Frame(root,bg="gray")
    frame7.place(relx=0.27,rely=0.3,relwidth=0.73,relheight=0.9)

    metin_alani = Text(frame7,height=23,width=80,bg="lightgray",fg="black",font="Arial 11 bold")
    metin_alani.tag_configure("style",foreground="#333",font=("Arial",10,"bold"))
    metin_alani.pack(anchor=S)

    karsilama = "lütfen notunuzu giriniz..."
    metin_alani.insert(END,karsilama,"style")


frame2 = Frame(root,bg="#87cefa")
frame2.place(relx=0.02,rely=0.6,relwidth=0.25,relheight=0.13)
add_image = PhotoImage(file="icons/add.png")
add_btn = Button(frame2,image=add_image,relief=FLAT,bg="#87cefa",command=add_note)
add_btn.pack()

#---------------------------------------------------------#
#---------------------------------------------------------#
#frame3
def editle():
    
    def okumaİslemi():
        try:

            okumaF = Frame(root,bg="gray")
            okumaF.place(relx=0.27,rely=0.2,relwidth=0.73,relheight=0.1)
            read_mode = Label(okumaF,text="-OKUMA MODU AÇIK-",bg="gray",fg="lightgrey",font="Arial 10 bold")
            read_mode.pack(padx=10,pady=10,side=LEFT)

            def edit_mode():

                okumaF = Frame(root,bg="gray")
                okumaF.place(relx=0.27,rely=0.2,relwidth=0.73,relheight=0.1)
                read_mode = Label(okumaF,text="-DÜZENLEME MODU AÇIK-",bg="gray",fg="lightgrey",font="Arial 10 bold")
                read_mode.pack(padx=10,pady=10,side=LEFT)

                def save_mode():
                    
                    dosyaİsmi = mylist.get(mylist.curselection())
                    dosyaismi_uzanti = "mynotes/{}.txt".format(dosyaİsmi)
                    alan = okuma_alani2.get("1.0","end")
                    dosya = open(dosyaismi_uzanti,"w")
                    dosya.write(alan)
                    dosya.close()
                    read_mode["text"] = "NOT DÜZENLENDİ."



                edit_btn2 = Button(okumaF,text="Save",bg="green",fg="white",font="Arial 10 bold",command=save_mode)
                edit_btn2.pack(padx=10,pady=10,side=LEFT)
                yazi=mylist.get(mylist.curselection())
                ac = "mynotes/{}.txt".format(yazi)
                notAc = open(ac,"r")
                notu_oku = notAc.read()
                notAc.close()
         
                oku_panel = Frame(root,bg="lightgray")
                oku_panel.place(relx=0.27,rely=0.3,relwidth=0.73,relheight=0.9)
                okuma_alani2 = Text(oku_panel,height=23,width=80,bg="lightgray",fg="black",font="Arial 11 bold")
                okuma_alani2.tag_configure("style",foreground="#333",font=("Arial",10,"bold"))
                okuma_alani2.pack(anchor=S)
                okuma_alani2.insert(END,notu_oku,"style")
                

            edit_btn2 = Button(okumaF,text="Edit Mode",bg="green",fg="white",font="Arial 10 bold",command=edit_mode)
            edit_btn2.pack(padx=10,pady=10,side=LEFT)
            yazi=mylist.get(mylist.curselection())
            ac = "mynotes/{}.txt".format(yazi)
            notAc = open(ac,"r")
            notu_oku = notAc.read()
            notAc.close()
         
            oku_panel = Frame(root,bg="lightgray")
            oku_panel.place(relx=0.27,rely=0.3,relwidth=0.73,relheight=0.9)
            okuma_alani = Text(oku_panel,height=23,width=80,bg="lightgray",fg="black",font="Arial 11 bold")
            okuma_alani.tag_configure("style",foreground="#333",font=("Arial",10,"bold"))
            okuma_alani.pack(anchor=S)
            okuma_alani.insert(END,notu_oku,"style")
            okuma_alani["state"] = DISABLED
        except:
            silindi = Frame(root,bg="gray")
            silindi.place(relx=0.27,rely=0.5,relwidth=0.73,relheight=0.1)
            Label(silindi,text="LÜTFEN DÜZENLEMEK VEYA OKUMAK İSTEDİGİNİZ NOTU SEÇİNİZ!!!",bg="gray",fg="yellow",font="Arial 12 bold").pack()
    read_work = Thread(target=okumaİslemi)
    read_work.start()

   


frame3 = Frame(root,bg="#87cefa")
frame3.place(relx=0.02,rely=0.73,relwidth=0.25,relheight=0.13)

edit_image = PhotoImage(file="icons/edit.png")
edit_btn = Button(frame3,image=edit_image,relief=FLAT,bg="#87cefa",command=editle)
edit_btn.pack()
#---------------------------------------------------------#
#---------------------------------------------------------#
#frame4
def delete():

    try:

        f = open("log/notlar.txt","r")
        lines = f.readlines()
        f.close()

        f = open("log/notlar.txt","w")
        yazi=mylist.get(mylist.curselection())
        silinecek_satir = "{}".format(yazi)
        uzanti = "mynotes/{}.txt".format(yazi)
        for line in lines:
          if line!=silinecek_satir+"\n":
            f.write(line)
        
        f.close()
        os.unlink(uzanti) 

        silindi = Frame(root,bg="gray")
        silindi.place(relx=0.27,rely=0.2,relwidth=0.73,relheight=0.1)
        Label(silindi,text="SİLME İŞLEMİ BAŞARILI\n(Güncellemek için kapatıp açınız..)",bg="gray",fg="yellow",font="Arial 12 bold").pack()
        def yokEt():
            sleep(6)
            silindi = Frame(root,bg="gray")
            silindi.place(relx=0.27,rely=0.2,relwidth=0,relheight=0)
            Label(silindi,text="SİLME İŞLEMİ BAŞARILI",bg="gray",fg="yellow",font="Arial 12 bold").pack()
        yoketislem = Thread(target=yokEt)
        yoketislem.start()
    except:
        silindi = Frame(root,bg="gray")
        silindi.place(relx=0.27,rely=0.2,relwidth=0.73,relheight=0.1)
        Label(silindi,text="SİLMEK İSTEDİGİNİZ NOTU SEÇİNİZ\n(Güncellemek için kapatıp açınız..)",bg="gray",fg="yellow",font="Arial 12 bold").pack()
   
   
#---------------------------------------------------------#
frame4 = Frame(root,bg="#87cefa")
frame4.place(relx=0.02,rely=0.86,relwidth=0.25,relheight=0.14)

delete_image = PhotoImage(file="icons/delete.png")
delete_btn = Button(frame4,image=delete_image,relief=FLAT,bg="#87cefa",command=delete)
delete_btn.pack()
#---------------------------------------------------------#
#---------------------------------------------------------#
#frame5

def havadurumu():
    
    try:
        frame5["bg"] = "#66CCFF"
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=".format("izmir")
        api = "e7d2c6c38b9ae7616ec4a3579c9313cf&lang=tr"
        ara = url+api
        r = requests.get(ara)
        sleep(3)
        yaz = r.json()
        isim = yaz["name"]
        country = yaz["sys"]["country"]
        temp = int(yaz["main"]["temp"]-273.15)
        con = yaz["weather"][0]["description"]
        tarih = datetime.datetime.now()
        mesg = "{} ülkesi {} şehiri hava durumu\nsıcaklık:{}ϲ∘\tdurum:{}\tTarih: {}".format(country,isim,temp,con,tarih)
        Hl["text"] = mesg
        frame5["bg"] = "#87cefa"
       
    except:
        pass
        #Hl["text"] = "İNTERNET BAGLANTISI YOK."

t1 = Thread(target=havadurumu)
t1.start()

frame5 = Frame(root,bg="#87cefa")
frame5.place(relx=0.27,rely=0,relwidth=0.73,relheight=0.2)
hvdrm_icon = PhotoImage(file="icons/hava.png")
H_İMAGE = Label(frame5,image=hvdrm_icon,bg="#87cefa")
H_İMAGE.pack(padx=50,side=LEFT)

Label(frame5,text="Notepaper",font="Arial 10 bold",bg="#87cefa",fg="gray").pack(side=LEFT)

Hl = Label(frame5,bg="#87cefa",fg="gray")
Hl.pack(side=RIGHT)

#---------------------------------------------------------#
#---------------------------------------------------------#
#frame6
rastgele = random.randint(2,6)
resim = "images/plaj{}.png".format(rastgele)

background = PhotoImage(file=resim)
frame6 = Frame(root,bg="black")
frame6.place(relx=0.27,rely=0.2,relwidth=0.73,relheight=0.8)
bg_image = Label(frame6,image=background,height=1360)
bg_image.pack()



scrollbar = Scrollbar(root,width=10,elementborderwidth=-10)
scrollbar.pack( side = LEFT, fill = Y )

mylist = Listbox(frame, yscrollcommand = scrollbar.set ,width=45,height=18,bg="#66CCFF",fg="#2f4f4f",font="Arial 15 bold",selectbackground="#8fbc8f",)



dosya = open("log/notlar.txt","r")
oku = dosya.read()
dosya.close()
a = 1
for i in oku.splitlines():

   
    
    mylist.insert(END,i)

    mylist.pack(padx=5,pady=2,side=LEFT)
    scrollbar.config( command = mylist.yview )


    
#---------------------------------------------------------#
#---------------------------------------------------------#



mainloop()






