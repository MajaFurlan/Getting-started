from tkinter import *

st_vrstic = 4 
st_vzigalic_po_vrsticah = [1,3,5,7]

matrika=list()
for i in range(st_vrstic):
    matrika.append([1]*st_vzigalic_po_vrsticah[i] + [0]*(max(st_vzigalic_po_vrsticah) - st_vzigalic_po_vrsticah[i]))


root = Tk()
root.title("Nim")
w = Canvas(root, width = 150*max(st_vzigalic_po_vrsticah), height = 150*st_vrstic)
for i in matrika:
            k=0
            for j in range(max(st_vzigalic_po_vrsticah)):
                if matrika[i][j]==1:
                    w.create_line(50+k,50*i,50+k,100*i)
                    k+=100
                else:
                    k+=100
root.mainloop()

k=5
a=k*2
