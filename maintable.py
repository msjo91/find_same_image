# -*- coding: utf-8 -*-

from imagebtn import *
from tkinter import *
from random import *
import time


class Maintable(Frame):
    n=0
    selected_image=0
    
    def __init__(self, master, picture, alphabet, width):
        super(Maintable, self).__init__()
        self.image_number_list = []  # 셔플된 이미지의 번호를 저장하기 위한 리스트. 16개
        self.master = master # maintable frame의 parent 설정
        self.width = width # maintable의 넓이. = 4
        self.n = width * width # maintable에 추가될 이미지 수. = 16
        self.picture = picture # # app에서 생성한 이미지 받아와서 저장

        # 숨겨진 이미지 셔플링
        self.random_shuffle()

        # TODO
        # ImageButton widget 생성하고 각 widget에 숨겨진 이미지 추가
        # 이미지 클릭시 이벤트 bind
        for i in range(0,self.width):
            for j in range(0,self.width):
                pass



    # TODO
    # hidden 이미지 셔플링
    def random_shuffle(self):
        print('random')
    # 선택된 알파벳 ImageButton의 숨겨진 이미지 출력
    def show_hidden(self, event):
        event.widget.config(image=event.widget.get_hidden())

    # TODO
    # 숨겨진 이미지 숨기고 알파벳 이미지로 변환
    # 선택된 이미지와 컨베이어의 현재 이미지와 비교하고, 비교 결과에 따른 명령어 실행 부분
    def hide_picture(self, event):
        #time.sleep(10)
        #time.sleep(1.5)
        selected_image = self.picture.index(event.widget.hidden)

        
        
