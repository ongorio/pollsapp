from django.db import models

# Create your models here.
class Poll(models.Model):
    title = models.CharField('Title', max_length=255)
    description = models.CharField('Description', max_length=500)

    class Meta:
        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'


class Option(models.Model):
    text = models.CharField('Text', max_length=255)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='options')
    # help_text = models.CharField('Help Text', max_length=255)

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'


class Response(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='responses')
    
    class Meta:
        verbose_name = 'Response'
        verbose_name_plural = 'Responses'