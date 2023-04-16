from django.db import models

import users.models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    city = models.CharField(max_length=50)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(
        to=Company,
        on_delete=models.CASCADE,
        related_name='companies',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class JobApplication(models.Model):
    user = models.ForeignKey(
        to= users.models.CustomUser,
        on_delete=models.CASCADE,
        related_name='job_applications'
    )
    vacancy = models.ForeignKey(
        to=Vacancy,
        on_delete=models.CASCADE,
        related_name='job_applications'
    )

    def __str__(self):
        return f'{self.user.email} -- {self.vacancy.name}'