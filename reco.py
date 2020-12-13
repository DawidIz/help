#!/usr/bin/python3

import os,sys,subprocess

# html template
html = '''<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Document</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <script src="index.js"></script>
    </body>
</html>'''

# directory name from args
try:
    path = sys.argv[1]
except Exception as e:
    print(e)
    sys.exit(1)

# create dir
try:
    os.mkdir(path)
    print('Created directory: ' + path)
except Exception as e:
    print(e)
    sys.exit(1)

# create files in directory

try:
    with open(path + '/index.html','w') as file:
        file.write(html)

    cmd = f'touch {path}/index.js {path}/style.css'
    subprocess.run(
        cmd,
        shell = True,
        check = True)

    print('Created files: index.html, index.js, style.css')
    sys.exit(0)

except Exception as e:
    print(e)
    
# cleaning after failure
try:
    os.rmdir(path)
    print('Directory %s deleted' % path)
except Exception as e:
    print(e)
