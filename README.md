# Note-Web-App Backend API

A backend for [Notes-Web-App](https://github.com/paul3bin/notes-web-app) using Django and Django-REST-Framework

## Installation

1. To build the container run

```bash
  docker-compose build
```

2. To create migration files

```bash
  docker-compose run --rm backend sh -c "python3 manage.py makemigrations"
```

3. To migrate the db models

```bash
  docker-compose run --rm backend sh -c "python3 manage.py migrate"
```

4. To run the application locally

```bash
  docker-compose up
```

## API Reference

#### Create/Register

```http
  POST /api/user/create
```

| Parameter  | Type     | Description                 |
| :--------- | :------- | :-------------------------- |
| `email`    | `string` | **Required**. Your email    |
| `password` | `string` | **Required**. Your password |
| `name`     | `string` | **Required**. Your name     |

#### Authenticate User

```http
  POST /api/user/token
```

| Parameter  | Type     | Description                 |
| :--------- | :------- | :-------------------------- |
| `email`    | `string` | **Required**. Your email    |
| `password` | `string` | **Required**. Your password |

#### Get Notes List

```http
  GET /api/note/get
```

Headers -> Authorization: Token

#### Create New Note

```http
  POST /api/note/create
```

Headers -> Authorization: Token

| Parameter | Type     | Description              |
| :-------- | :------- | :----------------------- |
| `title`   | `string` | **Required**. Note Title |
| `body`    | `string` | **Required**. Note Body  |
| `user`    | `string` | **Required**. User ID    |

#### Get Details of Specific Note

```http
  GET /api/note/get/<str:pk>
```

Headers -> Authorization: Token

#### Update Note

```http
  PUT /api/note/update/<str:pk>
```

Headers -> Authorization: Token

| Parameter | Type     | Description              |
| :-------- | :------- | :----------------------- |
| `title`   | `string` | **Required**. Note Title |
| `body`    | `string` | **Required**. Note Body  |
| `user`    | `string` | **Required**. User ID    |

#### Delete Note

```http
  DELETE /api/note/delete/<str:pk>
```

Headers -> Authorization: Token
