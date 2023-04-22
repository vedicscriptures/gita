import os

# set the base directory
base_dir = '.'

# iterate over all the folders and subfolders
for root, dirs, files in os.walk(base_dir):
    for file in files:
        # check if the file is an index.html file
        if file == 'index.html':
            # get the folder name as x
            x = os.path.basename(root)
            # get the subfolder name as y
            y = os.path.basename(os.path.dirname(os.path.abspath(root)))
            # read the current data from the html file
            with open(os.path.join(root, file), 'r') as f:
                body = f.read()
            # modify the html file as per the requirement
            modified_html = f'''
            <!DOCTYPE html>
            <html>
            <head>
              <meta charset="UTF-8">
              <title>Bhagavad Gita API : Chapter {x} Slok {y} </title>
              <link rel="stylesheet" href="../../css/style.css">
            </head>
            <body>
            {body}
            </body>
            </html>
            '''
            # write the modified html back to the file
            with open(os.path.join(root, file), 'w') as f:
                f.write(modified_html)
