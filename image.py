# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Nx7BhSP5wHAORNPqJHeljVT2pc8eGnx
"""

class image:
  li=["F8-107-1.jpg","F8-107-1 (2).jpg","F8-107-1 (3).jpg","F10-136-1.jpg","F10-136-2.jpg"]

  def path(img_name):
    return (path_prefix + img_name)

  def image(img_path):
    img=image.load_img(img_path,target_size=(300,300))
    img=image.img_to_array(img)
    images.append(imread(img_path))
    inputs.append(img.copy())
    return inputs

  def load(image_path):
    inputs=images_loading(image_path))

  for i in li:
    image_path=image(path(i))
    load(image_path)

m=int(input("請輸入m值? "))
n=int(input("請輸入n值? "))

def hcf(m,n):
  de_m=[]
  for m in range(1,m+1):
    de_m.append()
print(m,"與",n,"的最大公因數為")