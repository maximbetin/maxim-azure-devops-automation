import requests
from .utils import get_headers
from .config import PERSONAL_ACCESS_TOKEN
import logging

if PERSONAL_ACCESS_TOKEN is None:
    logging.error('Personal Access Token (PAT) not found. Please set it as an environment variable.')
    exit(1)

logging.debug('Personal Access Token (PAT) found.')
headers = get_headers(PERSONAL_ACCESS_TOKEN)

def create_project(organization_name: str, project_name: str, description: str, template_type_id: str):
    """Create a new Azure DevOps project."""
    url = f'https://dev.azure.com/{organization_name}/_apis/projects?api-version=7.1-preview.4'
    
    payload = {
        "name": project_name,
        "description": description,
        "capabilities": {
            "versioncontrol": {"sourceControlType": "Git"},
            "processTemplate": {"templateTypeId": template_type_id}
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 202:
        logging.info(f'Project created successfully. ID: {response.json().get("id")}')
    else:
        logging.error(f'Failed to create project. HTTP Status code: {response.status_code}, Message: {response.text}')


def create_repository(organization_name: str, project_id: str, repository_name: str):
    """Create a new repository in Azure DevOps project."""

    url = f'https://dev.azure.com/{organization_name}/{project_id}/_apis/git/repositories?api-version=7.1-preview.1'

    payload = {
        "name": repository_name,
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        logging.info(f'Repository created successfully. ID: {response.json().get("id")}')
        return response.json().get('id')
    
    else:
        logging.error(f'Failed to create repository. HTTP Status code: {response.status_code}, Message: {response.text}')


def create_pipeline(organization_name: str, project_id: str, repository_name: str, repository_id: str):
    """Create a new Azure DevOps pipeline."""
    url = f"https://dev.azure.com/{organization_name}/{project_id}/_apis/pipelines?api-version=7.1-preview.1"

    payload = {
        "name": "Test Pipeline",
        "folder": "Test Folder",
        "configuration": {
            "type": "yaml",
            "path": "azure-pipeline.yml",
            "repository": {
                "id": repository_id,
                "name": repository_name,
                "type": "azureReposGit",
                "url": f"https://dev.azure.com/{organization_name}/_git/{repository_name}",
                "defaultBranch": "refs/heads/master",
                "clean": "null"
            },
        },
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code in [200, 201, 202]:
        logging.info(f"Pipeline created successfully. ID: {response.json().get('id')}")
        return response.json().get('id')
    else:
        logging.error(f"Failed to create pipeline. HTTP Status code: {response.status_code}, Message: {response.text}")

