from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    referencenumber = models.CharField(max_length=255)
    # url
    company = models.CharField(max_length=255)
    sourcename = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.CharField(max_length=255)
    

    """
    Add the following for a sponsored job
    """
    # salary
    # education
    # jobtype
    # category
    # experience
    # sponsored = models.CharField(max_length=255)
    # budget = models.IntegerField()
    # phone = models.CharField(max_length=11)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/jobs/%i/" % self.id