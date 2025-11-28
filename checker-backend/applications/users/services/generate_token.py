







from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from app_settings import app_settings

from applications.users.utils import email_token_generator


class GenerateActivationLinkService:
    """
    This service generates a link to verify a user's email and activate a user.
    """

    def __init__(self, id: User) -> None:
        """
        Initialize the service.

        Args:
            user (User): An instance of User for whom we need to generate an activation link.
        """
        self.user = self.get_user(id=id)
        self.link = None

    def execute(self) -> None:
        """
        Execute the process.
        """
        self.generate_link()
        self.send_link()

    def get_user(self, id: int) -> None:
        """
        Get the user by the id that was provided.

        Args:
            id (int): An integer that represents the id of the User that we need to generate a link for.
        """
        return User.objects.get(id=id)

    def generate_link(self) -> None:
        """
        Compose a link using generated token and the instance of User.
        """
        uid = urlsafe_base64_encode(force_bytes(self.user.id))
        self.token = email_token_generator.make_token(user=self.user)
        self.link = f'http://shaulskyi.com/api/users/verify-email/?uid={uid}&token={self.token}'

    def send_link(self) -> None:
        """
        Send an email to the User to activate his account.
        """
        send_mail(
            subject='Activate your account.',
            message=f'Hi, use link {self.link} in order to activate account.',
            from_email=app_settings.application_email,
            recipient_list=[self.user.email],
        )
