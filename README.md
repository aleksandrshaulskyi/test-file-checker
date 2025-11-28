







# Test-file-checker.

The application that allows you to run online flake8 validation of your python files.

## Disclaimer.

Frontend is not optimized. It will not handle errors or pending state of requests.
And obviously it is not flexible at all.

Was developed and tested only in Chrome on MacOS 26.

## Test yorself.

http://shaulskyi.com

## Test locally.

For the sake of simplicity all containers are groupped in single docker-compose file.
Everything that you need to do in order to run this application locally is:

1) Create an .env file in **checker-backend** directory using the env_example in the same directory.
2) Run ```docker-compose up -d --build```.

That is it. Application will be accessible on **http://localhost/**

## Features.

1) Authentication.
    - Create a user.
    - Login as a user.

    No logout feature provided as I have not found it in the test task. Be sure to delete csrf token and session id
    from application cookies if you want to switch users.

2) File checking.
    - Get files.
    - Upload a file.
    - Delete a file.

    In the test task it is mentioned that a post request on /file/1/ should update the file.
    This is considered an **antipattern**.
    Insted such url accepts patch requests as it should.
    A new file sent to this endpoint will be bound to an existing entity. All previous checks will be deleted
    and new one will be ran upon upload.

    Everythin else works as requests. Files are loaded when accessing the index page (if logged in). Checks will be done both on upload and update a File.
    An email will be sent upon the check completion.