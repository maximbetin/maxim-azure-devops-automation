# Azure DevOps Automation Project

## Overview
This project automates the creation of Azure DevOps projects using Python. It leverages the Azure DevOps REST API to programmatically set up new projects, provision Azure infrastructure with Terraform, configure it using Ansible, and establish CI/CD pipelines with Azure Pipelines. The goal is to demonstrate a comprehensive DevOps pipeline implementation, showcasing cloud infrastructure, automation, and continuous deployment.

## Prerequisites
- Azure DevOps account
- Azure subscription
- Python 3.10 or later
- Terraform 0.13 or later
- Ansible Core 2.16 or later

## Getting Started

### 1. Clone the Repository
Start by cloning this repository to your local machine:
```bash
git clone https://github.com/maximbetin/maxim-azure-devops-automation.git
cd maxim-azure-devops-automation
```

### 2. Configure Azure Credentials
- Generate a Personal Access Token (PAT) in Azure DevOps with appropriate permissions through the [Azure DevOps Portal](https://dev.azure.com/)

### 3. Azure DevOps Automation with Python
See the README.md located at [/python/README.md](/python/README.md).

### 4. Provision the Infrastructure with Terraform
See the README.md located at [/terraform/README.md](/terraform/README.md).

### 5. Configure the Infrastructure with Ansible
See the README.md located at [/ansible/README.md](/ansible/README.md).

### 6. Set up CI/CD with Azure Pipelines
See the README.md located at [/pipelines/README.md](/python/pipelines/README.md).