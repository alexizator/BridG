# Generated by Django 2.0.7 on 2018-10-20 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0007_question_upvotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
