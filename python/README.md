# Azure DevOps Automation with Python

## Overview

This Python project automates the creation of projects, repositories, and pipelines in Azure DevOps using its REST API. It simplifies the initial setup for Azure DevOps resources, enabling developers and DevOps engineers to programmatically manage their Azure DevOps environment.

## Prerequisites

- **Python 3.10+**: Ensure Python is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- **Azure DevOps Account**: You need an Azure DevOps account and sufficient permissions to create projects, repositories, and pipelines.
- **Personal Access Token (PAT)**: A PAT with appropriate permissions for creating and managing Azure DevOps resources.

## Project Structure

The project is organized to ensure easy navigation and scalability:

- **`src/` Directory**: Contains the main Python scripts for the project, including:
  - **`azure_devops.py`**: Functions for interacting with Azure DevOps REST API.
  - **`config.py`**: Configuration settings, including Azure DevOps organization details and PAT.
  - **`main.py`**: The entry point of the script, orchestrating the creation of projects, repositories, and pipelines.
  - **`utils.py`**: Utility functions, such as for encoding the PAT.
- **`tests/` Directory**: Contains unit tests for the project.
    - **`test_azure_devops.py`**: Unit tests for the functions interacting with the Azure DevOps REST API.
- **`requirements.txt`**: Lists all the Python package dependencies.
- **`pipelines/` Directory**: Includes example YAML pipeline configurations.

## Variables and Sensitive Data Handling

The project uses environment variables and a `config.py` file to manage sensitive and configuration data securely:

### Environment Variables

- **PAT Storage**: The Personal Access Token is stored as an environment variable to avoid hardcoding sensitive information in source files. It is accessed within `config.py`.

### Configuration File

- **`config.py`**: Centralizes non-sensitive configuration settings, such as the Azure DevOps organization name and project details. Sensitive data, like the PAT, is loaded from environment variables.

## Getting Started

### Step 1: Configure Environment Variables

Set up the required environment variable for the PAT:

```bash
export PERSONAL_ACCESS_TOKEN="your_personal_access_token_here"
```

For Windows Command Prompt, use `set` instead of `export`. For PowerShell, use `$env:PERSONAL_ACCESS_TOKEN="your_personal_access_token_here"`.

### Step 2: Install Dependencies

Install the required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Script

Execute the main script to start creating your Azure DevOps resources:

```bash
python src/main.py
```

## Testing

Unit tests are provided in the `tests/` directory. To run the tests, ensure you have `pytest` and any other testing dependencies installed:

```bash
pytest tests/
```

# TODO:
Implement proper retry logic
Make the code more modular
Fix Pipeline Creation
