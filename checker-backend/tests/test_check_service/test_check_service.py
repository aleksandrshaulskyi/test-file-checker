from pytest import mark
from unittest.mock import patch

from applications.checker.choices import CheckStatus
from applications.checker.services import CheckFileService
from tests.test_check_service.fixtures import *


@mark.django_db
def test_bad_file(file_one):
    """
    Test that a file containing flake8 violations
    fails the validation check.
    """
    with patch('applications.checker.viewsets.file.FileViewSet.perform_create'):
        service = CheckFileService(id=file_one.id)
        service.run_linteration()

        assert service.check_status == CheckStatus.CHECK_FAILED

@mark.django_db
def test_good_file(file_two):
    """
    Test that a file that does not contain flake8 violations
    passes the validation check.
    """
    with patch('applications.checker.viewsets.file.FileViewSet.perform_create'):
        service = CheckFileService(id=file_two.id)
        service.run_linteration()

        assert service.check_status == CheckStatus.CHECK_IS_SUCCESSFUL
