from tkinter import *
from tkinter import messagebox
import random,os
import tempfile,smtplib

def clear():
    bathsoapentry.delete(0, 0)
    facecreamentry.delete(0, 0)
    facewashentry.delete(0, 0)
    bodylotionentry.delete(0, 0)
    lipbalmentry.delete(0, 0)
    shampooentry.delete(0, 0)

    wheatentry.delete(0, 0)
    riceentry.delete(0, 0)
    oatsentry.delete(0, 0)
    oliveoilentry.delete(0, 0)
    gheeentry.delete(0, 0),
    sugarentry.delete(0, 0)

    redbullentry.delete(0, 0)
    pepsientry.delete(0, 0)
    cocacolaentry.delete(0, 0)
    monsterentry.delete(0, 0)
    limcaentry.delete(0, 0)
    mountaindewentry.delete(0, 0)


    bathsoapentry.insert(0,0)
    facecreamentry.insert(0,0)
    facewashentry.insert(0,0)
    bodylotionentry.insert(0,0)
    lipbalmentry.insert(0,0)
    shampooentry.insert(0,0)

    wheatentry.insert(0,0)
    riceentry.insert(0,0)
    oatsentry.insert(0,0)
    oliveoilentry.insert(0,0)
    gheeentry.insert(0,0),
    sugarentry.insert(0,0)

    redbullentry.insert(0,0)
    pepsientry.insert(0,0)
    cocacolaentry.insert(0,0)
    monsterentry.insert(0,0)
    limcaentry.insert(0,0)
    mountaindewentry.insert(0,0)

    cosmetictaxentry.delete(0,END)
    grocerytaxentry.delete(0, END)
    beveragestaxentry.delete(0, END)

    cosmeticpriceentry.delete(0,END)
    grocerypriceentry.delete(0,END)
    beveragespriceentry.delete(0,END)

    nameentry.delete(0,END)
    phoneentry.delete(0,END)
    billnumberentry.delete(0,END)

    textarea.delete(1.0,END)

def sendemail():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderentry.get(),passwordentry.get())
            message=email_textarea.get(1.0,END)
            ob.sendmail(senderentry.get(),recieverentry.get(),message)
            ob.quit()
            messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error','Something went wrong, Please try again',parent=root1)
    if textarea.get(1.0, END).strip() == '':
        messagebox.showerror('Error', 'Bill is empty')
    else:
        root1 = Toplevel()
        root1.grab_set()
        root1.title('Send E-Mail')
        root1.config(bg='gray20')
        root1.resizable(0, 0)

        senderframe = LabelFrame(
            root1,
            text='SENDER',
            font=('times new roman', 16, 'bold'),
            bd=6,
            bg='gray20',
            fg='white'
        )
        senderframe.grid(row=0, column=0, padx=40, pady=20)

        senderlabel = Label(
            senderframe,
            text="SENDER's E-MAIL",
            font=('times new roman', 15, 'bold'),
            bg='gray20',
            fg='white'
        )
        senderlabel.grid(row=0, column=0, padx=10, pady=8)

        senderentry = Entry(
            senderframe,
            font=('times new roman', 14, 'bold'),
            bd=4,
            width=20,
            relief=RAISED
        )
        senderentry.grid(row=0, column=1, padx=10, pady=8)

        passwordlabel = Label(
            senderframe,
            text="PASSWORD",
            font=('times new roman', 15, 'bold'),
            bg='gray20',
            fg='white'
        )
        passwordlabel.grid(row=1, column=0, padx=10, pady=8)

        passwordentry = Entry(
            senderframe,
            font=('times new roman', 14, 'bold'),
            bd=4,
            width=20,
            relief=RAISED,
            show='*'
        )
        passwordentry.grid(row=1, column=1, padx=10, pady=8)

        recipientframe = LabelFrame(
            root1,
            text='RECIPIENT',
            font=('times new roman', 16, 'bold'),
            bd=6,
            bg='gray20',
            fg='white'
        )
        recipientframe.grid(row=1, column=0, padx=40, pady=20)

        recieverlabel = Label(
            recipientframe,
            text="E-MAIL",
            font=('times new roman', 15, 'bold'),
            bg='gray20',
            fg='white'
        )
        recieverlabel.grid(row=0, column=0, padx=10, pady=8)

        recieverentry = Entry(
            recipientframe,
            font=('times new roman', 14, 'bold'),
            bd=4,
            width=20,
            relief=RAISED
        )
        recieverentry.grid(row=0, column=1, padx=10, pady=8)

        messagelabel = Label(
            recipientframe,
            text="MESSAGE",
            font=('times new roman', 15, 'bold'),
            bg='gray20',
            fg='white'
        )
        messagelabel.grid(row=1, column=0, padx=10, pady=8, columnspan=2)

        email_textarea = Text(
            recipientframe,
            font=('times new roman', 15, 'bold'),
            bd=2,
            relief=RAISED,
            width=40,
            height=12
        )
        email_textarea.grid(row=2, column=0, columnspan=2, padx=10, pady=8)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('-',''))


        sendbutton=Button(
            root1,
            text='SEND',
            font=('times new roman',16,'bold'),
            width=15,
            command=send_gmail
        )
        sendbutton.grid(row=2,column=0,pady=20)
        root1.mainloop()


def printbill():
    if textarea.get(1.0, END).strip() == '':
        messagebox.showerror('Error', 'Bill is empty')
    else:
        file = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
        with open(file.name, 'w') as f:
            f.write(textarea.get(1.0, END))
        try:
            os.startfile(file.name, 'print')
        except Exception as e:
            messagebox.showerror('Print Error', f'Could not print: {e}')

def searchbill():
    found = False
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnumberentry.get():
            with open(f'bills/{i}', 'r') as f:
                textarea.delete(1.0, END)
                textarea.insert(END, f.read())
            found = True
            break
    if not found:
        messagebox.showerror('Error', 'Invalid Bill Number')

def savebill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill')
    if result:
        billcontent=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(billcontent)
        file.close()
        messagebox.showinfo('Success',f'Bill Number {billnumber} is saved successfully')
billnumber=random.randint(500,1000)

def total():
    global soapprice,facecreamprice,facewashprice,shampooprice,bodylotionprice,lipbalmprice,riceprice,oliveoilprice,oatsprice,wheatprice,gheeprice,sugarprice,cocacolaprice,limcaprice,pepsiprice,monsterenergyprice,redbullprice,mountaindewprice,totalbill
    #COSMETICS PRICE EVALUATION
    soapprice=int(bathsoapentry.get())*80
    facecreamprice=int(facecreamentry.get())*140
    facewashprice=int(facewashentry.get())*210
    shampooprice=int(shampooentry.get())*40
    bodylotionprice=int(bodylotionentry.get())*350
    lipbalmprice=int(lipbalmentry.get())*20

    totalcosmeticprice=soapprice+facecreamprice+facewashprice+shampooprice+bodylotionprice+lipbalmprice
    cosmeticpriceentry.delete(0,END)
    cosmeticpriceentry.insert(0,f"{totalcosmeticprice} Rs.")
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxentry.delete(0,END)
    cosmetictaxentry.insert(0,f"{cosmetictax} Rs")

    #GROCERY PRICE EVALUATION
    riceprice=int(riceentry.get())*65
    oliveoilprice=int(oliveoilentry.get())*650
    oatsprice=int(oatsentry.get())*170
    wheatprice=int(wheatentry.get())*110
    gheeprice=int(gheeentry.get())*275
    sugarprice=int(sugarentry.get())*60

    totalgroceryprice=riceprice+oliveoilprice+oatsprice+wheatprice+gheeprice+sugarprice
    grocerypriceentry.delete(0, END)
    grocerypriceentry.insert(0, f"{totalgroceryprice} Rs.")
    grocerytax = totalgroceryprice * 0.05
    grocerytaxentry.delete(0, END)
    grocerytaxentry.insert(0, f"{grocerytax} Rs")

    #BEVERAGES PRICE EVALUATION
    cocacolaprice=int(cocacolaentry.get())*40
    limcaprice=int(limcaentry.get())*20
    pepsiprice=int(pepsientry.get())*75
    mountaindewprice=int(mountaindewentry.get())*40
    monsterenergyprice=int(monsterentry.get())*160
    redbullprice=int(redbullentry.get())*120

    totalbeveragesprice=cocacolaprice+limcaprice+pepsiprice+mountaindewprice+monsterenergyprice+redbullprice
    beveragespriceentry.delete(0, END)
    beveragespriceentry.insert(0, f"{totalbeveragesprice} Rs.")
    beveragestax = totalbeveragesprice * 0.08
    beveragestaxentry.delete(0, END)
    beveragestaxentry.insert(0, f"{beveragestax} Rs")

    totalbill=totalcosmeticprice+totalgroceryprice+totalbeveragesprice+cosmetictax+grocerytax+beveragestax
def billarea():
    textarea.delete(1.0,END)
    if nameentry.get()=='' or phoneentry.get()=='':
        messagebox.showerror('Error!','Customer Details Are Required')
    elif cosmeticpriceentry.get()=='' and grocerypriceentry.get()=='' and beveragespriceentry.get()=='':
        messagebox.showerror('Error!','No Products Are Selected')
    elif cosmeticpriceentry.get()=='0 Rs.' and grocerypriceentry.get()=='0 Rs.' and beveragespriceentry.get()=='0 Rs.':
        messagebox.showerror('Error!','No Products Are Selected')
    else:
        textarea.insert(END,'\t\t** WELCOME CUSTOMER **')
        textarea.insert(END,f'\nBILL NUMBER : {billnumber}')
        textarea.insert(END, f'\nCUSTOMER NAME : {nameentry.get()}')
        textarea.insert(END, f'\nPHONE NUMBER : {phoneentry.get()}')
        textarea.insert(END, '\n-------------------------------------------------------')
        textarea.insert(END, 'PRODUCT\t\tQUANTITY\t\tPRICE')
        textarea.insert(END, '\n-------------------------------------------------------')

        #COSMETICS

        if int(bathsoapentry.get())!=0:
            textarea.insert(END,f'\nBATH SOAP\t\t{bathsoapentry.get()}\t\t{soapprice} Rs.')
        if int(facecreamentry.get())!=0:
            textarea.insert(END,f'\nFACE CREAM\t\t{facecreamentry.get()}\t\t{facecreamprice} Rs.')
        if int(facewashentry.get())!=0:
            textarea.insert(END,f'\nFACE WASH\t\t{facewashentry.get()}\t\t{facewashprice} Rs.')
        if int(shampooentry.get())!=0:
            textarea.insert(END,f'\nSHAMPOO\t\t{shampooentry.get()}\t\t{shampooprice} Rs.')
        if int(bodylotionentry.get())!=0:
            textarea.insert(END,f'\nBODY LOTION\t\t{bathsoapentry.get()}\t\t{bodylotionprice} Rs.')
        if int(lipbalmentry.get())!=0:
            textarea.insert(END,f'\nLIP BALM\t\t{lipbalmentry.get()}\t\t{lipbalmprice} Rs.')

        #GROCERY

        if int(riceentry.get())!=0:
            textarea.insert(END,f'\nRICE\t\t{riceentry.get()}\t\t{riceprice} Rs.')
        if int(oliveoilentry.get())!=0:
            textarea.insert(END,f'\nOLIVE OIL\t\t{oliveoilentry.get()}\t\t{oliveoilprice} Rs.')
        if int(oatsentry.get()) != 0:
                textarea.insert(END, f'\nOATS\t\t{oatsentry.get()}\t\t{oatsprice} Rs.')
        if int(wheatentry.get())!=0:
            textarea.insert(END,f'\nWHEAT\t\t{wheatentry.get()}\t\t{wheatprice} Rs.')
        if int(gheeentry.get())!=0:
            textarea.insert(END,f'\nGHEE\t\t{gheeentry.get()}\t\t{gheeprice} Rs.')
        if int(sugarentry.get())!=0:
            textarea.insert(END,f'\nSUGAR\t\t{sugarentry.get()}\t\t{sugarprice} Rs.')

        #BEVERAGES

        if int(cocacolaentry.get())!=0:
            textarea.insert(END,f'\nCOCA COLA\t\t{cocacolaentry.get()}\t\t{cocacolaprice} Rs.')
        if int(limcaentry.get())!=0:
            textarea.insert(END,f'\nLIMCA\t\t{limcaentry.get()}\t\t{limcaprice} Rs.')
        if int(pepsientry.get()) != 0:
                textarea.insert(END, f'\nPEPSI\t\t{pepsientry.get()}\t\t{pepsiprice} Rs.')
        if int(mountaindewentry.get())!=0:
            textarea.insert(END,f'\nMOUNTAIN DEW\t\t{mountaindewentry.get()}\t\t{mountaindewprice} Rs.')
        if int(monsterentry.get())!=0:
            textarea.insert(END,f'\nMONSTER ENERGY\t\t{monsterentry.get()}\t\t{monsterenergyprice} Rs.')
        if int(redbullentry.get())!=0:
            textarea.insert(END,f'\nRED BULL\t\t{redbullentry.get()}\t\t{redbullprice} Rs.')

        textarea.insert(END, '\n-------------------------------------------------------')

        if cosmetictaxentry.get()!='0.0 Rs.':
            textarea.insert(END,f"\nCOSMETIC TAX :\t\t{cosmetictaxentry.get()}")
        if grocerytaxentry.get() != '0.0 Rs.':
                textarea.insert(END, f"\nGROCERY TAX :\t\t{grocerytaxentry.get()}")
        if beveragestaxentry.get() != '0.0 Rs.':
                textarea.insert(END, f"\nBEVERAGES TAX :\t\t{beveragestaxentry.get()}")

        textarea.insert(END,f"\nTOTAL BILL :\t\t{totalbill}")

        textarea.insert(END, '\n-------------------------------------------------------')

        savebill()
root=Tk()
root.title('Retail Billing System')
root.geometry('1270x685')
root.iconbitmap('icon.ico')
headinglabel=Label(
    root,
    text='Retail Billing System',
    font=('times new roman',30,'bold'),
    bg='gray10',
    fg='gold',
    bd=10,
    relief=RAISED)
headinglabel.pack(fill=X,pady=10)
customer_details_frame=LabelFrame(
    root,
    text='Customer Details',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='gold',
    bd=8,
    relief=RAISED)
customer_details_frame.pack(fill=X)

namelabel=Label(
    customer_details_frame,
    text='Name',
    font=('times new roman',15,'bold')
    ,bg='gray10',
    fg='white')
namelabel.grid(row=0,column=0,padx=20)

nameentry=Entry(
    customer_details_frame,
    font=('times new roman',15),
    bd=8,
    width=18
)
nameentry.grid(row=0,column=1,padx=8)

phonelabel=Label(
    customer_details_frame,
    text='Phone No.',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white')
phonelabel.grid(row=0,column=2,padx=20,pady=4)

phoneentry=Entry(
    customer_details_frame,
    font=('times new roman',15),
    bd=8,
    width=18
)
phoneentry.grid(row=0,column=3,padx=8)

billnumberlabel=Label(
    customer_details_frame,
    text='Bill No.',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white')
billnumberlabel.grid(row=0,column=4,padx=20,pady=4)

billnumberentry=Entry(
    customer_details_frame,
    font=('times new roman',15),
    bd=8,
    width=18
)
billnumberentry.grid(row=0,column=5,padx=8)

searchButton=Button(
    customer_details_frame,
    text='SEARCH',
    font=('times new roman',15,'bold'),
    bd=6,
    command=searchbill
)
searchButton.grid(row=0,column=8,padx=12,pady=8)

productsframe=Frame(root)
productsframe.pack()

cosmeticsframe=LabelFrame(
    productsframe,
    text='Cosmetics',
    font=('times new roman', 15, 'bold'),
    bg='gray10',
    fg='gold',
    bd=8,
    relief=RAISED
)
cosmeticsframe.grid(row=0,column=0,pady=6)

bathsoaplabel=Label(
    cosmeticsframe,
    text='Bath Soap',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
bathsoaplabel.grid(row=0,column=0,padx=8,pady=6,sticky='w')
bathsoapentry=Entry(
    cosmeticsframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
bathsoapentry.grid(row=0,column=1,pady=6,padx=8)
bathsoapentry.insert(0,0)

facecreamlabel=Label(
    cosmeticsframe,
    text='Face Cream',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
facecreamlabel.grid(row=1,column=0,pady=6,padx=8,sticky='w')

facecreamentry=Entry(
    cosmeticsframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
facecreamentry.grid(row=1,column=1,pady=6,padx=8)
facecreamentry.insert(0,0)

facewashlabel=Label(
    cosmeticsframe,
    text='Face Wash',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
facewashlabel.grid(row=2,column=0,pady=6,padx=8,sticky='w')

facewashentry=Entry(
    cosmeticsframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
facewashentry.grid(row=2,column=1,pady=6,padx=8,sticky='w')
facewashentry.insert(0,0)

shampoolabel=Label(
    cosmeticsframe,
    text='Shampoo',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
shampoolabel.grid(row=3,column=0,pady=6,padx=8,sticky='w')

shampooentry=Entry(
    cosmeticsframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
shampooentry.grid(row=3,column=1,pady=6,padx=8,sticky='w')
shampooentry.insert(0,0)

bodylotionlabel=Label(
    cosmeticsframe,
    text='Body Lotion',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
bodylotionlabel.grid(row=4,column=0,pady=6,padx=8,sticky='w')

bodylotionentry=Entry(
    cosmeticsframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
bodylotionentry.grid(row=4,column=1,pady=6,padx=8,sticky='w')
bodylotionentry.insert(0,0)

lipbalmlabel=Label(
    cosmeticsframe,
    text='Lip Balm',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
lipbalmlabel.grid(row=5,column=0,pady=6,padx=8,sticky='w')

lipbalmentry=Entry(
    cosmeticsframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
lipbalmentry.grid(row=5,column=1,pady=6,padx=8,sticky='w')
lipbalmentry.insert(0,0)

groceryframe=LabelFrame(
    productsframe,
    text='Grocery',
    font=('times new roman', 15, 'bold'),
    bg='gray10',
    fg='gold',
    bd=8,
    relief=RAISED
)
groceryframe.grid(row=0,column=1,pady=6)

ricelabel=Label(
    groceryframe,
    text='Rice',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
ricelabel.grid(row=0,column=0,pady=6,padx=8,sticky='w')

riceentry=Entry(
    groceryframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
riceentry.grid(row=0,column=1,pady=6,padx=8,sticky='w')
riceentry.insert(0,0)

oliveoillabel=Label(
    groceryframe,
    text='Olive Oil',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
oliveoillabel.grid(row=1,column=0,pady=6,padx=8,sticky='w')

oliveoilentry=Entry(
    groceryframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
oliveoilentry.grid(row=1,column=1,pady=6,padx=8,sticky='w')
oliveoilentry.insert(0,0)

oatslabel=Label(
    groceryframe,
    text='Oats',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
oatslabel.grid(row=2,column=0,pady=6,padx=8,sticky='w')

oatsentry=Entry(
    groceryframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
oatsentry.grid(row=2,column=1,pady=6,padx=8,sticky='w')
oatsentry.insert(0,0)

wheatlabel=Label(
    groceryframe,
    text='Wheat',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
wheatlabel.grid(row=3,column=0,pady=6,padx=8,sticky='w')

wheatentry=Entry(
    groceryframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
wheatentry.grid(row=3,column=1,pady=6,padx=8,sticky='w')
wheatentry.insert(0,0)

gheelabel=Label(
    groceryframe,
    text='Ghee',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
gheelabel.grid(row=4,column=0,pady=6,padx=8,sticky='w')

gheeentry=Entry(
    groceryframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
gheeentry.grid(row=4,column=1,pady=6,padx=8,sticky='w')
gheeentry.insert(0,0)

sugarlabel=Label(
    groceryframe,
    text='Sugar',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
sugarlabel.grid(row=5,column=0,pady=6,padx=8,sticky='w')

sugarentry=Entry(
    groceryframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
sugarentry.grid(row=5,column=1,pady=6,padx=8,sticky='w')
sugarentry.insert(0,0)

beveragesframe=LabelFrame(
    productsframe,
    text='Beverages',
    font=('times new roman', 15, 'bold'),
    bg='gray10',
    fg='gold',
    bd=8,
    relief=RAISED
)
beveragesframe.grid(row=0,column=2,pady=6)

cocacolalabel=Label(
    beveragesframe,
    text='Coca Cola',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
cocacolalabel.grid(row=0,column=0,pady=6,padx=8,sticky='w')

cocacolaentry=Entry(
    beveragesframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
cocacolaentry.grid(row=0,column=1,pady=6,padx=8,sticky='w')
cocacolaentry.insert(0,0)

limcalabel=Label(
    beveragesframe,
    text='Limca',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
limcalabel.grid(row=1,column=0,pady=6,padx=8,sticky='w')

limcaentry=Entry(
    beveragesframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
limcaentry.grid(row=1,column=1,pady=6,padx=8,sticky='w')
limcaentry.insert(0,0)

pepsilabel=Label(
    beveragesframe,
    text='Pepsi',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
pepsilabel.grid(row=2,column=0,pady=6,padx=8,sticky='w')

pepsientry=Entry(
    beveragesframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
pepsientry.grid(row=2,column=1,pady=6,padx=8,sticky='w')
pepsientry.insert(0,0)

mountaindewlabel=Label(
    beveragesframe,
    text='Mountain Dew',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
mountaindewlabel.grid(row=3,column=0,pady=6,padx=8,sticky='w')

mountaindewentry=Entry(
    beveragesframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
mountaindewentry.grid(row=3,column=1,pady=6,padx=8,sticky='w')
mountaindewentry.insert(0,0)

monsterlabel=Label(
    beveragesframe,
    text='Monster Energy',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
monsterlabel.grid(row=4,column=0,pady=6,padx=8,sticky='w')

monsterentry=Entry(
    beveragesframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
monsterentry.grid(row=4,column=1,pady=6,padx=8,sticky='w')
monsterentry.insert(0,0)

redbulllabel=Label(
    beveragesframe,
    text='Red Bull',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
redbulllabel.grid(row=5,column=0,pady=6,padx=8,sticky='w')

redbullentry=Entry(
    beveragesframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
redbullentry.grid(row=5,column=1,pady=6,padx=8,sticky='w')
redbullentry.insert(0,0)

billframe=Frame(productsframe,bd=8,relief=RAISED)
billframe.grid(row=0,column=3)

billarealabel=Label(
    billframe,
    text='Billing Area',
    font=('times new roman',15,'bold'),
    bd=8,
    relief=RAISED
)
billarealabel.pack(fill=X)
scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=17,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuframe=LabelFrame(
    root,
    text='Bill Menu',
    font=('times new roman', 15, 'bold'),
    bg='gray10',
    fg='gold',
    bd=8,
    relief=RAISED
)
billmenuframe.pack()

cosmeticpricelabel=Label(
    billmenuframe,
    text='Cosmetic Price',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
cosmeticpricelabel.grid(row=0,column=0,pady=6,padx=8,sticky='w')
cosmeticpriceentry=Entry(
    billmenuframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
cosmeticpriceentry.grid(row=0,column=1,pady=6,padx=8,sticky='w')

grocerypricelabel=Label(
    billmenuframe,
    text='Grocery Price',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
grocerypricelabel.grid(row=1,column=0,pady=6,padx=8,sticky='w')
grocerypriceentry=Entry(
    billmenuframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
grocerypriceentry.grid(row=1,column=1,pady=6,padx=8,sticky='w')

beveragespricelabel=Label(
    billmenuframe,
    text='Cosmetic Price',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
beveragespricelabel.grid(row=2,column=0,pady=6,padx=8,sticky='w')
beveragespriceentry=Entry(
    billmenuframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
beveragespriceentry.grid(row=2,column=1,pady=6,padx=8,sticky='w')

cosmetictaxlabel=Label(
    billmenuframe,
    text='Cosmetic Tax',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
cosmetictaxlabel.grid(row=0,column=2,pady=6,padx=8,sticky='w')
cosmetictaxentry=Entry(
    billmenuframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
cosmetictaxentry.grid(row=0,column=3,pady=6,padx=8,sticky='w')

grocerytaxlabel=Label(
    billmenuframe,
    text='Grocery Tax',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
grocerytaxlabel.grid(row=1,column=2,pady=6,padx=8,sticky='w')
grocerytaxentry=Entry(
    billmenuframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
grocerytaxentry.grid(row=1,column=3,pady=6,padx=8,sticky='w')

beveragestaxlabel=Label(
    billmenuframe,
    text='Beverages Tax',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white'
)
beveragestaxlabel.grid(row=2,column=2,pady=6,padx=8,sticky='w')
beveragestaxentry=Entry(
    billmenuframe,
    font=('times new roman',15,'bold'),
    width=10,
    bd=6
)
beveragestaxentry.grid(row=2,column=3,pady=6,padx=8,sticky='w')

buttonframe=Frame(billmenuframe,bd=8,relief=RAISED)
buttonframe.grid(row=0,column=4,rowspan=3)

totalbutton=Button(
    buttonframe,
    text='Total',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white',
    bd=8,
    width=8,
    pady=8,
    command=total
)
totalbutton.grid(row=0,column=0,pady=20,padx=5)

billbutton=Button(
    buttonframe,
    text='Bill',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white',
    bd=8,
    width=8,
    pady=8,
    command=billarea
)
billbutton.grid(row=0,column=1,pady=20,padx=5)

emailbutton=Button(
    buttonframe,
    text='E-Mail',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white',
    bd=8,
    width=8,
    pady=8,
    command=sendemail
)
emailbutton.grid(row=0,column=2,pady=20,padx=5)

printbutton=Button(
    buttonframe,
    text='Print',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white',
    bd=8,
    width=8,
    pady=8,
    command=printbill
)
printbutton.grid(row=0,column=3,pady=20,padx=5)

clearbutton=Button(
    buttonframe,
    text='Clear',
    font=('times new roman',15,'bold'),
    bg='gray10',
    fg='white',
    bd=8,
    width=8,
    pady=8,
    command=clear
)
clearbutton.grid(row=0,column=4,pady=20,padx=5)
root.mainloop()