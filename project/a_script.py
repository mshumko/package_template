# A script showing how this package is imported into a script.

import project

# Can also put this in __init__.py so it is imported as package.hello
from project.library import hello

print('In a_script.py!')
print(f'Configuration paths: {project.config}')

hello()