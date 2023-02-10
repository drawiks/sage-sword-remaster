from tkinter import *
# from tkinter.messagebox import showerror, showwarning, showinfo
import random

game = 1

money = 0

vraghp = 0

manna = 0

loss = 10
mloss = 20

p1 = 1
p2 = 1
p3 = 1

def play():
    global vraghp
    vrag.place(x=275 , y=50 , height=150 , width=50)
    eye.place(x=265 , y=50 , height=35 , width=70)
    vh.place(x=250 , y=0 , height=50 , width=100)
    attack.place(x=0 , y=200 , height=200 , width=300)
    mattack.place(x=300 , y=200 , height=200 , width=300)
    logo.place_forget()
    play.place_forget()
    lvl.place_forget()
    manna = 0
    if game == 1:
        vraghp = 1000
        vh["text"]="❤" + str(vraghp)
    elif game == 2:
        vraghp = 2500
        vh["text"]="❤" + str(vraghp)
    elif game == 3:
        vraghp = 5000
        vh["text"]="❤" + str(vraghp)
    elif game == 4:
        vraghp = 7500
        vh["text"]="❤" + str(vraghp)
    elif game == 5:
        vraghp = 10000
        vh["text"]="❤" + str(vraghp)

def back():
    logo.place(x=2 , y=10 , height=100 , width=600)
    play.place(x=200 , y=170 , height=60 , width=200)
    lvl.place(x=200 , y=240 , height=60 , width=200)
    win.place_forget()
    back.place_forget()

def attack():
    global vraghp
    global loss
    global game
    global manna
    global money
    money += random.randint(1,5)
    manna += 1
    vraghp -= loss
    vh["text"]="❤" + str(vraghp)
    if game == 1:
        if vraghp <= 0:
            vraghp = 0
            game = 2
            vrag.place_forget()
            vh.place_forget()
            eye.place_forget()
            win.place(x=0 , y=0 , height=200 , width=600)
            attack.place_forget()
            mattack.place_forget()
            back.place(x=200 , y=200 , height=70 , width=200)
            money += random.randint(300,600)
    elif game == 2:
        if vraghp <= 0:
            vraghp = 0
            game = 3
            vrag.place_forget()
            vh.place_forget()
            eye.place_forget()
            win.place(x=0 , y=0 , height=200 , width=600)
            attack.place_forget()
            mattack.place_forget()
            back.place(x=200 , y=200 , height=70 , width=200)
            money += random.randint(350,700)
    elif game == 3:
        if vraghp <= 0:
            vraghp = 0
            game = 4
            vrag.place_forget()
            vh.place_forget()
            eye.place_forget()
            win.place(x=0 , y=0 , height=200 , width=600)
            attack.place_forget()
            mattack.place_forget()
            back.place(x=200 , y=200 , height=70 , width=200)
            money += random.randint(400,750)
    elif game == 4:
        if vraghp <= 0:
            vraghp = 0
            game = 5
            vrag.place_forget()
            vh.place_forget()
            eye.place_forget()
            win.place(x=0 , y=0 , height=200 , width=600)
            attack.place_forget()
            mattack.place_forget()
            back.place(x=200 , y=200 , height=70 , width=200)
            money += random.randint(450,800)
    elif game == 5:
        if vraghp <= 0:
            vraghp = 0
            #game += 1
            vrag.place_forget()
            vh.place_forget()
            eye.place_forget()
            win.place(x=0 , y=0 , height=200 , width=600)
            attack.place_forget()
            mattack.place_forget()
            back.place(x=200 , y=200 , height=70 , width=200)
            money += random.randint(550,900)
            

def mattack():
    global vraghp
    global loss
    global game
    global manna
    global money
    money += random.randint(1,7)
    if manna >= 20:
        vraghp -= mloss
        vh["text"]="❤" + str(vraghp)
        manna -= 20

def lvl():
    damage.place(x=0 , y=0 , height=70 , width=300)
    magic.place(x=300 , y=0 , height=70 , width=300)
    up1.place(x=0 , y=120 , height=40 , width=300)
    up2.place(x=300 , y=120 , height=40 , width=300)
    home.place(x=10 , y=350 , height=40 , width=40)
    coin.place(x=60 , y=350 , height=40 , width=150)
    logo.place_forget()
    play.place_forget()
    lvl.place_forget()
    coin["text"]="⚫" + str(money)
    
def damage():
    stat1.place(x=10 , y=120 , height=50 , width=190)
    proc1.place(x=180 , y=120 , height=50 , width=100)
    plus1.place(x=432 , y=120 , height=50 , width=100)
    price1.place(x=280 , y=120 , height=50 , width=150)
    stat2.place_forget()
    proc2.place_forget()
    plus2.place_forget()
    price2.place_forget()
    up1.place_forget()
    up2.place_forget()
    proc1["text"]=str(p1) + "/15"
    if p1 == 1:
        price1["text"]="⚫250"
    elif p1 == 2:
        price1["text"]="⚫400"
    elif p1 == 3:
        price1["text"]="⚫550"
    elif p1 == 4:
        price1["text"]="⚫700"
    elif p1 == 5:
        price1["text"]="⚫850"
    elif p1 == 6:
        price1["text"]="⚫1000"
    elif p1 == 7:
        price1["text"]="⚫1150"
    elif p1 == 8:
        price1["text"]="⚫1300"
    elif p1 == 9:
        price1["text"]="⚫1450"
    elif p1 == 10:
        price1["text"]="⚫1600"
    elif p1 == 11:
        price1["text"]="⚫1750"
    elif p1 == 12:
        price1["text"]="⚫1900"
    elif p1 == 13:
        price1["text"]="⚫2050"
    elif p1 == 14:
        price1["text"]="⚫2200"
    elif p1 == 15:
        proc1.place(x=180 , y=120 , height=50 , width=150)
        price1.place_forget()
        plus1.place_forget()

def magic():
    stat2.place(x=10 , y=120 , height=50 , width=190)
    proc2.place(x=180 , y=120 , height=50 , width=100)
    plus2.place(x=432 , y=120 , height=50 , width=100)
    price2.place(x=280 , y=120 , height=50 , width=150)
    stat1.place_forget()
    proc1.place_forget()
    plus1.place_forget()
    price1.place_forget()
    up1.place_forget()
    up2.place_forget()
    proc2["text"]=str(p2) + "/15"
    if p2 == 1:
        price2["text"]="⚫350"
    elif p2 == 2:
        price2["text"]="⚫500"
    elif p2 == 3:
        price2["text"]="⚫650"
    elif p2 == 4:
        price2["text"]="⚫800"
    elif p2 == 5:
        price2["text"]="⚫950"
    elif p2 == 6:
        price2["text"]="⚫1100"
    elif p2 == 7:
        price2["text"]="⚫1250"
    elif p2 == 8:
        price2["text"]="⚫1400"
    elif p2 == 9:
        price2["text"]="⚫1550"
    elif p2 == 10:
        price2["text"]="⚫1700"
    elif p2 == 11:
        price2["text"]="⚫1850"
    elif p2 == 12:
        price2["text"]="⚫2000"
    elif p2 == 13:
        price2["text"]="⚫2150"
    elif p1 == 14:
        price1["text"]="⚫2300"
    elif p1 == 15:
        proc2.place(x=180 , y=120 , height=50 , width=150)
        price2.place_forget()
        plus2.place_forget()

def home():
    logo.place(x=2 , y=10 , height=100 , width=600)
    play.place(x=200 , y=170 , height=60 , width=200)
    lvl.place(x=200 , y=240 , height=60 , width=200)
    damage.place_forget()
    magic.place_forget()
    home.place_forget()
    up1.place_forget()
    up2.place_forget()
    stat1.place_forget()
    stat2.place_forget()
    plus1.place_forget()
    plus2.place_forget()
    price1.place_forget()
    price2.place_forget()
    proc1.place_forget()
    proc2.place_forget()
    coin.place_forget()

def plus1():
    global p1
    global money
    global loss
    if p1 == 1:
        if money >= 100:
            money -= 100
            p1 += 1
            loss += 5
            proc1["text"]=str(p1) + "/15"
            price1["text"]="⚫250"
            coin["text"]="⚫" + str(money)
    elif p1 == 2:
        if money >= 250:
            money -= 250
            p1 += 1
            loss += 5
            proc1["text"]=str(p1) + "/15"
            price1["text"]="⚫400"
            coin["text"]="⚫" + str(money)
    elif p1 == 3:
        if money >= 400:
            money -= 400
            p1 += 1
            loss += 5
            proc1["text"]=str(p1) + "/15"
            price1["text"]="⚫550"
            coin["text"]="⚫" + str(money)
    elif p1 == 4:
        if money >= 550:
            money -= 550
            p1 += 1
            loss += 5
            proc1["text"]=str(p1) + "/15"
            price1["text"]="⚫700"
            coin["text"]="⚫" + str(money)
    elif p1 == 5:
        if money >= 700:
            money -= 700
            p1 += 1
            loss += 5
            proc1["text"]=str(p1) + "/15"
            price1["text"]="⚫850"
            coin["text"]="⚫" + str(money)
    elif p1 == 6:
        if money >= 850:
            money -= 850
            p1 += 1
            loss += 5
            proc1["text"]=str(p1) + "/15"
            price1["text"]="⚫1000"
            coin["text"]="⚫" + str(money)
    elif p1 == 7:
        if money >= 1000:
            money -= 1000
            p1 += 1
            loss += 5
            proc1["text"]=str(p1) + "/15"
            price1["text"]="⚫1150"
            coin["text"]="⚫" + str(money)
    elif p1 == 8:
        if money >= 1150:
            money -= 1150
            p1 += 1
            loss += 5
            proc1["text"]=str(p1) + "/15"
            price1["text"]="⚫1300"
            coin["text"]="⚫" + str(money)
    elif p1 == 9:
        if money >= 1300:
            money -= 1300
            p1 += 1
            loss += 5
            proc1["text"]=str(p1) + "/15"
            price1["text"]="⚫1450"
            coin["text"]="⚫" + str(money)
    elif p1 == 10:
        if money >= 1450:
            money -= 1450
            p1 += 1
            loss += 5
            proc1["text"]=str(p1) + "/15"
            price1["text"]="⚫1600"
            coin["text"]="⚫" + str(money)
    elif p1 == 11:
        if money >= 1600:
            money -= 1600
            p1 += 1
            loss += 5
            proc1["text"]=str(p1) + "/15"
            price1["text"]="⚫1750"
            coin["text"]="⚫" + str(money)
    elif p1 == 12:
        if money >= 1750:
            money -= 1750
            p1 += 1
            loss += 5
            proc1["text"]=str(p1) + "/15"
            price1["text"]="⚫1900"
            coin["text"]="⚫" + str(money)
    elif p1 == 13:
        if money >= 1900:
            money -= 1900
            p1 += 1
            loss += 5
            proc1["text"]=str(p1) + "/15"
            price1["text"]="⚫2050"
            coin["text"]="⚫" + str(money)
    elif p1 == 14:
        if money >= 2050:
            money -= 2050
            p1 += 1
            loss += 5
            proc1["text"]=str(p1) + "/15"
            coin["text"]="⚫" + str(money)
            proc1.place(x=180 , y=120 , height=50 , width=150)
            price1.place_forget()
            plus1.place_forget()
            

def plus2():
    global p2
    global money
    global mloss
    chislo = random.randint(5,9)
    if p2 == 1:
        if money >= 200:
            money -= 200
            p2 += 1
            mloss += chislo
            proc2["text"]=str(p2) + "/15"
            price2["text"]="⚫350"
            coin["text"]="⚫" + str(money)
    elif p2 == 2:
        if money >= 350:
            money -= 350
            p2 += 1
            mloss += chislo
            proc2["text"]=str(p2) + "/15"
            price2["text"]="⚫500"
            coin["text"]="⚫" + str(money)
    elif p2 == 3:
        if money >= 500:
            money -= 500
            p2 += 1
            mloss += chislo
            proc2["text"]=str(p2) + "/15"
            price2["text"]="⚫650"
            coin["text"]="⚫" + str(money)
    elif p2 == 4:
        if money >= 650:
            money -= 650
            p2 += 1
            mloss += chislo
            proc2["text"]=str(p2) + "/15"
            price2["text"]="⚫800"
            coin["text"]="⚫" + str(money)
    elif p2 == 5:
        if money >= 800:
            money -= 800
            p2 += 1
            mloss += chislo
            proc2["text"]=str(p2) + "/15"
            price2["text"]="⚫950"
            coin["text"]="⚫" + str(money)
    elif p2 == 6:
        if money >= 950:
            money -= 950
            p2 += 1
            mloss += chislo
            proc2["text"]=str(p2) + "/15"
            price2["text"]="⚫1100"
            coin["text"]="⚫" + str(money)
    elif p2 == 7:
        if money >= 1100:
            money -= 1100
            p2 += 1
            mloss += chislo
            proc2["text"]=str(p2) + "/15"
            price2["text"]="⚫1250"
            coin["text"]="⚫" + str(money)
    elif p2 == 8:
        if money >= 1250:
            money -= 1250
            p2 += 1
            mloss += chislo
            proc2["text"]=str(p2) + "/15"
            price2["text"]="⚫1400"
            coin["text"]="⚫" + str(money)
    elif p2 == 9:
        if money >= 1400:
            money -= 1400
            p2 += 1
            mloss += chislo
            proc2["text"]=str(p2) + "/15"
            price2["text"]="⚫1550"
            coin["text"]="⚫" + str(money)
    elif p2 == 10:
        if money >= 1550:
            money -= 1550
            p2 += 1
            mloss += chislo
            proc2["text"]=str(p2) + "/15"
            price2["text"]="⚫1700"
            coin["text"]="⚫" + str(money)
    elif p2 == 11:
        if money >= 1700:
            money -= 1700
            p2 += 1
            mloss += chislo
            proc2["text"]=str(p2) + "/15"
            price2["text"]="⚫1850"
            coin["text"]="⚫" + str(money)
    elif p2 == 12:
        if money >= 1850:
            money -= 1850
            p2 += 1
            mloss += chislo
            proc2["text"]=str(p2) + "/15"
            price2["text"]="⚫2000"
            coin["text"]="⚫" + str(money)
    elif p2 == 13:
        if money >= 2000:
            money -= 2000
            p2 += 1
            mloss += chislo
            proc2["text"]=str(p2) + "/15"
            price2["text"]="⚫2150"
            coin["text"]="⚫" + str(money)
    elif p2 == 14:
        if money >= 2150:
            money -= 2150
            p2 += 1
            mloss += 5
            proc2["text"]=str(p2) + "/15"
            coin["text"]="⚫" + str(money)
            proc2.place(x=180 , y=120 , height=50 , width=150)
            price2.place_forget()
            plus2.place_forget()

# root.attributes("-alpha", 0.5)

root = Tk()
root.title('Sage Sword')
# root.iconbitmap("icon.ico")
root.geometry('600x400')
root.resizable(width=False , height=False)
root['bg']='white'

# bgimg = PhotoImage(file="bg.png")
# bg = Label(root , image=bgimg)
# bg.place(x=-2 , y=-2)

play = Button(root , text="Play" , font=("arial black",25) , bg="black" , fg="white" , command=play)
lvl = Button(root , text="LvL UP" , font=("arial black",25) , bg="black" , fg="white" , command=lvl)

damage = Button(root , text="Damage" , font=("arial black",25) , bg="black" , fg="white" , command=damage)
magic = Button(root , text="Magic" , font=("arial black",25) , bg="black" , fg="white" , command=magic)

home = Button(root , text="🏠" , font="intro 20", bg="black" , fg="white" , command=home)
back = Button(root , text="Back" , font=("arial black",25) , bg="black" , fg="white" , command=back)

plus1 = Button(root , text="+" , font="intro 25", bg="black" , fg="white" , command=plus1)
plus2 = Button(root , text="+" , font="intro 25", bg="black" , fg="white" , command=plus2)

attack = Button(root , text="⚔" , font="intro 45", bg="black" , fg="white" , command=attack)
mattack = Button(root , text="🔥" , font="intro 45", bg="black" , fg="white" , command=mattack)

stat1 = Label(root , text="Damage" , font=("arial black",25) , bg="black" , fg="white")
stat2 = Label(root , text="Magic" , font=("arial black",25) , bg="black" , fg="white")

price1 = Label(root , text="" , font=("arial black",25) , bg="black" , fg="white")
price2 = Label(root , text="" , font=("arial black",25) , bg="black" , fg="white")

proc1 = Label(root , text="" , font=("arial black",25) , bg="black" , fg="white")
proc2 = Label(root , text="" , font=("arial black",25) , bg="black" , fg="white")

coin = Label(root , text="" , font="intro 20" ,bg="black" , fg="white")

up1 = Label(root , text="↑" , font="intro 25" , bg="white" , fg="black")
up2 = Label(root , text="↑" , font="intro 25" , bg="white" , fg="black")

vrag = Label(root , text="" , font="intro 25" , bg="#FDD9B5" , fg="#FDD9B5")
eye = Label(root , text="⚫⚫" , font="intro 19" , bg="#FDD9B5" , fg="black")
vh = Label(root , text="" , font="intro 19" , bg="white" , fg="black")
win = Label(root , text="WIN!" , font=("arial black",50) , bg="white" , fg="black")

logo = Label(root , text="Sage Sword" , font=("arial black",50) ,bg="white" , fg="black")

logo.place(x=2 , y=10 , height=100 , width=600)

play.place(x=200 , y=170 , height=60 , width=200)
lvl.place(x=200 , y=240 , height=60 , width=200)

root.mainloop()