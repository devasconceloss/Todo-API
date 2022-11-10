# Todo API

REST API designed in FastAPI for Todo APP

## Requirements
Python 3.7+, FastAPI package and ASGI Server.

Check your python and pip version:

```python --version```
```pip --version or -V```

## Installation:

```pip install fastapi```

```pip install "uvicorn[standard]```


## Root End Point
```http://127.0.0.1:8000/```

You can change the port for whatever you want using:

```--port=Number```


## Schema
- All API access is based on HTTP;
- All Data is in JSON type;


## Todo Model
This is the schema used by now, date for creation and finalization of the todos will be used in the future.

```commandline,

{
  "0": {
    "id": int,
    "title": "string",
    "category": "string",
    "done": true
  },
  "1": {
    "id": int,
    "title": "string",
    "category": "string",
    "done": true
  }
}
```

## End Points

| Command | End Point       | Description       |
|---------|-----------------|-------------------|
| GET     | /               | List all todos    |
| GET     | /todo/{id_todo} | List todo by id   |
| PUT     | /todo/          | Update todo by id |
| POST    | /todo/          | Create todo       |