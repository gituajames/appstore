from django.db import models


class maps(models.Model):
    map_title = models.CharField(max_length=50)
    map_sheet_number = models.IntegerField()

    def __str__(self):
        return self.map_title
