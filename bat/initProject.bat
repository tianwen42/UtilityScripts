@echo off
set project_root=my_project

if not exist %project_root% (
    mkdir %project_root%
    cd %project_root%

    @REM  config your project structure
    mkdir src docs tests data config lib scripts output logs models dist resources web backend docs\requirements
    
    echo Project folder structure initialization is complete!!
) else (
    echo Error: Folder %project_root% Already exists, please select a new directory name.
)