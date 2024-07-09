import tkinter
from pathlib import Path
from tkinter import filedialog
import openpyxl

class Application(tkinter.Frame):
    def __init__(self,root=None):
        super().__init__(root,width=380,height=280,borderwidth=1,relief="groove")
        self.root=root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        quit_btn=tkinter.Button(self)
        quit_btn["text"]="閉じる"
        quit_btn["command"]=self.root.destroy
        quit_btn.pack(side="bottom")

        self.text_box=tkinter.Entry(self)
        self.text_box["width"]=10
        self.text_box.pack()

        submit_btn=tkinter.Button(self)
        submit_btn["text"]="実行"
        submit_btn["command"]=self.save_data
        submit_btn.pack()

        self.message=tkinter.Message(self)
        self.message.pack()

    def save_data(self):
        text=self.text_box.get()
        file_name=filedialog.askopenfilename(initialdir=Path.cwd())
        wb=openpyxl.load_workbook(file_name)
        ws=wb.worksheets[0]
        ws["A1"].value=text
        wb.save(file_name)
        self.message["text"]="保存完了"

root=tkinter.Tk()
root.title("ExcelApp")
root.geometry("400x300")
app=Application(root=root)
app.mainloop()