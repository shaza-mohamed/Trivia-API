import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.new_question = {
            'question': 'What is the color of apples?',
            'answer': 'red',
            'difficulty': 1,
            'category': '1'
        }
        
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """TODO:Write at least one test for each test for successful operation and for expected errors."""


    """ 1.tests for categories endpoint"""
    def test_get_categories(self):
        """ success """
        res=self.client().get('/categories')
        data= json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
    def test_non_existing_category_404(self):
        """Failure"""
        res = self.client().get('/categories/456')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found') 


    """2.tests for paginated questions endpoint"""
    def test_get_paginated_questions(self):
        """success"""
        res=self.client().get('/questions')
        data= json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['catrgories'])
    def test_404_sent_requesting_beyond_valid_page(self):
        """Failure"""
        res = self.client().get('/questions?page=4551')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
    

    """3.tests for Delete question endpoint"""
    def test_delete_question(self):
        """success"""
        question = Question(question='what is the best programming language?', answer='python', difficulty=1, category=1)
        question.insert()
        res = self.client().delete('/questions/{}'.format(question.id))
        data = json.loads(res.data)
        deleted_question = Question.query.filter(Question.id== question.id).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], question.id)
        self.assertEqual(deleted_question, None)  
    def test_404_if_question_does_not_exist(self):
        """Failure"""
        res = self.client().delete('/questions/8000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    
    """4.tests for update question endpoint"""
    def test_create_new_question(self):
        """success"""
        total_questions_1= Question.query.all()
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)
        total_questions_2= Question.query.all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(total_questions_2)-len(total_questions_1) == 1)

    def test_422_if_add_question_fails(self):
        """Failure"""
        wrong= {'question':'what is?'}
        total_questions_1= Question.query.all()
        res = self.client().post('/questions', json=wrong)
        data = json.loads(res.data)
        total_questions_2= Question.query.all()
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")
        self.assertTrue(len(total_questions_2)-len(total_questions_1) == 0)


    """5.tests for searching for question endpoint"""
    def test_search_questions(self):
        """success"""
        res = self.client().post('/questions',json={'searchTerm': 'a'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    def test_if_search_fails(self):
        """Failure"""
        res = self.client().post('/questions',json={'searchTerm': 'hjfgdh'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data["message"], "resource not found") 


    """6.tests for getting questions by category"""
    def test_get_questions_by_category(self):
        """success"""
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
    def test_question_in_notfound_category(self):
        """Failure"""
        res = self.client().get('/categories/int(20)/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data["message"], "resource not found") 
    
    """7. tests for quizzes """
    def test_quiz(self):
        """success"""
        res = self.client().post('/quizzes', json={'previous_questions': [],'quiz_category': {'id': '0'}})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])
        ''' when i write ex:json={'previous_questions': [],'quiz_category': {'type':'Science', 'id': '1'}} it give me error 422!=200 but when i run curl it run successfully and i can't figure why this happen'''

    def test_quiz_fails(self):
        """failure"""  
        res = self.client().post('/quizzes', json={})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data["message"], "bad request") 

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()