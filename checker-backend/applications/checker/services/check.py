from django.core.mail import send_mail
from django.utils import timezone
from flake8.api.legacy import get_style_guide

from app_settings import app_settings

from applications.checker.models import Check, File
from applications.checker.choices import CheckStatus, FileStatus


class CheckFileService:
    """
    The service that is responsible for checking a file uploaded to the system.

    - Runs the linteration on the file that has been uploaded previously.
    - Creates an instance of Check.
    - Updates the status of the file that has been checked.
    """

    def __init__(self, id: int) -> None:
        """
        Initialize the service.

        Args:
            id (int): The id of a File.
        """
        self.file = self.get_file(id=id)
        self.check_status = None
        self.results = None
        self.check = None

    def execute(self) -> None:
        """
        Execute the process.

        - Run linteration.
        - Create an instance of Check.
        - Update checked file.
        - Send email with results.
        """
        self.run_linteration()
        self.create_check()
        self.update_file()
        self.send_mail()

    def get_file(self, id: int) -> File:
        """
        Get File by the id.

        Args:
            id (int): An id of the file that needs to be checked.

        Returns:
            File: An instance of the File.
        """
        return File.objects.get(id=id)
    
    def run_linteration(self) -> None:
        """
        Run flake8 linteration.
        """
        style_guide = get_style_guide(format='default', quiet=3)
        report = style_guide.check_files([self.file.file.path])
        total_errors = report.total_errors
        statistics = report.get_statistics('')

        report_text = f'Total errors: {total_errors}'

        for item in statistics:
            report_text += f'\n{item}'

        self.check_status = CheckStatus.CHECK_IS_SUCCESSFUL if total_errors == 0 else CheckStatus.CHECK_FAILED
        self.results = report_text
    
    def create_check(self) -> None:
        """
        Create an instance of Check and store to the database.
        """
        self.check = Check.objects.create(status=self.check_status, file=self.file, results=self.results)

    def update_file(self) -> None:
        """
        Update the checked file depending on the results of the linteration.
        """
        if self.check_status == CheckStatus.CHECK_IS_SUCCESSFUL:
            self.file.last_check_status = FileStatus.CHECK_SUCCESSFUL
        else:
            self.file.last_check_status = FileStatus.CHECK_FAILED
        
        self.file.checking_required = False
        self.file.last_checked_at = timezone.now()

        self.file.save(update_fields=['last_checked_at', 'last_check_status'])

    def send_mail(self) -> None:
        """
        Send email with check results to the user.
        """
        email = self.file.user.email

        sent = send_mail(
            subject='Check results.',
            message=f'Your file was checked.\nThe check was {self.check_status}.\nResults:\n{self.results}',
            from_email=app_settings.application_email,
            recipient_list=[email],
        )

        self.check.email_sent = bool(sent)
        self.check.save(update_fields=['email_sent'])
