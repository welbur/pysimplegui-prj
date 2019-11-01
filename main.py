"""
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import remi.gui as gui
from remi import start, App
from threading import Timer


class OCR_miniApp(App):
    def __init__(self, *args):
        super(OCR_miniApp, self).__init__(*args)

    def main(self):
        # the margin 0px auto centers the main container
        verticalContainer = gui.Widget(width=540, margin='0px auto', style={'display': 'block', 'overflow': 'hidden'})

        horizontalContainer = gui.Widget(width='100%', layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, margin='0px',
                                         style={'display': 'block', 'overflow': 'auto'})

        subContainerLeft = gui.Widget(width=320, style={'display': 'block', 'overflow': 'auto', 'text-align': 'center'})

        self.img = gui.Image('/res:logo.png', height=100, margin='10px')
        self.img.onclick.connect(self.on_img_clicked)

        self.uptext = gui.Label('识别应用场景')
        self.bt_tableocr = gui.Button('表格识别', width=200, height=30, margin='10px')
        self.bt_tableocr.onclick.connect(self.goto_tableocr_web)
        self.bt_tableocr = gui.Button('文档识别', width=200, height=30, margin='10px')
        self.bt_tableocr.onclick.connect(self.goto_dococr_web)


        # this flag will be used to stop the display_counter Timer
        self.stop_flag = False

        # returning the root widget
        return verticalContainer


    # listener function
    # 跳转到官网
    def on_img_clicked(self, widget):
        print ('官网: http://www.yuanxiang.cn')

    def goto_tableocr_web(self,widget):
        print('go to table-ocr')
    def goto_dococr_web(self,widget):
        print ('go to doc-ocr')

    def on_close(self):
        """ Overloading App.on_close event to stop the Timer.
        """
        self.stop_flag = True
        super(OCR_miniApp, self).on_close()


if __name__ == "__main__":
    # starts the webserver
    # optional parameters
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    import ssl

    start(OCR_miniApp, debug=True, address='0.0.0.0', port=8081, start_browser=True, multiple_instance=True)
