import os

PREFIX = 'azure_devops_'
ORGANIZATION_NAME = 'betinmaxim'
PROJECT_NAME = PREFIX + 'project'
REPOSITORY_NAME = PREFIX + 'repo'
PIPELINE_NAME = PREFIX + 'pipeline'
PIPELINE_FILE_NAME = 'azure-pipeline.yml'
TEMPLATE_TYPE_ID = '6b724908-ef14-45cf-84f8-768b5384da45'
DESCRIPTION = 'This project is aimed at showcasing some of the features and capabilities of Azure DevOps services.'

PERSONAL_ACCESS_TOKEN = os.getenv('AZURE_DEVOPS_PAT')
