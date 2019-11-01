
import PySimpleGUI as sg
import datetime
import remi.gui as gui
from remi import start, App
from threading import Timer

class OCR_miniApp(App):
    def __init__(self, *args):
        super(OCR_miniApp, self).__init__(*args)

    def main(self):
        #sg.ChangeLookAndFeel('GreenTan')

        col = [
                [sg.Button('表格识别', font='Helvetica 20', button_color=('black', 'white'), size=(20,1.5))],
                [sg.Button('文档识别', font='Helvetica 20', button_color=('black', 'white'), size=(20,1.5))]
            ]
        #main windows
        layout_main =  [
                    [sg.Text('AI工具', size=(100,1.5), font='Helvetica 20', text_color='white', background_color='black')],
                    [sg.Image(filename=r'logo.png',size=(100,100), key='yxlogo', enable_events=True)],
                    [sg.Text('识别能力列表：', size=(20,1), font='Helvetica 25', pad=(10,10))],
                    [sg.Column(col, background_color='white')]
                ]
        sg.Image()
        window_main = sg.Window('OCR List',
                           #default_element_size=(30,1),
                           #font='Helvetica 18',
                           text_justification='center',
                        ).Layout(layout_main)
        #table ocr windows
        layout_tableocr =  [
                    [sg.Button('返回')],
                    [sg.Image(key='img_ocr', enable_events=True)],
                    [sg.Text('识别结果：', size=(20,1), font='Helvetica 25', pad=(10,10))],
                    [sg.Output()]
                ]
        window_tableocr = sg.Window('Table OCR',
                           #default_element_size=(30,1),
                           #font='Helvetica 18',
                           text_justification='center'
                        ).Layout(layout_tableocr)
        win_tableocr_active = False
        while True:
            event, values = window_main.Read(timeout=10)
            if event != sg.TIMEOUT_KEY:
                print(event, values)
            if event == '表格识别' and not win_tableocr_active:
                win_tableocr_active = True
                print(event, values)
                self.goto_tableocr_web(self)
                window_tableocr = sg.Window('Table OCR',
                                            # default_element_size=(30,1),
                                            # font='Helvetica 18',
                                            element_justification='center', finalize=True
                                            ).Layout(layout_tableocr)
            if win_tableocr_active:
                print("go to table ocr windows")
                event, values = window_tableocr.Read(timeout=100)
                # print("win2 ", event)
                if event != sg.TIMEOUT_KEY:
                    print("win2 ", event)
                if event == '返回' or event is None:
                    # print("Closing window 2", event)
                    win_tableocr_active = False
                    window_tableocr.Close()
            if event == 'yxlogo':
                print ('yxlogo')

            if event in (None, 'Exit'):
                break

        window.Close()

    # 跳转到官网
    def on_img_clicked(self):
        print('官网: http://www.yuanxiang.cn')

    def goto_tableocr_web(self,widget):
        print('go to table-ocr')
        to = TableOcr()
        to.main()
    def goto_dococr_web(self):
        print('go to doc-ocr')

class TableOcr():
    def __init__(self, *args):
        super(TableOcr, self).__init__(*args)

    def main(self):
        print ('table ocr class')

if __name__ == "__main__":
    # starts the webserver
    # optional parameters
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    import ssl
    start(OCR_miniApp, debug=True, address='0.0.0.0', port=8081, start_browser=True, multiple_instance=True)

