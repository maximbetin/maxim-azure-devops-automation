import api_calls
import os
import logging

# Configure basic logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Main function to execute the script
def main():
      
    logging.info('Starting script...')

    organization = 'betinmaxim'
    project_name = 'Azure DevOps Automation'
    description = 'This project is aimed at showcasing some of the features and capabilities of Azure DevOps services.'
    template_type_id = '6b724908-ef14-45cf-84f8-768b5384da45'  # Agile template type ID

    # Retrieve PAT from environment variable
    personal_access_token = os.getenv('AZURE_DEVOPS_PAT')

    if personal_access_token:
        logging.info('Personal Access Token (PAT) found.')
        logging.info('Initiating project creation...')
        api_calls.create_project(organization, personal_access_token, project_name, description, template_type_id)
    else:
        logging.error('Personal Access Token (PAT) not found. Please set it as an environment variable.')

if __name__ == "__main__":
    main()
