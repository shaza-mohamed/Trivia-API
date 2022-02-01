# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History"
'5' : "Entertainment",
'6' : "Sports"}


GET '\questions?page=<page_number>'
- Fetches a dictionary of paginated questions of all categories
- Request Arguments(optional): page number(int)
- Returns: 1.List of questions, 2.Dictionary of Category id  and Category type 3. total number of questions
- response example:
  "catrgories": {
    "1": "art",
    "2": "science"
  },
  "current_category": null,
  "questions": [
    [
      {
        "answer": "anwer1",
        "category": "art",
        "difficulty": 5,
        "id": 1,
        "question": "question1"
      }
    ]
  ],
  "success": true,
  "total_questions": 1
}

DELETE '/questions/<question_id>' 
- Delete an existing questions from the repository of all questions
- Request arguments: question_id:int
-return: id of deleted question upon success, list of current questions and number of total questions 
-Example:
  "deleted": 6,
  "questions": [
    {
      "answer": " answer1 ",
      "category": "1",
      "difficulty": 5,
      "id": 1,
      "question": "question 1"
    },
  ],
  "success": true,
  "total_questions": 1
}

POST '/questions'
If no search term is included in request:

- Creates a new question using JSON request parameters.
- Request Body: {question:string, answer:string, difficulty:int, category:string}
- returns: id of created question, list of question  and total questions. 
- response example:
  "created": 8,
  "questions": [
    {
      "answer": " answer1 ",
      "category": "1",
      "difficulty": 5,
      "id": 1,
      "question": "question 1"
    },
    {
      "answer": "Michigan",
      "category": "3",
      "difficulty": 3,
      "id": 8,
      "question": "Which US state contains an area known as the Upper Penninsula?"
    }
  ],
  "success": true,
  "total_questions": 2
}

If search term is included in request:
- Searches for questions using search term in JSON request body.
- Request body: {searchTerm:string}
- Returns paginated matching questions.
-Example curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "question"}.
-response:
  "Questions": [
    {
      "answer": " answer1 ",
      "category": "1",
      "difficulty": 5,
      "id": 1,
      "question": "question 1"
    },
  ],
  "success": true,
  "total_questions": 2
}

GET '/categories/<int:id>/questions'
- Gets questions by category id using request arguments 
- Request argument: category id 
- returns: JSON object with paginated questions of specific category.
- response example:
{
  "current_category": "art", 
  "questions": [
    {
      "answer": " answer1 ",
      "category": "1",
      "difficulty": 5,
      "id": 1,
      "question": "question 1"
    },
  ],
  "success": true,
  "total_questions": 2
}

POST '/quizzes'
- allow user to play quiz game
- Returns JSON object with random question whic is in a chosen category(optional) and not among previous questions.
- Request body: {previous_questions: [], quiz_category: {id:int, type:string}}
- response example:
  "question": {
    "answer": "answer",
    "category": "art",
    "difficulty": 4,
    "id": 3,
    "question": "question"
  },
  "success": true
}


```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```