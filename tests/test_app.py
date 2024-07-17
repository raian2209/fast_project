from fastapi import FastAPI
from fastapi.testclient import TestClient

from fast_project.app import create_app


def test_create_app():
    app = create_app()
    assert isinstance(app, FastAPI)
