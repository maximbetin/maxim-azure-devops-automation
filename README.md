# Azure DevOps Automation Project

## Overview
This project automates the creation of Azure DevOps projects using Python. It leverages the Azure DevOps REST API to programmatically set up new projects, provision Azure infrastructure with Terraform, configure it using Ansible, and establish CI/CD pipelines with Azure Pipelines. The goal is to demonstrate a comprehensive DevOps pipeline implementation, showcasing cloud infrastructure, automation, and continuous deployment.

## Prerequisites
- Azure DevOps account
- Azure subscription
- Python 3.6 or later
- Terraform 0.12 or later
- Ansible 2.9 or later

## Getting Started

### 1. Clone the Repository
Start by cloning this repository to your local machine:
```bash
git clone https://github.com/maximbetin/maxim-azure-devops-automation.git
cd maxim-azure-devops-automation
```

### 2. Install Python Dependencies
Install the required Python packages by running:
```
pip install -r requirements.txt
```

### 3. Configure Azure Credentials
- Generate a Personal Access Token (PAT) in Azure DevOps with appropriate permissions through the [Azure DevOps Portal](https://dev.azure.com/)

### 4. Create an Azure DevOps Project
Run the Python script to create a new Azure DevOps project:
```
python3 scripts/main.py
```

### 5. Provision the Infrastructure with Terraform
See the README.md located at [/terraform/README.md](/terraform/README.md).

### 6. Configure the Infrastructure with Ansible
See the README.md located at [/ansible/README.md](/ansible/README.md).

### 7. Set up CI/CD with Azure Pipelines
See the README.md located at [/pipelines/README.md](/pipelines/README.md).

## TODO:
Write Ansible Code to configure the VM
Encrypt Ansible variables
Write code to create Azure Repos, Azure Pipelines
Configure the Pipeline to deploy to a VM
Script to destroy the unneeded stuff