# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import gspread
from docutils.parsers import null
from gspread import Spreadsheet
#import service as service
from oauth2client.service_account import ServiceAccountCredentials

scope=["https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/drive.file"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("gs_credentials.json", scope )
client = gspread.authorize(credentials)

#client.create("Tickets")

wbID = '1lrQIC1k10Q-6aAvljW5-jEazjrlcsg1SML_yAni2SaE'
hoja : Spreadsheet = client.open_by_key(wbID)
pag = hoja.worksheet("inicios")


#pag.append_row(["HOLA","MUNDO"])
val = pag.acell('E2').value

if val is None :
        print('error')
else:
        print(val)

l = val
n = []

for x in l:
   n.append(ord(x) - 96)
print(n)


#from tkinter import *

#raiz=Tk()
#raiz.title("Ene-0")
#raiz.geometry("550x250")
#raiz.resizable("false,false")

#lbl=Label(raiz, text)
#raiz.mainloop()


