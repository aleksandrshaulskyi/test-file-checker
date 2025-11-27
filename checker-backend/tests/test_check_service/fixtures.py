from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from pytest import fixture

from applications.checker.models import File


@fixture
def bad_file() -> SimpleUploadedFile:
    """
    Returns:
        SimpleUploadedFile: A file that is supposed to fail the check.
    """
    content = b'import os\n'

    return SimpleUploadedFile(
        name='bad_file.py',
        content=content,
        content_type='text/x-python'
    )

@fixture
def good_file() -> SimpleUploadedFile:
    """
    Returns:
        SimpleUploadedFile: A file that is supposed to pass the check.
    """
    content = b'def test():\n    return 8\n'

    return SimpleUploadedFile(
        name='good_file.py',
        content=content,
        content_type='text/x-python'
    )

@fixture
def user() -> User:
    """
    Returns:
        User: An instance of User.
    """
    return User.objects.create_user(username='test', password='test')

@fixture
def file_one(user, bad_file) -> File:
    """
    Returns:
        File: An instance of a File that is supposed to fail the check.
    """
    return File.objects.create(
        file=bad_file,
        user=user,
    )

@fixture
def file_two(user, good_file) -> File:
    """
    Returns:
        File: An instance of a File that is supposed to pass the check.
    """
    return File.objects.create(
        file=good_file,
        user=user,
    )
