# A library module.

import project

def hello():
    print('In the project.library.hello() function.')

    print(f'Saving data to {project.config["project_data_dir"]}!')

    return