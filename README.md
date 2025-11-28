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

    Everything else works as requests. Files are loaded when accessing the index page (if logged in). Checks will be done both on upload and update a File.
    An email will be sent upon the check completion.

## Additional.

Every additional task is completed.

1) Created testing scaffolding with Pytest. In order to run execute:  
    - ```docker exec -it django bash```
    - ```pytest```

2) Email verification implemented. Upon registration a user is created as inactive (is_active flag is set to False).  
   A custom link that contains a one-time token is the generated and sent to a user email address.  
   After user requests such link his profile is switched to active.  
   Login is disabled for the inactive users.  

3) A completely separated process runs in a different container to collect garbage (unbound files in storage.)  
   This allows us to do the scheduled task in a fancy way avoid the need of manipulating Gunicorn workers
   in order to prevent forked workers from executing the same job. It is also fancier than running such task in a different
   thread.

   Aside that, a normal celery task is scheduled to run every hour to do exactly same thing.

4) All the variables are stored in the .env file and accessed using Pydantic settings module.
