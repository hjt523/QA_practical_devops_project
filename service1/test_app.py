import pytest
from flask import Flask, redirect, render_template, request,url_for 
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase
from unittest.mock import patch
from sqlalchemy import desc
import requests
from os import getenv

# import the app's classes and objects
from app import app, prior, db

class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        # Create test Entries
        sample = prior(doodle="Test Statement")

        # save users to database
        
        db.session.add(sample)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


# Write a test class for testing that the index / about page loads.
class TestViews(TestBase):

    def test_index_get(self):
        with patch('requests.get') as g:
            g.return_value.text = "test"
            with patch('requests.post') as p:
                p.return_value.text = "test"
                response = self.client.get(url_for('main'))
                self.assertEqual(response.status_code, 200)
                self.assertIn(b'Idea', response.data)
                self.assertIn(b'Doodle', response.data)
                self.assertIn(b'Test Statement', response.data)
        
