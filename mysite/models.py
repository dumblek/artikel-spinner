from django.db import models


class Spinner(models.Model):

    def spinner(self, artikel):
        hasil = str(artikel) + ' apalah'
        return hasil