# Generated by Django 5.0.1 on 2024-01-20 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_soil', '0002_test_soil_user_alter_test_soil_soil_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test_soil',
            old_name='user',
            new_name='usersd',
        ),
    ]
