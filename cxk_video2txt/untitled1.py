# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:45:45 2019

@author: xm
"""
import cv2
import time
import numpy as np
import curses
pixels = " .,-'`:!1+*%    "
time.sleep(5)
def img_2_char(img):
    '''
    »Ò¶ÈÍ¼ÏñÓ³Éä³É×Ö·û[0,255] -> [0,16]
    ÓÃ[0,16]Ë÷ÒýÖµÈ¡×Ö·û
    :param img:
    :return:  ×Ö·ûÊý×é
    '''
    ret = []
    p = img / 255
    indexes = (p * (len(pixels) - 1)).astype(np.int)
    height, width = img.shape
    for row in range(height):
        line = ""
        for col in range(width):
            index = indexes[row][col]
            line += pixels[index] + " "
        ret.append(line)
    return ret




def play_video(video_char):
    width, height = len(video_char[0][0]), len(video_char[0])
    stdscr = curses.initscr()
    curses.start_color()
    try:
        stdscr.resize(height, width * 2)
        for pic_i in range(len(video_char)):
            for line_i in range(height):
                # ½«pic_iµÄµÚiÐÐÐ´ÈëµÚiÁÐ¡£(line_i, 0)±íÊ¾´ÓµÚiÐÐµÄ¿ªÍ·¿ªÊ¼Ð´Èë¡£×îºóÒ»¸ö²ÎÊýÉèÖÃ×Ö·ûÎª°×É«
                stdscr.addstr(line_i, 0, video_char[pic_i][line_i], curses.COLOR_WHITE)
            stdscr.refresh()  # Ð´ÈëºóÐèÒªrefresh²Å»áÁ¢¼´¸üÐÂ½çÃæ
            time.sleep(1 / 40)
    finally:
        curses.endwin()


cap = cv2.VideoCapture('cxk.mp4')
stdscr = curses.initscr()
curses.start_color()

#hasFrame, frame = cap.read()
#frame=cv2.resize(frame,(64,40))
#frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#char=img_2_char(frame)
width, height = 128,40

#len(char[0]), len(char)
import time
time1=time.time()
while 1:
    hasFrame, frame = cap.read()
    if not hasFrame :
#        cv2.waitKey()
        break
    
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame=cv2.resize(frame,(64,40))
    char=img_2_char(frame)
#    cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)
#    frameWidth = frame.shape[1]
#    frameHeight = frame.shape[0]


    try:
#        stdscr.resize(height, width * 2)
#        stdscr.resize(height//2, width*2)
        for line_i in range(height):
            # ½«pic_iµÄµÚiÐÐÐ´ÈëµÚiÁÐ¡£(line_i, 0)±íÊ¾´ÓµÚiÐÐµÄ¿ªÍ·¿ªÊ¼Ð´Èë¡£×îºóÒ»¸ö²ÎÊýÉèÖÃ×Ö·ûÎª°×É«
            stdscr.addstr(line_i, 0, char[line_i], curses.COLOR_WHITE)
#            stdscr.addstr(line_i, 0, video_char[pic_i][line_i], curses.COLOR_WHITE)

        stdscr.refresh()  # Ð´ÈëºóÐèÒªrefresh²Å»áÁ¢¼´¸üÐÂ½çÃæ
        time.sleep(1 / 30) #¿ÉÄÜÓëµçÄÔÅäÖÃÓÐ¹Ø Òô»­²»Í¬£¬
    except:
        continue
#    finally:

curses.nocbreak()#¹Ø±Õ×Ö·ûÖÕ¶Ë¹¦ÄÜ£¨Ö»ÓÐ»Ø³µÊ±²Å·¢ÉúÖÕ¶Ë£©
stdscr.keypad(0)
curses.echo() #´ò¿ªÊäÈë»ØÏÔ¹¦ÄÜ
curses.endwin()
print("time: ")
print(time.time()-time1)
cap.release()
