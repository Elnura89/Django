# Generated by Django 4.2.5 on 2023-09-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_app', '0006_alter_contacts_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='fullname',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='mail',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
