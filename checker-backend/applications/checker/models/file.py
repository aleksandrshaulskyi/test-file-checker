from os.path import basename

from django.core.validators import FileExtensionValidator
from django.db import models

from main.storage import file_storage
from applications.checker.choices import FileStatus


class File(models.Model):
    """
    Infrastructure model that is used to store files uploaded by users for checking.

    It is not an instance of the domain entity.
    """
    file = models.FileField(
        storage=file_storage,
        verbose_name='Файл для проверки.',
        validators=[FileExtensionValidator(allowed_extensions=['py'])],
    )

    user = models.ForeignKey(
        to='auth.User',
        on_delete=models.CASCADE,
        related_name='files',
        verbose_name='Пользователь, загрузивший файл.',
    )

    checking_required = models.BooleanField(
        default=True,
        verbose_name='Нуждается в проверке?',
    )

    last_checked_at = models.DateTimeField(
        null=True,
        verbose_name='Дата и время последней проверки.',
    )

    last_check_status = models.CharField(
        choices=FileStatus.choices,
        default=FileStatus.CHECK_PENDING,
        verbose_name='Статус последней проверки.',
    )

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self) -> str:
        return f'{basename(self.file.name)} uploaded by {self.user.username}'
