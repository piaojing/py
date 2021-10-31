#!"C:\Users\V\AppData\Local\Programs\Python\Python310\python.exe"

# modify file name, contents

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form['description'].value
 
opened_file = open('data/'+pageId, 'w')
opened_file.write(description)
opened_file.close()
 
os.rename('data/'+pageId, 'data/'+title) # change file name from pageID to title
 
#Redirection
print("Location: index.py?id="+title)
print()