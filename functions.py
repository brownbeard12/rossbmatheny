import dominate
import os
import ntpath
from dominate.tags import *

#Find any images in /assets folder, not including sub-directories
def img_loop(img_dir):
	for entry in os.scandir(img_dir):
		if (entry.path.endswith(".jpg")
				or entry.path.endswith(".png")) and entry.is_file():
			if entry.path.endswith(".jpg"):
				img_name = ntpath.basename(entry.path).replace(".jpg","")
			elif entry.path.endswith(".png"):
				img_name = ntpath.basename(entry.path).replace(".png","")
			if (img_name.startswith("a_")
				or img_name.startswith("b_")
				or img_name.startswith("c_")
				or img_name.startswith("d_")
				or img_name.startswith("e_")
				or img_name.startswith("f_")
				or img_name.startswith("g_")
				or img_name.startswith("h_")
				or img_name.startswith("i_")
				or img_name.startswith("j_")
				or img_name.startswith("k_")):
				img_name = img_name[2:]
			with div():
				img(_class='u-max-full-width', src=entry.path, alt=img_name.capitalize())
