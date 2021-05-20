
# Note-Web-App Backend API

A brief description of what this project does and who it's for


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
  POST api/user/create
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**. Your email |
| `password` | `string` | **Required**. Your password |
| `name` | `string` | **Required**. Your name |


#### Authenticate User

```http
  POST /api/user/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email` | `string` | **Required**. Your email |
| `password` | `string` | **Required**. Your password |



  
