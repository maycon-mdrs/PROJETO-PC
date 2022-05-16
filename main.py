from tkinter import*
from tkinter import ttk
import os

#Importar imagens(os)
pastaApp=os.path.dirname(__file__)

#Interface do app
app=Tk()
app.title("Easy IMC")
app.geometry("700x600")
app.configure(background="#006666")

#Importar imagem(tabela)
imgTabela=PhotoImage(file=pastaApp+"tabela.png")

#Interface gráfica
lay=Label(app,background= "#ebebeb")
lay.place(x=35, y=35, width=625, height= 525)

#Listas para armazenar os dados(altura, peso e imc)
#24 - 35

lJaneiro=[]
lFevereiro=[]
lMarço=[]
lAbril=[]
lMaio=[]
lJunho=[]
lJulho=[]
lAgosto=[]
lSetembro=[]
lOutubro=[]
lNovembro=[]
lDezembro=[]

listMeses= ["Janeiro", "Fevereiro","Março","Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro" ,"Novembro", "Dezembro"]

#Função para imprimir os dados armazenados de cada mês(if para lista em branco; else para lista preenchida)
#42 - 365

def consultas():
  if cb_cmes.get() == "Janeiro":
    if lJaneiro == []:
      txtcm=Label(app, text=("janeiro"),background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app, text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app, text=("---"),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app, text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)
    else:
      txtcm=Label(app, text=(" Janeiro"),background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app, text=(lJaneiro[0],"m"),background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app, text=(lJaneiro[1],"kg"),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app, text=("{:.2f}".format(lJaneiro[2])),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)

  elif cb_cmes.get() == "Fevereiro":
    if lFevereiro == []:
      txtcm=Label(app, text=("Fevereiro"),background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app, text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app, text=("---"),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app, text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)
    else:
      txtcm=Label(app, text=(" Fevereiro"),background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app, text=(lFevereiro[0],"m"),background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app, text=(lFevereiro[1],"kg"),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app, text=("{:.2f}".format(lFevereiro[2])),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)

  elif cb_cmes.get() == "Março":
    if lMarço == []:
      txtcm=Label(app,text=("Março"), background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app,text=("---"),background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app, text=("---"),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app,text=("---"),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)
    else:
      txtcm=Label(app, text=(" Março"),background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app, text=(lMarço[0],"m"),background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app, text=(lMarço[1],"kg"),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app, text=("{:.2f}".format(lMarço[2])),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)

  elif cb_cmes.get() == "Abril":
    if lAbril == []:
      txtcm=Label(app,text=("Abrul"), background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)
    else:
      txtcm=Label(app, text=(" Abril"),background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app, text=(lAbril[0],"m"),background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app, text=(lAbril[1],"kg"),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app, text=("{:.2f}".format(lAbril[2])),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)

  elif cb_cmes.get() == "Maio":
    if lMaio == []:
      txtcm=Label(app,text=("Maio"), background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app,text=("---"),background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)
    else:
      txtcm=Label(app, text=(" Maio"),background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app, text=(lMaio[0],"m"),background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app, text=(lMaio[1],"kg"),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app, text=("{:.2f}".format(lMaio[2])),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)

  elif cb_cmes.get() == "Junho":
    if lJunho == []:
      txtcm=Label(app,text=("Junho"), background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)
    else:
      txtcm=Label(app, text=(" Junho"),background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app, text=(lJunho[0],"m"),background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app, text=(lJunho[1],"kg"),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app, text=("{:.2f}".format(lJunho[2])),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)
      
  elif cb_cmes.get() == "Julho":
    if lJulho == []:
      txtcm=Label(app, text=("Julho"),background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app, text=("---"),background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)
    else:
      txtcm=Label(app, text=(" Julho"),background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app, text=(lJulho[0],"m"),background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app, text=(lJulho[1],"kg"),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app, text=("{:.2f}".format(lJulho[2])),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20) 

  elif cb_cmes.get() == "Agosto":
    if lAgosto == []:
      txtcm=Label(app,text=("Agosto"), background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app, text=("---"),background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app, text=("---"),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app, text=("---"),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)
    else:
      txtcm=Label(app, text=(" Agosto"),background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app, text=(lAgosto[0],"m"),background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app, text=(lAgosto[1],"kg"),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app, text=("{:.2f}".format(lAgosto[2])),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)   

  elif cb_cmes.get() == "Setembro":
    if lSetembro == []:
      txtcm=Label(app, text=("Setembro"),background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)
    else:
      txtcm=Label(app, text=(" Setembro"),background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app, text=(lSetembro[0],"m"),background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app, text=(lSetembro[1],"kg"),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app, text=("{:.2f}".format(lSetembro[2])),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)  

  elif cb_cmes.get() == "Outubro":
    if lOutubro == []:
      txtcm=Label(app,text=("Outubro"), background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)
    else:
      txtcm=Label(app, text=(" Outubro"),background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app, text=(lOutubro[0],"m"),background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app, text=(lOutubro[1],"kg"),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app, text=("{:.2f}".format(lOutubro[2])),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20) 

  elif cb_cmes.get() == "Novembro":
    if lNovembro == []:
      txtcm=Label(app,text=("Novembro"), background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)
    else:
      txtcm=Label(app, text=(" Novembro"),background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app, text=(lNovembro[0],"m"),background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app, text=(lNovembro[1],"kg"),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app, text=("{:.2f}".format(lNovembro[2])),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20) 

  elif cb_cmes.get() == "Dezembro":
    if lDezembro == []:
      txtcm=Label(app,text=("Dezembro"), background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app,text=("---"), background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20)
    else:
      txtcm=Label(app, text=(" Dezembro"),background= "#cdf7f0", foreground= "#212121")
      txtcm.place(x=550, y=255, width=75, height=20)

      txtca=Label(app, text=(lDezembro[0],"m"),background= "#cdf7f0", foreground= "#212121")
      txtca.place(x=550, y=295, width=75, height=20)

      txtcp=Label(app, text=(lDezembro[1],"kg"),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=335, width=75, height=20)

      txtcp=Label(app, text=("{:.2f}".format(lDezembro[2])),background= "#cdf7f0", foreground= "#212121")
      txtcp.place(x=550, y=375, width=75, height=20) 

  txtmesc=Label(app, text="Mês:", background="#32E0C4", foreground="#212121")
  txtmesc.place(x=465,y=255,width=75, height=20)

  txtaltc=Label(app, text="Altura:", background="#32E0C4", foreground="#212121")
  txtaltc.place(x=465,y=295,width=75, height=20) 

  txtpesoc=Label(app, text="Peso:", background="#32E0C4", foreground="#212121")
  txtpesoc.place(x=465,y=335,width=75, height=20) 

  txtimcc=Label(app, text="IMC:", background="#32E0C4", foreground="#212121")
  txtimcc.place(x=465,y=375,width=75, height=20) 

#Função para calcular e imprimir o imc
#370 - 471

def calcular():
  alt = float(altura.get())
  pes = float(peso.get())
  imc = (pes / (alt**2)) 

  #Variações de status para determinado imc
  #378 - 389

  if (imc < 18.5):
    x = "Você está abaixo do peso"
  elif (imc >= 18.6) and (imc <= 24.9):
    x = "Peso ideal"
  elif (imc >= 25.0) and (imc <= 29.9):
    x= "Levemente acima do peso"
  elif (imc >= 30.0) and (imc <= 34.9):
    x = "Obesidade grau I"
  elif (imc >= 35.0) and (imc <= 39.9):
    x = "Obesidade grau II (severa)"
  else:
    x = "Obesidade III (mórbida)"
 
  txtimc=Label(app, text=("O IMC do usuário é: {:.2f}" .format(imc)),background="#ebebeb", foreground="#212121") 
  txtimc.place(x=65, y=195,width=200, height=20)

  txtimc=Label(app, text=(x),background="#ebebeb", foreground="#212121") 
  txtimc.place(x=65, y=215,width=200, height=20)
  
  #Tabela imc
  tabela=Label(app,image=imgTabela)
  tabela.place(x=45,y=255)

  #Comando para armazenar os dados em cada lista(mês)
  #404 - 473

  if cb_mes.get() == "Janeiro":
    lJaneiro.clear()
    lJaneiro.append(alt)
    lJaneiro.append(pes)
    lJaneiro.append(imc)

  elif cb_mes.get() == "Fevereiro":
    lFevereiro.clear()
    lFevereiro.append(alt)
    lFevereiro.append(pes)
    lFevereiro.append(imc)

  elif cb_mes.get() == "Março":
    lMarço.clear()
    lMarço.append(alt)
    lMarço.append(pes)
    lMarço.append(imc)

  elif cb_mes.get() == "Abril":
    lAbril.clear()
    lAbril.append(alt)
    lAbril.append(pes)
    lAbril.append(imc)
  elif cb_mes.get() == "Maio":
    lMaio.clear()
    lMaio.append(alt)
    lMaio.append(pes)
    lMaio.append(imc)

  elif cb_mes.get() == "Junho":
    lJunho.clear()
    lJunho.append(alt)
    lJunho.append(pes)
    lJunho.append(imc)

  elif cb_mes.get() == "Julho":
    lJulho.clear()
    lJulho.append(alt)
    lJulho.append(pes)
    lJulho.append(imc)

  elif cb_mes.get() == "Agosto":
    lAgosto.clear()
    lAgosto.append(alt)
    lAgosto.append(pes)
    lAgosto.append(imc)

  elif cb_mes.get() == "Setembro":
    lSetembro.clear()
    lSetembro.append(alt)
    lSetembro.append(pes)
    lSetembro.append(imc)

  elif cb_mes.get() == "Outubro":
    lOutubro.clear()
    lOutubro.append(alt)
    lOutubro.append(pes)
    lOutubro.append(imc)

  elif cb_mes.get() == "Novembro":
    lNovembro.clear()
    lNovembro.append(alt)
    lNovembro.append(pes)
    lNovembro.append(imc)

  elif cb_mes.get() == "Dezembro":
    lDezembro.clear()
    lDezembro.append(alt)
    lDezembro.append(pes)
    lDezembro.append(imc)


#Interface gráfica

txt1=Label(app, text= "Easy IMC", background= "#32E0C4", foreground= "#212121")
txt1.place(x=45,y=45,width=605,height=50)

txtal=Label(app, text= "Altura(metros):", background= "#32E0C4", foreground="#212121")
txtal.place(x=45, y=115, width=130, height=20)

altura=Entry(app)
altura.place(x=185, y=115, width=100, height=20)

txtpeso=Label(app, text= "Peso(kg):", background= "#32E0C4", foreground="#212121")
txtpeso.place(x=45, y=155, width=130, height=20)

peso=Entry(app)
peso.place(x=185, y=155, width=100, height=20);

cmes=Label(app, text= "Consultar mês:", background= "#32E0C4", foreground = "#212121")
cmes.place(x=365, y=155, width=130, height=20)

Button(app,text="Calcular IMC", command=calcular).place(x=505, y=195,width=100, height=20)

Button(app,text="Realizar consulta", command=consultas).place(x=365, y=195,width=130, height=20)

txtmes=Label(app, text= "Mês:", background= "#32E0C4", foreground="#212121")
txtmes.place(x=365, y=115, width=130, height=20)

cb_mes=ttk.Combobox(app, values=listMeses)
cb_mes.place(x=505, y=115, width=100, height=20) #box dos meses

cb_cmes=ttk.Combobox(app, values=listMeses)
cb_cmes.place(x=505, y=155, width=100, height=20) #box para consulta

app.mainloop()
