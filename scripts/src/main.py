import logging
from src.azure_devops import create_project, create_pipeline, create_repository
from src.config import (
    ORGANIZATION_NAME,
    PROJECT_NAME,
    DESCRIPTION,
    TEMPLATE_TYPE_ID,
    REPOSITORY_NAME,
)

def setup_logging():
    """Configures the logging format and level."""
    logging_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=logging_format)

def main():
    """Main entry point of the script."""
    setup_logging()
    logging.debug('Starting script...')

    logging.info('Initiating project creation...')
    create_project(
        ORGANIZATION_NAME,
        PROJECT_NAME,
        DESCRIPTION,
        TEMPLATE_TYPE_ID
    )

    logging.info('Initializing repository creation...')
    repository_id = create_repository(
        ORGANIZATION_NAME,
        PROJECT_NAME,
        REPOSITORY_NAME
    )

    if repository_id is None:
        logging.error('Failed to create repository. Exiting...')
        return
    
    logging.info('Initiating pipeline creation...')
    create_pipeline(
        ORGANIZATION_NAME,
        PROJECT_NAME,
        REPOSITORY_NAME,
        repository_id
    )

    logging.debug('Script execution completed.')

if __name__ == "__main__":
    main()
