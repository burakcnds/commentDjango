# Generated by Django 5.0 on 2024-04-09 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0003_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
