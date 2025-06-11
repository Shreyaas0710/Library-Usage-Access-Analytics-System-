from django.db import models

class Book(models.Model):
    sno = models.AutoField(db_column='Sno', primary_key=True)
    reg_no = models.CharField(max_length=20, db_column='reg_no')
    program_title = models.CharField(max_length=200, db_column='program_title')
    date = models.DateField(db_column='date')
    services_required = models.TextField(db_column='services_required')
    auditorium_name = models.CharField(max_length=100, db_column='auditorium_name')
    requestor_detail = models.TextField(db_column='requestor_details')

    class Meta:
        db_table = 'one'
        managed = False


class Ebook(models.Model):
    sno = models.IntegerField(primary_key=True)  # replace with actual field name if different
    book_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20)
    english_name= models.CharField(max_length=255)
    year_of_publish = models.IntegerField()
    publisher_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'three'
        managed = False

    def __str__(self):
        return self.title
