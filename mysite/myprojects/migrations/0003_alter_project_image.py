# Generated by Django 4.0.5 on 2022-07-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0002_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(upload_to='img/'),
        ),
    ]
