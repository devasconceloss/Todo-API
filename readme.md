# Todo API

REST API designed in FastAPI for Todo APP

- [Environment](#environment)
- [Installation](#installation-)
- [Run Server](#run-server-)
- [Root EndPoint](#root-endpoint)
- [Schema](#schema)
- [Todo Model](#todo-model)
- [End Points](#end-points)
- [Documentation](#documentation)
- [API Functions](#api-functions)

## Environment
To start the environment go to the terminal and type:
```commandline
source venv/bin/activate
```

## Installation:
All the packages are installed on the environment


## Run Server:
```commandline
uvicorn archive-name:app --reload
```

## Root EndPoint
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
    "status": "OK",
    "code": "200",
    "message": "Fetched all data",
    "result": [
        {
            "title": "string",
            "category": "string",
            "done": boolean,
            "id": int
        },
        {
            "title": "string",
            "category": "string",
            "done": boolean,
            "id": int
        }
    ]
}
```

## End Points

| Command | End Point        | Description                   |
|---------|------------------|-------------------------------|
| GET     | /                | Get All Todos                 |
| GET     | /todos/{id_todo} | Get Todo By Id                |
| Delete  | /todos/{id_todo} | Delete Todo                   |
| Patch   | /todos/{id_todo} | Finishing Todo                |
| POST    | /todos           | Create todo                   |
| GET     | /highest_id      | Get Highest Id on Database    |

## Documentation

````http://127.0.0.1:8000/docs````

## API Functions

- [GET /](#get-) 
- [GET /todos/{id_todo}](#get-todostodoid)
- [DELETE](#delete-todostodoid)
- [PATCH](#patch-todosidtodo)
- [POST](#post-todos)
- [GET](#get-highestid)


## GET /

* _Optional parameters:_
  * Skip: integer - Default = 0;
  * Limit: integer - Default = 100;
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
```commandline,
{
    "status": "OK",
    "code": "200",
    "message": "Fetched all data",
    "result": [
        {
            "title": "string",
            "category": "string",
            "done": boolean,
            "id": int
        },
        {
            "title": "string",
            "category": "string",
            "done": boolean,
            "id": int
        }
    ]
}
```



## GET /todos/{todo_id}

Required:
* _id_todo_


Curl
````commandline
curl -X 'GET' \
'http://127.0.0.1:8000/todo/{todo_id}' \
-H 'accept: application/json'

````

Request URL:
```
http://127.0.0.1:8000/todos/{todo_id}
```


Response:
````commandline
{
  "status": "OK",
  "code": "200",
  "message": "Fetched the selected data",
  "result": {
    "title": "string",
    "category": "string",
    "done": boolean,
    "id": int
  }
}
````

# DELETE /todos/{todo_id}

Required:
* _todo_id: integer (path)_


Curl
````commandline
curl -X 'DELETE' \
  'http://127.0.0.1:8000/todo/{todo_id}' \
  -H 'accept: application/json' \
````

Request URL
```
http://127.0.0.1:8000/todo/{id_todo}
```

Response body
```
{
  "status": "OK",
  "code": "200",
  "message": "Todo deleted",
  "result": null
}
```

# PATCH /todos/{id_todo}
_Request body:_
```
{
  "parameter": {
    "id": int,
    "title": "string",
    "category": "string",
    "done": true
  }
}
```

Curl 
````commandline
curl -X 'PATCH' \
'http://127.0.0.1:8000/todos/{todo_id}' \
-H 'accept: application/json'
````

Request URL 
````commandline
http://127.0.0.1:8000/todos/{todo_id}
````

Response body
````commandline
{
  "id": int,
  "title": "string",
  "category": "stirng",
  "done": bool
}
````

# POST /todos

Request Body 
````commandline
{
  "parameter": {
    "id": int,
    "title": "string",
    "category": "string",
    "done": true
  }
}
````

Curl
````commandline
curl -X 'POST' \
  'http://localhost:8000/todos' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "parameter": {
    "id": int,
    "title": "string",
    "category": "string",
    "done": true
  }
}'
````

Response body

````commandline
{
  "status": "Created Todo",
  "code": "201",
  "message": "Todo created successfully",
  "result": null
}
````

## GET /highest_id

* _No parameters_

Curl

```commandline
curl -X 'GET' \
  'http://localhost:8000/highest_id' \
  -H 'accept: application/json'
```

Request URL:
```commandline
http://localhost:8000/highest_id
```

Response body:
```
{
  "highest_id": int
}
``