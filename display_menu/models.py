from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Item(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

