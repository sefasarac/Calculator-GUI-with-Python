from graphics import *
operand = ""
operandClicked=False
sonuc,sayi1=0,0
# https://github.com/sefasarac
def resetAC(textBox:Entry):
    global sonuc,sayi1,operand,operandClicked
    sonuc=0
    sayi1=0
    operand=""
    operandClicked=False
    textBox.setText("0")

def hesapla(operand:str,yazili,textbox:Entry):
    global sayi1
    if(sayi1!=0):
        sayi1,yazili=int(float(sayi1)),int(float(yazili))
        if(operand=="+"):
            sonuc=sayi1+yazili
            textbox.setText(str(sonuc))
            sayi1=sonuc
        elif(operand == "-"):
            sonuc=sayi1-yazili
            textbox.setText(str(sonuc))
            sayi1=sonuc
        elif(operand == "/"):
            sonuc=sayi1/yazili
            textbox.setText(str(sonuc))
            sayi1=sonuc
        elif(operand == "x"):
            sonuc=sayi1*yazili
            textbox.setText(str(sonuc))
            sayi1=sonuc
        elif(operand == "**"):
            sonuc=sayi1**yazili
            textbox.setText(str(sonuc))
            sayi1=sonuc
        elif(operand == "%"):
            sonuc=sayi1%yazili
            textbox.setText(str(sonuc))
            sayi1=sonuc
        elif(operand=="="):
            return

def yaziGoster(tiklanan:str,textbox:Entry):
    global operand,operandClicked,sonuc,sayi1
    if(operandClicked==True):
        if(tiklanan=="+" or tiklanan=="-" or tiklanan=="x" or tiklanan=="/" or tiklanan=="**" or tiklanan=="%" or tiklanan=="="):
            resetAC(textbox)
            return
        textbox.setText("")
        operandClicked=False
    yazili=textbox.getText()
    if(tiklanan.isnumeric()):
        if(tiklanan=="0" and yazili=="0"):
            return
        if(yazili=="0"):
            yazili=""
        if(len(yazili)==20):
            return
        yazili+=tiklanan
        textbox.setText(yazili)
    elif( tiklanan=="+"):
        hesapla(operand,yazili,textbox)
        sayi1=int(float(textbox.getText()))
        operand="+"
        operandClicked=True
        return
    elif( tiklanan=="-"):
        hesapla(operand,yazili,textbox)
        sayi1=int(float(textbox.getText()))
        operand="-"
        operandClicked=True
        return
    elif( tiklanan=="/"):
        hesapla(operand,yazili,textbox)
        sayi1=int(float(textbox.getText()))
        operand="/"
        operandClicked=True
        return
    elif( tiklanan=="x"):
        hesapla(operand,yazili,textbox)
        sayi1=int(float(textbox.getText()))
        operand="x"
        operandClicked=True
        return
    elif( tiklanan=="**"):
        hesapla(operand,yazili,textbox)
        sayi1=int(float(textbox.getText()))
        operand="**"
        operandClicked=True
        return
    elif( tiklanan=="%"):
        hesapla(operand,yazili,textbox)
        sayi1=int(float(textbox.getText()))
        operand="%"
        operandClicked=True
        return
    elif( tiklanan=="AC"):
        resetAC(textbox)
    elif( tiklanan=="+/-"):
        tersi = int(float(textbox.getText()))
        textbox.setText(tersi*-1)
    elif( tiklanan=="="):
        hesapla(operand,yazili,textbox)
        operand="="
        operandClicked=False

def main():
    win = GraphWin("Calculator", 600, 600)
    tbox = Entry(Point(290,50),23)
    tbox.setText("0")
    tbox.draw(win)
    pixelVirtual=tk.PhotoImage(width=1, height=1)
    btn_AC = tk.Button(win,text="AC",image=pixelVirtual,height=100,width=150,compound="c",command=lambda: yaziGoster("AC",tbox) )
    btn_AC.place(x=0,y=100)
    btn_degistirici=tk.Button(win,text="+/-",image=pixelVirtual,height=100,width=150,compound="c",command=lambda: yaziGoster("+/-",tbox))
    btn_degistirici.place(x=150,y=100)
    btn_modulus=tk.Button(win,text="%",image=pixelVirtual,height=100,width=150,compound="c",command=lambda: yaziGoster("%",tbox))
    btn_modulus.place(x=300,y=100)
    btn_division=tk.Button(win,text="/",image=pixelVirtual,height=100,width=150,compound="c",command=lambda: yaziGoster("/",tbox))
    btn_division.place(x=450,y=100)
    btn_seven=tk.Button(win,text="7",image=pixelVirtual,height=100,width=150,compound="c",command=lambda: yaziGoster("7",tbox))
    btn_seven.place(x=0,y=200)
    btn_eight=tk.Button(win,text="8",image=pixelVirtual,height=100,width=150,compound="c",command=lambda: yaziGoster("8",tbox))
    btn_eight.place(x=150,y=200)
    btn_nine=tk.Button(win,text="9",image=pixelVirtual,height=100,width=150,compound="c",command=lambda: yaziGoster("9",tbox))
    btn_nine.place(x=300,y=200)
    btn_multiplacition=tk.Button(win,text="x",image=pixelVirtual,height=100,width=150,compound="c",command=lambda: yaziGoster("x",tbox))
    btn_multiplacition.place(x=450,y=200)
    btn_four=tk.Button(win,text="4",image=pixelVirtual,height=100,width=150,compound="c",command=lambda: yaziGoster("4",tbox))
    btn_four.place(x=0,y=300)
    btn_five=tk.Button(win,text="5",image=pixelVirtual,height=100,width=150,compound="c",command=lambda: yaziGoster("5",tbox))
    btn_five.place(x=150,y=300)
    btn_six=tk.Button(win,text="6",image=pixelVirtual,height=100,width=150,compound="c",command=lambda: yaziGoster("6",tbox))
    btn_six.place(x=300,y=300)
    btn_abstraction=tk.Button(win,text="-",image=pixelVirtual,height=100,width=150,compound="c",command=lambda: yaziGoster("-",tbox))
    btn_abstraction.place(x=450,y=300)
    btn_one=tk.Button(win,text="1",image=pixelVirtual,height=100,width=150,compound="c",command=lambda: yaziGoster("1",tbox))
    btn_one.place(x=0,y=400)
    btn_two=tk.Button(win,text="2",image=pixelVirtual,height=100,width=150,compound="c",command=lambda: yaziGoster("2",tbox))
    btn_two.place(x=150,y=400)
    btn_three=tk.Button(win,text="3",image=pixelVirtual,height=100,width=150,compound="c",command=lambda: yaziGoster("3",tbox))
    btn_three.place(x=300,y=400)
    btn_sum=tk.Button(win,text="+",image=pixelVirtual,height=100,width=150,compound="c",command=lambda: yaziGoster("+",tbox))
    btn_sum.place(x=450,y=400)
    btn_zero=tk.Button(win,text="0",image=pixelVirtual,height=100,width=300,compound="c",command=lambda: yaziGoster("0",tbox))
    btn_zero.place(x=0,y=500)
    btn_exponentiation=tk.Button(win,text="**",image=pixelVirtual,height=100,width=150,compound="c",command=lambda: yaziGoster("**",tbox))
    btn_exponentiation.place(x=300,y=500)
    btn_equal=tk.Button(win,text="=",image=pixelVirtual,height=100,width=150,compound="c",command=lambda: yaziGoster("=",tbox))
    btn_equal.place(x=450,y=500)
    win.getMouse()
    win.close()  
main()
# https://github.com/sefasarac