#!/usr/bin/python2.7

import os

filelist = [f for f in os.listdir(".") if f.endswith(".html")]
for f in filelist:
    os.remove(f)

for filename in os.listdir('./../markdown/'):
    if filename[-2:] == "md":
        md = open('./../markdown/' + filename, "r")
        md_contents = md.read()
        md.close()
        html = open('./' + filename[:-2] + "html", "w")
        html.write('<!DOCTYPE html>\n')
        html.write('<html>\n')
        html.write('<title>' + filename[:-3] + '</title>\n')
        html.write('<xmp theme="united" style="display:none;">\n\n')
        md_contents = md_contents.replace(".md)", ".html)")
        html.write(md_contents)
        html.write('\n\n</xmp>\n')
        html.write('<script src="strapdown.js/strapdown.js"></script>\n')
        html.write('</html>\n')
        html.close()
