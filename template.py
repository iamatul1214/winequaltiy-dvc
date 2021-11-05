
'''
template.py file is used to define the template/structure of the program.
Here we have defined folders where we can track the data.
'''

import os

dirs=[
    os.path.join('data','raw'),      ## os.path.join() will create the folders in the format in which program is being executed.
    os.path.join('data','processed'),
    'notebooks',
    'saved_models',
    'src'
]

for dir in dirs:
    os.makedirs(dir, exist_ok=True)
    with open(os.path.join(dir,'.gitkeep'),'w') as f:
        pass                                        ## This will create the directories

'''
This will create the required files.
'''

files=[
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py"),
    "README.md"
]

for file in files:
    with open(file,'w') as f:
        pass
