# Short script to set up virtual environment in python and download the requesite libraries 

if [ -d "venv" ]; then
    echo "Virtual Environment ./venv already found. If there is an issue with dependencies, try deleting the venv and rerunning setup.sh"
else
    echo "Virtual enviroment not found. Setting up venv and installing dependencies..."
    python3 -m venv venv
    source ./venv/bin/activate
    python3 -m pip install -r requirements.txt
    echo "Dependencies installed. Note: to exit the virtual enviornment, use command 'exit' in shell or Ctrl-d"
fi

