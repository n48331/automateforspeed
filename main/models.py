from django.db import models

# Create your models here.
class Files(models.Model):
    id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=20, unique=False)
    date = models.DateField(auto_now_add=True)
    excel_file = models.FileField(upload_to='excel/')
    pdf_file = models.FileField(upload_to='pdf/')

    def __str__(self):
        return f"{self.id} - {self.date}"