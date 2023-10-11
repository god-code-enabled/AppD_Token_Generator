# README for AppDynamics Token Generator Script

This project consists of three main files: `credentials.json`, `requirements.txt`, and `tokenGen.py`. The Python script (`tokenGen.py`) is designed to encrypt credentials and generate an API token based on the specified credentials, while continuously generating a new token every minute. This README provides steps on how to set up and run the script on your machine.

## Pre-requisites

1. **Python Installation**:
    - **Windows**:
        1. Download the latest version of Python from the [official website](https://www.python.org/downloads/windows/).
        2. Launch the installer.
        3. Be sure to check the box that says "Add Python x.y to PATH" before clicking "Install Now".
        4. Once the installation is complete, verify the installation and check the Python version by opening a command prompt and running: `python --version`

    - **Linux**:
        - **Ubuntu/Debian**:
            1. Update package list: `sudo apt update`
            2. Install Python: `sudo apt install python3`
        - **Fedora**:
            1. Install Python: `sudo dnf install python3`
        - **CentOS/RHEL**:
            1. Enable EPEL repository: `sudo yum install epel-release`
            2. Install Python: `sudo yum install python3`
        - Verify the installation by running: `python3 --version`

## Setup

1. **Clone/Download the Project**:
    - Clone the project to your local machine or download the zip file.
    - Navigate to the project directory, which is named `Token Generator`.

2. **Virtual Environment Setup**:
    - Navigate to the project directory in your terminal.
    - Create a virtual environment within the project directory by running: `python -m venv env` (or `python3 -m venv env` on Linux)
    - Activate the virtual environment:
        - Windows: `.\env\Scripts\activate`
        - Linux: `source env/bin/activate`

3. **Dependency Installation**:
    - While the virtual environment is active, install the necessary dependencies using the command: `pip install -r requirements.txt`

4. **Configuration**:
    - Open `credentials.json` in a text editor.
    - Update the `ACCOUNT_NAME`, `CLIENT_NAME`, and `ENCRYPTED_SECRET_KEY` fields with your own credentials.
    - Save and close the file.

## Usage

1. **Run the Script**:
    - With the virtual environment activated, run the script using the command: `python tokenGen.py` (or `python3 tokenGen.py` on Linux)
    - The script is in test mode and will print a new token to the console every minute.

2. **Stop the Script**:
    - To stop the script, simply hit `Ctrl + C` in the terminal where the script is running.

## Integration Examples

1. **Integrate with Another API**:
    - You could modify the `generate_token` function to return the token instead of printing it, then use that token in your API requests.
    ```python
    def generate_token():
        # ... rest of your code ...
        if response.status_code == 200:
            token_data = response.json()
            API_TOKEN = token_data.get("access_token")
            return API_TOKEN  # Return the token
        else:
            print(f"Failed to generate token. Status code: {response.status_code}")
            return None
    
    # Usage:
    API_TOKEN = generate_token()
    response = requests.get('https://api.example.com/endpoint', headers={'Authorization': f'Bearer {API_TOKEN}'})
    ```

2. **Set as Environment Variable**:
    - You can set the generated token as an environment variable in your system.
    ```python
    import os
    
    # ... rest of your code ...
    
    def generate_token():
        # ... rest of your code ...
        if response.status_code == 200:
            token_data = response.json()
            API_TOKEN = token_data.get("access_token")
            os.environ['API_TOKEN'] = API_TOKEN  # Set as environment variable
    ```

3. **Integration with Power BI**:
    - You can utilize the Power BI REST API and use the generated token for authentication.
    ```python
    import requests
    
    # ... rest of your code ...
    
    def generate_token():
        # ... rest of your code ...
        if response.status_code == 200:
            token_data = response.json()
            API_TOKEN = token_data.get("access_token")
            return API_TOKEN
    
    # Usage:
    API_TOKEN = generate_token()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_TOKEN}'
    }
    response = requests.post('https://api.powerbi.com/', headers=headers, json={...})
    ```

## Troubleshooting

- Ensure that the virtual environment is activated whenever you are running the script.
- Make sure all the fields in `credentials.json` are filled out correctly.
- Check the console for any error messages that may indicate what's going wrong.
  
