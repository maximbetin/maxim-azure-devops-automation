import pytest
import requests_mock
from src.azure_devops import create_project, create_repository, create_pipeline

@pytest.fixture
def setup_requests_mock():
    with requests_mock.Mocker() as m:
        yield m

def test_create_project_success(setup_requests_mock):
    setup_requests_mock.post('https://dev.azure.com/test_org/_apis/projects?api-version=7.1-preview.4', status_code=202, json={"id": "test_project_id"})
    
    assert create_project('test_org', 'test_project', 'A test project', 'template_type_id') is None

def test_create_repository_success(setup_requests_mock):
    setup_requests_mock.post('https://dev.azure.com/test_org/test_project/_apis/git/repositories?api-version=7.1-preview.1', status_code=201, json={"id": "test_repo_id"})
    
    repo_id = create_repository('test_org', 'test_project', 'test_repo')
    assert repo_id == "test_repo_id"

def test_create_pipeline_success(setup_requests_mock):
    setup_requests_mock.post('https://dev.azure.com/test_org/test_project/_apis/pipelines?api-version=7.1-preview.1', status_code=202, json={"id": "test_pipeline_id"})
    
    pipeline_id = create_pipeline('test_org', 'test_project', 'test_repo', 'test_repo_id')
    assert pipeline_id == "test_pipeline_id"
