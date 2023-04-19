@echo off

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in the system PATH. pizduy siudy: https://www.python.org/downloads/release/
    exit /b 1
)

REM Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo Pip is not installed or not in the system PATH. installing PIP
    pushd scripts
    python get-pip.py
    popd
)

REM Install pip packages if not already installed
pip show cryptography >nul 2>&1
if errorlevel 1 (
    echo Installing cryptography...
    pip install cryptography
)

pip show requests >nul 2>&1
if errorlevel 1 (
    echo Installing requests...
    pip install requests
)

echo Packages installed successfully.

REM Check if the large_file folder does not exist
if not exist large_files (
    REM Change to the scripts directory
    pushd scripts

    REM Change to the scripts/resources directory
    pushd resources

    REM Check if local.properties exists
    if exist local.properties (
        echo scripts/resources/local.properties exists. Continue execution...
    ) else (
        REM If the file does not exist, create it with placeholder data and stop execution
        echo seed=^<placeholder^> > local.properties
        echo local.properties did not exists. populate the scripts/resources/local.properties with the SECRET_SEED and run this .bat file again
        popd
        exit /b
    )

    REM Continue with the rest of your script
    popd

    REM Execute your Python scripts
    python prerequisites.py

    REM Return to the root folder
    popd
) else (
    echo large_files dir exists, download is not required.
)


echo Our daddy told us not be ashamed of our rationality and intelligence