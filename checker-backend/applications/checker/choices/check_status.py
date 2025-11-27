from django.db.models import TextChoices


class CheckStatus(TextChoices):
    """
    Represents the status of checking of a file.
    """
    CHECK_IS_SUCCESSFUL = 'successful', 'Successful'
    CHECK_FAILED = 'failed', 'Failed'
