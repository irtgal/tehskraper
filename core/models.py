from django.db import models

PAGE_CHOICES = (
	('st', 'https://slo-tech.com/'),
	('mn', 'https://www.monitor.si/')
)
class Story(models.Model):
	page =models.CharField(max_length=3, choices=PAGE_CHOICES)
	date = models.DateTimeField(auto_now_add=False)
	slug = models.URLField(max_length=200)
	summary = models.TextField(blank=True, null=True)
	title = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return f'{self.page} - {self.title}'

	class Meta:
		verbose_name_plural = "Stories"
