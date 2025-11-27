from django.db.models import TextChoices


class FileStatus(TextChoices):
    """
    Represents the status of checking the file that has been uploaded.
    
    In other words it represents the lifecycle of a file in the application.

    - CHECK_PENDING: File was uploaded and is waiting to be checked.
    - CHECK_SUCCESSFUL: File has been checked and no errors were found during the last check.
    - CHECK_FAILED: File has been checked and an error was found during the last check.
    """
    CHECK_PENDING = 'pending', 'Checking is pending'
    CHECK_SUCCESSFUL = 'success', 'Checked successfully'
    CHECK_FAILED = 'failed', 'Check was failed'
