#! /usr/bin/env python
from curses import REPORT_MOUSE_POSITION
from re import L
import cv2
import ttkbootstrap as tk
from tkinter import *
import PIL.Image, PIL.ImageTk
from PIL import ImageTk, Image
from cv2 import getPerspectiveTransform
import numpy as np
import matplotlib.pyplot as plt
from regex import P
import yaml 

TARGET_H, TARGET_W = 500, 500
camera_img = cv2.imread('Dataset/data1/data1_65.jpg')
camera_img = cv2.cvtColor(camera_img, cv2.COLOR_BGR2RGB)
target_image = cv2.imread('template.png')
target_image = cv2.resize(target_image, (TARGET_W, TARGET_H))


targ_pts = 4

pt_ctr = 0
img_pts = []
ipm_pts = []
wrld_pts = []
M = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

#create 2 windows SEPARATE one to show the cam_img with cam_img dimensions and another to show the target_image with TARGET_W, TARGET_H dimensions
cam_window = tk.Window(themename="superhero")
cam_window.title("Camera Image")
cam_canvas = Canvas(cam_window, width=camera_img.shape[1], height=camera_img.shape[0])
cam_canvas.pack()
cam_img = PIL.Image.fromarray(camera_img)
cam_img = ImageTk.PhotoImage(cam_img)
cam_canvas.create_image(0, 0, image=cam_img, anchor=NW)

target_canvas = Toplevel()
target_canvas.title("Template Image")
target_canvas = Canvas(target_canvas, width=TARGET_W, height=TARGET_H)
target_canvas.pack()
target_image = cv2.cvtColor(target_image, cv2.COLOR_BGR2RGB)
target_image = PIL.Image.fromarray(target_image)
target_image = ImageTk.PhotoImage(target_image)
target_canvas.create_image(0, 0, image=target_image, anchor=NW)


def left_click(event):
    global pt_ctr, img_pts, ipm_pts, wrld_pts, M
    if pt_ctr < targ_pts:
        pt_ctr += 1
        img_pts.append([event.x, event.y])
        cam_canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill='blue')
        cam_canvas.create_text(event.x, event.y, text=pt_ctr)
        cam_canvas.update()
        print("Point %d added" % pt_ctr)
        print("Image Points: ", img_pts)

    elif pt_ctr >= targ_pts and pt_ctr < targ_pts*2:
        pt_ctr += 1
        wrld_pts.append([event.x, event.y])
        target_canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill='red')
        target_canvas.create_text(event.x, event.y, text=pt_ctr)
        target_canvas.update()
        print("Point %d added" % pt_ctr)
        print("World Points: ", wrld_pts)

    elif pt_ctr == targ_pts*2:
        img_pts = np.float32(img_pts)
        wrld_pts = np.float32(wrld_pts)
        M = getPerspectiveTransform(img_pts, wrld_pts)
        print("Homography Matrix: ", M)
        warped = cv2.warpPerspective(camera_img, M, (TARGET_W, TARGET_H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT,
                                 borderValue=0)
        save_yaml()
        #show the wraped image with opencv in a pop up window
        warped = cv2.cvtColor(warped, cv2.COLOR_BGR2RGB)
        cv2.imshow("Warped", warped)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        pt_ctr += 1




def right_click(event):
    global pt_ctr, img_pts, ipm_pts, wrld_pts, M
    if pt_ctr <= 4:
        pt_ctr -= 1
        cam_canvas.delete("all")
        cam_canvas.create_image(0, 0, image=cam_img, anchor=NW)
        img_pts.pop()
        
        for i in range(len(img_pts)):
            cam_canvas.create_oval(img_pts[i][0]-5, img_pts[i][1]-5, img_pts[i][0]+5, img_pts[i][1]+5, fill='blue')
            cam_canvas.create_text(img_pts[i][0], img_pts[i][1], text=i+1)
        cam_canvas.update()
        print("Point %d removed" % pt_ctr)
    elif pt_ctr > 4 and pt_ctr < 8:
        pt_ctr -= 1
        target_canvas.delete("all")
        target_canvas.create_image(0, 0, image=target_image, anchor=NW)
        wrld_pts.pop()
        
        for i in range(len(wrld_pts)):
            target_canvas.create_oval(wrld_pts[i][0]-5, wrld_pts[i][1]-5, wrld_pts[i][0]+5, wrld_pts[i][1]+5, fill='red')
            target_canvas.create_text(wrld_pts[i][0], wrld_pts[i][1], text=i+1)
        target_canvas.update()
        print("Point %d removed" % pt_ctr)


def save_yaml():
    global M
    with open('homography_calib.yaml', 'w') as f:
        yaml.dump({'M': M.tolist()}, f)
        f.write('\n')
    f.close()
    print("Homography Matrix saved to homography_calib.yaml")





cam_canvas.bind("<Button-3>", right_click)
cam_canvas.bind("<Button-1>", left_click)

target_canvas.bind("<Button-3>", right_click)
target_canvas.bind("<Button-1>", left_click)


cam_window.mainloop()
target_canvas.mainloop()