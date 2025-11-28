from os.path import basename
from django.db import models

from applications.checker.choices import CheckStatus


class Check(models.Model):
    """
    Infrastructure model that is used to store performed files checks.
    """
    status = models.CharField(
        choices=CheckStatus.choices,
        verbose_name='Статус проверки.',
    )

    file = models.ForeignKey(
        to='checker.File',
        on_delete=models.CASCADE,
        related_name='checks',
        verbose_name='Файл, для которого производилась проверка.',
    )

    datetime = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время проверки.',
    )

    results = models.TextField(
        verbose_name='Результаты проверки.',
    )

    email_sent = models.BooleanField(
        default=False,
        verbose_name='Письмо отправлено?',
    )

    class Meta:
        verbose_name = 'Check'
        verbose_name_plural = 'Checks'

    def __str__(self) -> str:
        return f'Check of {basename(self.file.file.name)} attempted at {self.datetime}'
