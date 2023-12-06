# Book API

## Requirements:

- Python >= 3.8

## Setup:

1. Clone this repository
   ```
   python -m venv env
   ```
2. Create a virtual env
   ```
   python -m venv env
   ```
3. Activate the virtual environment
   - For Windows:
   ```
   .\env\Scripts\activate
   ```
   - For Unix or MacOS
   ```
   source env/bin/activate
   ```
4. Install dependencies
   ```
   pip install -r requirements.txt
   ```
5. Run migrations
   ```
   python manage.py migrate
   ```
6. Seed the database with mock data
   ```
   python manage.py seed_db
   ```
7. Start the development server
   ```
   python manage.py runserver
   ```

## API Documentation

### End Points:

```
GET /api/books/
POST /api/books/
GET /api/books/{id}/
PUT /api/books/{id}/
DELETE /api/books/{id}/
```

### Response/Request Format:

Response Format (GET/POST/PUT):

```
[
  {
    "id": 1,
    "title": "Example Book",
    "author": "John Doe",
    "language": "en"
  },
  ...
]
```

Request Format (POST/PUT):

```
{
  "title": "Example Book",
  "author": "John Doe",
  "language": "en"
}
```

```
NOTE: language fild is not compulsory. default is English(en)
Choices for language:
English (en)
Spanish (sp)
French (fr)
German (ge)
Hindi (hi)
```

In case of a POST request where a book with the same title, author, and language already exists: <br>
Status Code: 400 Bad Request <br>
Response Format:

```
{
  "non_field_errors": [
    "The fields title, author_name, language must make a unique set."
  ]
}
```
