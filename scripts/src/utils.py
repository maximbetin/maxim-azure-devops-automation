from base64 import b64encode

def encode_pat(token: str):
    """Encode a personal access token for use in an HTTP header."""
    return b64encode(bytes(f':{token}', 'utf-8')).decode('utf-8')

def get_headers(pat: str):
    """Generate headers for API requests."""
    return {
        'Authorization': f'Basic {encode_pat(pat)}',
        'Content-Type': 'application/json',
    }
