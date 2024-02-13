from base64 import b64encode
import logging
from .config import PERSONAL_ACCESS_TOKEN

def encode_pat(token: str):
    """Encode a personal access token for use in an HTTP header."""
    return b64encode(bytes(f':{token}', 'utf-8')).decode('utf-8')

def get_headers():

    if PERSONAL_ACCESS_TOKEN is None:
        logging.error('Personal Access Token is not set. Exiting...')
        return

    logging.debug('Personal Access Token is set.')    
    """Generate headers for API requests."""
    return {
        'Authorization': f'Basic {encode_pat(PERSONAL_ACCESS_TOKEN)}',
        'Content-Type': 'application/json',
    }
