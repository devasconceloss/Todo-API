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
  0: {
    "id": int,
    "title": "string",
    "category": "string",
    "done": bool
  },
  1: {
    "id": int,
    "title": "string",
    "category": "string",
    "done": bool
  }
}
```

## End Points

| Command | End Point       | Description                 |
|---------|-----------------|-----------------------------|
| GET     | /               | List all todos              |
| GET     | /todo/{id_todo} | List todo by id             |
| PUT     | /todo/          | Update todo by id           |
| Delete  | /todo/{id_todo} | Delete todo by id           |
| Patch   | /todo/{id_todo} | Partial update by Field Id  |
| POST    | /todo/          | Create todo                 |


## Documentation

````http://127.0.0.1:8000/docs````

## API Functions

- [GET /](#get-) 
- [GET /todo/{id_todo}](#get-todoid_todo)
- [PUT](#put-todoid_todo)
- [DELETE](#delete-todoid_todo)
- [PATCH](#patch-todoid_todo)
- [POST](#post-todo)




## GET /

* _No parameters_
* _No request body_

Curl
````commandline
curl -X 'GET' \
'http://127.0.0.1:8000/' \
-H 'accept: application/json'

````

Request URL
```
http://127.0.0.1:8000/
```

Response body
```
  {
  "0": {
    "id": 1,
    "title": "string",
    "category": "string",
    "done": true
  },
  "1": {
    "id": 2,
    "title": "test",
    "category": "work",
    "done": false
  }
}
```



## GET /todo/{id_todo}

Required:
* _id_todo_


Curl
````commandline
curl -X 'GET' \
'http://127.0.0.1:8000/todo/{id_todo}' \
-H 'accept: application/json'

````

Request URL:
```
http://127.0.0.1:8000/todo/{id_todo}
```


Response:
````commandline
{
  "id": int,
  "title": "string",
  "category": "string",
  "done": bool
}
````


# PUT /todo/{id_todo}

Required:
* _id_todo_
* _Request body_

Curl
````commandline
curl -X 'PUT' \
  'http://127.0.0.1:8000/todo/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 2,
  "title": "testando",
  "category": "string",
  "done": false
}
````

Request URL
```
http://127.0.0.1:8000/todo/{id_todo}
```

Response body
```
{
  "id": int,
  "title": "string",
  "category": "string",
  "done": bool
}
```
# DELETE /todo/{id_todo}

Required:
* _id_todo_


Curl
````commandline
curl -X 'DELETE' \
  'http://127.0.0.1:8000/todo/{id_todo}' \
  -H 'accept: application/json' \
````

Request URL
```
http://127.0.0.1:8000/todo/{id_todo}
```

Response body
````
{
  "0": {
    "id": int,
    "title": "string",
    "category": "string",
    "done": bool
  },
  "1": {
  "id": int,
  "title": "string",
  "category": "string",
  "done": bool
  }
}
````

# PATCH /todo/{id_todo}
Required:
* _id_todo_
* _id_field_
* _new_value_

Curl 
````commandline
curl -X 'PATCH' \
'http://127.0.0.1:8000/todo/1?id_field=4&new_value=true' \
-H 'accept: application/json'
````

Request URL 
````commandline
http://127.0.0.1:8000/todo/{id_todo}?id_field={id_field}&new_value={new_value}
````

Response body
````commandline
{
  "id": 10,
  "title": "aa",
  "category": "work",
  "done": "true"
}
````

# POST /todo/

Request Body 
````commandline
{
  "id": 4,
  "title": "string",
  "category": "string",
  "done": true
}
````

Curl
````commandline
curl -X 'POST' \
  'http://127.0.0.1:8000/todo/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": int,
  "title": "string",
  "category": "string",
  "done": bool
}'
````

Response body

````commandline
{
  "id": int,
  "title": "string",
  "category": "string",
  "done": bool
}
````