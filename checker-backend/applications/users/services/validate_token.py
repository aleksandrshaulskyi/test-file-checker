from django.contrib.auth.models import User
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from applications.users.utils import email_token_generator


class ValidateTokenService:
    """
    This service is responsible for the validation of a one-time token
    issued for the purpose of email validation using django built-in
    PasswordResetTokenGenerator.
    """

    def __init__(self, uid: bytes, token: str) -> None:
        """
        Initialize the service.

        Args:
            uid (bytes): A string that contains the id of a user.
            token (str): A token issued by the application previosly.
        """
        self.uid = uid
        self.token = token
        self.user = None

    def execute(self) -> None:
        """
        Execute the process.

        - Get the user.
        - Validate the provided token.
        - Update the user.
        """
        self.get_user()
        self.validate_token()
        self.update_user()

    def get_user(self) -> None:
        """
        Get an instance of User if any exist with the provided uid.

        Raises:
            UserNotFoundException: If no User with the id that has been retrieved exists.
        """
        user_id = force_str(urlsafe_base64_decode(self.uid))

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise Exception
        self.user = user

    def validate_token(self) -> None:
        """
        Validates the token using the same generator it was created with.
        """
        if not email_token_generator.check_token(user=self.user, token=self.token):
            raise Exception

    def update_user(self) -> None:
        """
        Activate the user if all the checks were successful.
        """
        self.user.is_active = True
        self.user.save(update_fields=['is_active'])
