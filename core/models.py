from django.db import models
from datetime import datetime

from django.db.models import CharField
from django.db.models.functions import Unaccent

PAGE_CHOICES = (
	('st', 'Slo-tech'),
	('mn', 'Monitor')
)
class Story(models.Model):
	page =models.CharField(max_length=3, choices=PAGE_CHOICES)
	date = models.DateTimeField(auto_now_add=False)
	slug = models.URLField(max_length=200)
	summary = models.TextField(blank=True, null=True)
	title = models.CharField(max_length=255, blank=True, null=True)
	seen = models.BooleanField(default=False)
	saved = models.BooleanField(default=False)
	saved_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return f'{self.page} - {self.title}'

	class Meta:
		verbose_name_plural = "Stories"

	def pretty_date(self):
		return self.date.strftime("%d. %b %Y %H:%M")

	def pretty_page(self):
		return [full for (short, full) in PAGE_CHOICES if short == self.page][0]
