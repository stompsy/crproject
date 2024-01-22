from django.db import models


# Create your models here.
class Agency(models.Model):
    id = models.AutoField(primary_key=True)
    agency_name = models.CharField(max_length=100)
    agency_description = models.TextField()
    # agency_logo = models.ImageField(upload_to="images/")
    agency_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.agency_name}"


class AgencyTypes(models.Model):
    id = models.AutoField(primary_key=True)
    agency_id = models.ForeignKey(Agency, on_delete=models.CASCADE)
    agency_type_name = models.CharField(max_length=100)
    agency_type_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.agency_type_name}"
