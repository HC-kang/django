# Generated by Django 4.0.3 on 2022-05-24 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='modified_date',
            new_name='modify_date',
        ),
    ]
