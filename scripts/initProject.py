import os

def create_project_structure(root_dir):
    # config your project structure
    folders = ['src', 'docs', 'tests', 'data', 'config', 'lib', 'scripts', 'output', 'logs', 
               'models', 'dist', 'resources', 'web', 'backend', 'docs/requirements']

    try:
        os.makedirs(root_dir)
        for folder in folders:
            os.makedirs(os.path.join(root_dir, folder))
        print("Project folder structure initialization is complete!!")

    except FileExistsError:
        print(f"Error: {root_dir} Already exists, please select a new directory name.")

    except Exception as e:
        print(f"An error occurred while initializing the project folder structure: {e}")

if __name__ == "__main__":
    project_root_dir = "my_project"
    create_project_structure(project_root_dir)
