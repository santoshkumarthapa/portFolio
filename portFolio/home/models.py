# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Myprofile(models.Model):
    cmp_nm = models.CharField(db_column='CMP_NM', max_length=10)  # Field name made lowercase.
    designation = models.CharField(db_column='DESIGNATION', max_length=10)  # Field name made lowercase.
    rspbty = models.CharField(db_column='RSPBTY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    st_dt = models.DateField(db_column='ST_DT', blank=True, null=True)  # Field name made lowercase.
    ed_dt = models.DateField(db_column='ED_DT', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.IntegerField(db_column='EMP_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'myprofile'


