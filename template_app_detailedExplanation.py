import tkinter
#tkinterモジュールをインポートし、tkinterの機能を使用

class Application(tkinter.Frame):#tkinter.Frameを継承したApplicationクラスの定義、FrameはGUIアプリケーションのウィンドウを表すコンポーネント
    def __init__(self,root=None):#クラスのコンストラクタメソッド、クラスの初期化を行っている。rootパラメータはウィンドウの親フレームを表す
        super().__init__(root,width=380,height=280,borderwidth=1,relief="groove")#super()は親クラスの属性やメソッドを呼び出すメソッド、rootはウィジェットの親となるTkインスタンスwidth=380,height=280:ウィジェットサイズの指定,borderwidth=1,relief="groove":ウィジェットの枠線設定
        self.pack()#クラス内部のインスタンスをウィジェット内部にデフォルトで設置
        self.pack_propagate(0)#ウィジェットのサイズ設定を無効にする
        self.root=root#クラスのインスタンス変数に引数のrootの値を割り当てる
        self.create_widgets_close()#閉じるボタンのメソッドを呼び出す
        self.create_widgets_text()#テキスト入力と実行ボタンを作成するメソッドを呼び出す



    def create_widgets_close(self):
        quit_btn=tkinter.Button(self)#ボタンウィジェットを作成
        quit_btn["text"]="閉じる"#ボタンのテキストを設定
        quit_btn["command"]=self.root.destroy#ボタンがクリックされたときにウィンドウを閉じるコマンド
        quit_btn.pack(side="bottom")#ボタンの位置を下に設定

    def create_widgets_text(self):
        self.text_box=tkinter.Entry(self)
        self.text_box["width"]=10
        self.text_box.pack()
        submit_btn=tkinter.Button(self)
        submit_btn["text"]="実行"
        submit_btn["command"]=self.input_handler
        submit_btn.pack()
        self.message=tkinter.Message(self)
        self.message.pack()

    def input_handler(self):
        text=self.text_box.get()
        self.message["text"]=text+"!!"




root=tkinter.Tk()
root.title('アプリ')
root.geometry('400x300')

app=Application(root=root)

app.mainloop()