#!"C:\Users\V\AppData\Local\Programs\Python\Python310\python.exe"
print("content-type: text/html;charset=utf-8\n")
print()

import cgi

# get url query string
form = cgi.FieldStorage()
print(form, '<br>')
if 'id' in form:
    pageId=form['id'].value # get id from url query string
    description=open('data/'+pageId, 'r').read()
    print("./data/"+pageId, '<br>')
else:
    pageId="Welcome"    
    description="Hello WEB!"
print(pageId)

print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    <li><a href="index.py?id=HTML">HTML</a></li>
    <li><a href="index.py?id=CSS">CSS</a></li>
    <li><a href="index.py?id=JavaScript">JavaScript</a></li>
  </ol>
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description))