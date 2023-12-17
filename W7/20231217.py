from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("Class10")
root.geometry("880x650")

# Row0
# Logo_Tree
TitleImage = Image.open("C:/Users/yoshi_pgnry07/Desktop/Python_2022Autumn/class10/image/logo_tree.png")
TitleImage = TitleImage.resize((32,32))
TitleImage = ImageTk.PhotoImage(TitleImage)
TitleLabel = Label(root, image=TitleImage)
TitleLabel.grid(row=0,column=0,sticky=W+N+S)
# 沙發 寢具 廚具 登入
SofaButton = Button(root, text="沙發", pady=2, padx=5,fg="#1E1E1E",bg="#ECE8E7",width=5, font=("Inter",12))
BedingButton = Button(root, text="寢具", pady=2, padx=5,fg="#1E1E1E",bg="#ECE8E7",width=5, font=("Inter",12))
kitchenwaiButton = Button(root, text="廚具", pady=2, padx=5,fg="#1E1E1E",bg="#ECE8E7",width=5, font=("Inter",12))
SignUpButton = Button(root, text="會員登入/註冊", pady=2, padx=5,fg="#1E1E1E",bg="#F8DCDC",width=12, font=("Inter",12))
SofaButton.grid(row=0,column=1,sticky=E+W)
BedingButton.grid(row=0,column=2,sticky=E+W)
kitchenwaiButton.grid(row=0,column=3,sticky=E+W)
SignUpButton.grid(row=0,column=7,sticky=E+W)

# row1
# Banner
BannerImage = Image.open("C:/Users/yoshi_pgnry07/Desktop/Python_2022Autumn/class10/image/banner.jpg")
BannerImage = BannerImage.resize((852,298))
BannerImage = ImageTk.PhotoImage(BannerImage)
BannerLabel = Label(root, image=BannerImage)
BannerLabel.grid(row=1,column=0,columnspan=8,padx=5,sticky=W+N+S+E)

# row2
# Sofa1+2+3+4
Sofa1Image = Image.open("C:/Users/yoshi_pgnry07/Desktop/Python_2022Autumn/class10/image/sofa1.jpg")
Sofa1Image = Sofa1Image.resize((202,200))
Sofa1Image = ImageTk.PhotoImage(Sofa1Image)
Sofa2Image = Image.open("C:/Users/yoshi_pgnry07/Desktop/Python_2022Autumn/class10/image/sofa2.jpg")
Sofa2Image = Sofa2Image.resize((202,200))
Sofa2Image = ImageTk.PhotoImage(Sofa2Image)
Sofa3Image = Image.open("C:/Users/yoshi_pgnry07/Desktop/Python_2022Autumn/class10/image/sofa3.jpg")
Sofa3Image = Sofa3Image.resize((202,200))
Sofa3Image = ImageTk.PhotoImage(Sofa3Image)
Sofa4Image = Image.open("C:/Users/yoshi_pgnry07/Desktop/Python_2022Autumn/class10/image/sofa4.jpg")
Sofa4Image = Sofa4Image.resize((202,200))
Sofa4Image = ImageTk.PhotoImage(Sofa4Image)

Sofa1Label = Label(root, image=Sofa1Image)
Sofa1Label.grid(row=2,column=0,columnspan=2,padx=5,sticky=W)
Sofa2Label = Label(root, image=Sofa2Image)
Sofa2Label.grid(row=2,column=2,columnspan=2,padx=5,sticky=W)
Sofa3Label = Label(root, image=Sofa3Image)
Sofa3Label.grid(row=2,column=4,columnspan=2,padx=5,sticky=W)
Sofa4Label = Label(root, image=Sofa4Image)
Sofa4Label.grid(row=2,column=6,columnspan=2,padx=5,sticky=W)

# row3
# Product Name
ProductName1Label = Label(root, text="三人座沙發, grann/bomstad 黑色/金屬", pady=2, padx=5,fg="#000000", font=("Inter",10))
ProductName2Label = Label(root, text="三人座沙發, grann/bomstad 黑色/木材", pady=2, padx=5,fg="#000000", font=("Inter",10))
ProductName3Label = Label(root, text="三人座沙發, grann/bomstad 米色/金屬", pady=2, padx=5,fg="#000000", font=("Inter",10))
ProductName4Label = Label(root, text="三人座沙發, grann/bomstad 米色/木材", pady=2, padx=5,fg="#000000", font=("Inter",10))
ProductName1Label.grid(row=3,column=0,columnspan=2,sticky=W)
ProductName2Label.grid(row=3,column=2,columnspan=2,sticky=W)
ProductName3Label.grid(row=3,column=4,columnspan=2,sticky=W)
ProductName4Label.grid(row=3,column=6,columnspan=2,sticky=W)

# row4
# Product Price
ProductPrice1Label = Label(root, text="NT.28,900", pady=2, padx=5,fg="#000000", font=("Inter",10))
ProductPrice2Label = Label(root, text="NT.28,900", pady=2, padx=5,fg="#000000", font=("Inter",10))
ProductPrice3Label = Label(root, text="NT.28,900", pady=2, padx=5,fg="#000000", font=("Inter",10))
ProductPrice4Label = Label(root, text="NT.28,900", pady=2, padx=5,fg="#000000", font=("Inter",10))
ProductPrice1Label.grid(row=4,column=0,padx=5,sticky=W)
ProductPrice2Label.grid(row=4,column=2,padx=5,sticky=W)
ProductPrice3Label.grid(row=4,column=4,padx=5,sticky=W)
ProductPrice4Label.grid(row=4,column=6,padx=5,sticky=W)
# Product Number
ProductNum1Label = Label(root, text="0", pady=2, padx=5,fg="#000000", font=("Inter",12))
ProductNum2Label = Label(root, text="0", pady=2, padx=5,fg="#000000", font=("Inter",12))
ProductNum3Label = Label(root, text="0", pady=2, padx=5,fg="#000000", font=("Inter",12))
ProductNum4Label = Label(root, text="0", pady=2, padx=5,fg="#000000", font=("Inter",12))
# Product Minus
ProductMinus1 = Button(root, text="-", bg="#E7E2E2",fg="#1E1E1E",font=("Inter",10))
ProductMinus2 = Button(root, text="-", bg="#E7E2E2",fg="#1E1E1E",font=("Inter",10))
ProductMinus3 = Button(root, text="-", bg="#E7E2E2",fg="#1E1E1E",font=("Inter",10))
ProductMinus4 = Button(root, text="-", bg="#E7E2E2",fg="#1E1E1E",font=("Inter",10))
# Product Plus
ProductPlus1 = Button(root, text="+", bg="#E7E2E2",fg="#1E1E1E",font=("Inter",10))
ProductPlus2 = Button(root, text="+", bg="#E7E2E2",fg="#1E1E1E",font=("Inter",10))
ProductPlus3 = Button(root, text="+", bg="#E7E2E2",fg="#1E1E1E",font=("Inter",10))
ProductPlus4 = Button(root, text="+", bg="#E7E2E2",fg="#1E1E1E",font=("Inter",10))
# Print out
ProductMinus1.grid(row=4,column=1,sticky=W)
ProductNum1Label.grid(row=4,column=1,sticky=W+E+S+N)
ProductPlus1.grid(row=4,column=1,sticky=E)
ProductMinus2.grid(row=4,column=3,sticky=W)
ProductNum2Label.grid(row=4,column=3,sticky=W+E+S+N)
ProductPlus2.grid(row=4,column=3,sticky=E)
ProductMinus3.grid(row=4,column=5,sticky=W)
ProductNum3Label.grid(row=4,column=5,sticky=W+E+S+N)
ProductPlus3.grid(row=4,column=5,sticky=E)
ProductMinus4.grid(row=4,column=7,sticky=W)
ProductNum4Label.grid(row=4,column=7,sticky=W+E+S+N)
ProductPlus4.grid(row=4,column=7,sticky=E)

# row5
# Row Config
root.rowconfigure(5, weight=2)
# Detail List
DetailListbtn = Button(root, text="詳細清單", bg="#ECEDE7",fg="#1E1E1E",font=("Inter",12))
DetailListbtn.grid(row=5,column=0,sticky=W+S,padx=5,pady=1)
# Shopping Cart
ShoppingCartImage = Image.open("C:/Users/yoshi_pgnry07/Desktop/Python_2022Autumn/class10/image/Shopping Cart.png")
ShoppingCartImage = ShoppingCartImage.resize((30,30))
ShoppingCartImage = ImageTk.PhotoImage(ShoppingCartImage)
ShoppingCartLabel = Label(root, image=ShoppingCartImage)
ShoppingCartLabel.grid(row=5,column=4,sticky=E+S)
# Total Val
TotalLabel = Label(root, text="共消費:0元", bg="#ECEDE7",fg="#1E1E1E", font=("Inter",12))
TotalLabel.grid(row=5,column=5,columnspan=2,sticky=S+W)
# Check Out
CheckOutButton = Button(root, text="結帳", bg="#ECEDE7",fg="#1E1E1E", font=("Inter",12))
CheckOutButton.grid(row=5,column=7,sticky=E+S)


root.mainloop()