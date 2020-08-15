import dominate
import os
import ntpath

from dominate.tags import *

doc = dominate.document(title="Ross B. Matheny | Engineer")

loc_assets = "/Users/Matheny Properties/Documents/WEBSITES/ROSSBMATHENY"
#loc_assets = ""

img_dir = r'C:\Users\Matheny Properties\Documents\WEBSITES\ROSSBMATHENY\assets'
#img_dir = 

with doc.head:
	meta(charset='utf-8')
	meta(name='description', content="Ross B. Matheny's Website")
	meta(name='author', content="Ross B. Matheny")
	meta(name='viewport', content="width=device-width, initial-scale=1")
	link(href="https://fonts.cdnfonts.com/css/league-spartan", rel="stylesheet")
	link(rel="stylesheet", href="normalize.css")
	link(rel="stylesheet", href="skeleton.css")
	link(rel="stylesheet", href="extra.css")
	link(rel="icon", type="image/png", href="assets/fav/favicon.ico")
	link(rel="apple-touch-icon", sizes="180x180", href="assets/fav/apple-touch-icon.png")
	link(rel="icon", type="image/png", sizes="32x32", href="assets/fav/favicon-32x32.png")
	link(rel="icon", type="image/png", sizes="16x16", href="assets/fav/favicon-16x16.png")
	link(rel="mask-icon", href="assets/fav/safari-pinned-tab.svg", color="#5bbad5")
	
with doc:
	attr(lang="en")
	with div(_class='main'):
		with div(_class='header league'):
			with header():
				h1('Ross B. Matheny')
			h2('Engineer + 3D Artist')
		with div(_class='container'):
			h2('Work', _class='section')
			
			with div(_class='center-content'):
			
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

		with div(_class='container'):
			h2('Contact', _class="section")
			
			with form(name="contact", method="POST"):
				input(type="hidden", name="form-name", value="contact")
				with div(_class="row"):
					with div(_class="six columns"):
						label("Your Name:", _for="name")
						input(id="name", _class="u-full-width", type="text", name="name")
					with div(_class="six columns"):
						label("Your Email:", _for="email")
						input(id="email", _class="u-full-width", type="text", name="email")
					label("Message:", _for="message")
					textarea(id="message", _class="u-full-width", name="message")
					button("Send", type="submit")
					
		footer("Copyright 2020.", _class="footer league")

with open('index.html', 'w') as f:
	print(doc, file=f)