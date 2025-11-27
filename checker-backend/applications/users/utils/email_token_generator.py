from django.contrib.auth.tokens import PasswordResetTokenGenerator


class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):
    """
    The custom token generator that is created because the default
    django token generator (PasswordResetTokenGenerator) is not working
    with users that are inactive (is_active = False).
    """
    def _make_hash_value(self, user, timestamp):
        return f'{user.pk}{timestamp}{user.email}{user.is_active}'

email_token_generator = EmailVerificationTokenGenerator()
