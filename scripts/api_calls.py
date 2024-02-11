import requests
from base64 import b64encode
from main import logging

# Function to encode PAT for authentication
def encode_pat(token: str) -> str:
    return b64encode(bytes(f':{token}', 'utf-8')).decode('utf-8')

# Function to create Azure DevOps project
def create_project(organization: str, personal_access_token: str, project_name: str, description: str, template_type_id: str) -> None:
    
    url = f'https://dev.azure.com/{organization}/_apis/projects?api-version=6.0'
    
    headers = {
        'Authorization': f'Basic {encode_pat(personal_access_token)}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        "name": project_name,
        "description": description,
        "capabilities": {
            "versioncontrol": {
                "sourceControlType": "Git"
            },
            "processTemplate": {
                "templateTypeId": template_type_id 
            }
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 202:
        logging.info('Project creation request sent successfully.')
    else:
        logging.error('HTTP %s: %s', response.status_code, response.json())
