#!"C:\Users\V\AppData\Local\Programs\Python\Python310\python.exe"

# add "delete with confirm alert"

print("Content-Type: text/html")
print()
import cgi, os
 
files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
 
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    
    # add function into form action, onclick: if true run default action else run reload page 
    delete_action = '''
      <form onsubmit="javascript:myFunction();" method="post" name="theForm">
        <input type="hidden" name="pageId" value="{}" />
        <input type="submit" value="delete"/>
      </form>
    '''.format(pageId)
else:
    pageId = 'Welcome'
    description = 'Hello, web'
    update_link = ''
    delete_action = ''
print('''<!doctype html>
<html>
<head>
  <title>WEB-Python</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href="create.py">create</a>
  {update_link}  
  <h2>{title}</h2>
  <p>{desc}</p>
  {delete_action}
  <script src="./js/delete.js"></script>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr, update_link=update_link, delete_action=delete_action))