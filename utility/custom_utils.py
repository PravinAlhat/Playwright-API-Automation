import pytest
from utility.utils import Variables as V
import playwright
from playwright.sync_api import sync_playwright
import os, shutil, pathlib, fnmatch
from pathlib import Path


def payload(name, job):
    body = {
        "name":name,
        "job":job
    }
    return body    

def delete_user(context, url, endpoint, delete_id):
    endpoint = endpoint.replace("id", delete_id)
    url = url + endpoint
    response = context.delete(url) 
    return response

def create_user(context, url, endpoint, name, job):
    url = url + endpoint
    data = payload(name, job)
    response = context.post(url, data=data)
    return response

def list_single_user(context, url, endpoint, user_id):
    endpoint = endpoint.replace("id", user_id)
    url = url + endpoint
    response = context.get(url)
    return response

def list_user(context, url, endpoint):
    url = url + endpoint
    response = context.get(url)
    return response

def get_project_root() -> Path:
    return Path(__file__).parent.parent

def move_dir(pattern: str = '*.log'):
    source_dir = get_project_root()
    destination_dir = os.path.join(source_dir, 'logs')
    if not os.path.isdir(destination_dir):
        pathlib.Path(destination_dir).mkdir(parents=True, exist_ok=True)
    for f in fnmatch.filter(os.listdir(source_dir), pattern):
        shutil.move(os.path.join(source_dir, f), os.path.join(destination_dir, f))

def single_invalid_user(context, url, endpoint):
    url = url + endpoint
    response = context.get(url)
    return response