# import external libraries
from tkinter import *
from PIL import Image, ImageTk
import time

vertical_padding = 5
horizontal_padding = 5

class StatusBar():
    def __init__(self, parent):
        self.window = parent.window
        self.parent = parent
        self.canvas = parent.bar_canvas
        self.width = parent.width
        self.height = 0.077 * parent.height

        button_width = int(0.03*self.width)
        button_height = int(self.height - 2*vertical_padding)

        # logo
        logo_width = int(0.13*self.width)
        logo_height = int(self.height - 2*vertical_padding)
        logo_x = horizontal_padding+logo_width/2
        logo_y = vertical_padding+logo_height/2
        self.logo = ImageTk.PhotoImage(Image.open("image/logo.png").resize((logo_width,logo_height)))
        self.canvas.create_image(logo_x, logo_y, image=self.logo)

        # leave
        leave_width = button_width
        leave_height = button_height
        leave_x = self.width-horizontal_padding-leave_width/2
        leave_y = vertical_padding+leave_height/2
        self.leave = ImageTk.PhotoImage(Image.open("image/exit_button.png").resize((leave_width,leave_height)))
        self.canvas.create_image(leave_x, leave_y, image=self.leave)

        # clock
        t = time.strftime("%H:%M:%S", time.localtime())
        t_x = self.width - 3*horizontal_padding - leave_width
        t_y = vertical_padding
        text = self.canvas.create_text(t_x, t_y, anchor=NE, text=t,fill='black',font=('Castoro', int(0.045 * self.parent.height)))
        text_bound = self.canvas.bbox(text)
        text_width = text_bound[2]-text_bound[0]
        text_height = text_bound[1]-text_bound[3]

        # volume
        volume_width = button_width
        volumn_height = button_height
        volume_x = self.width-5*horizontal_padding-leave_width-text_width-volume_width/2
        volume_y = vertical_padding+volumn_height/2
        self.volume = ImageTk.PhotoImage(Image.open("image/volume_button.png").resize((volume_width,volumn_height)))
        self.canvas.create_image(volume_x, volume_y , image=self.volume)

        # wifi
        wifi_width = button_width
        wifi_height = button_height
        wifi_x = volume_x - volume_width/2 - 2*horizontal_padding - wifi_width/2
        wifi_y = vertical_padding+wifi_height/2
        self.wifi = ImageTk.PhotoImage(Image.open("image/wifi_button.png").resize((wifi_width,wifi_height)))
        self.canvas.create_image(wifi_x, wifi_y, image=self.wifi)
