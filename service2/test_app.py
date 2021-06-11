import pytest
from flask import Flask, app, redirect, render_template, request,url_for 
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase
from sqlalchemy import desc
import requests
from os import getenv

from app import app

class testbase(TestCase):
    def create_app(self):
        return app

# Write a test class for testing that the index / about page loads.
class TestViews(testbase):

    def test_aesthetic_get(self):
        response = self.client.get(url_for('aesthetic'))
        self.assertEqual(response.status_code, 200)
