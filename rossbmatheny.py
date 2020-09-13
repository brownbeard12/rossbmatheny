import dominate
import os
import ntpath
import functions

from dominate.tags import *

doc = dominate.document(title="Ross B. Matheny | Engineer")

#loc_assets = "/Users/Matheny Properties/Documents/WEBSITES/ROSSBMATHENY"
loc_assets = ""

#img_dir = r'C:\Users\Matheny Properties\Documents\WEBSITES\ROSSBMATHENY\assets'
img_dir = "assets/"

functions.page_head(doc)
	
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
				functions.img_loop(img_dir)	

		with div(_class='container'):
			h2('Contact', _class="section")
			
			with form(name="contact", method="POST", data-netlify="true"):
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
