# Generated by Django 2.0.7 on 2018-10-20 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0003_answer_modified_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('-created',)},
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='pub_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='pub_date',
            new_name='created',
        ),
    ]
