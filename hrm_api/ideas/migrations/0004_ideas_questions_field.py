# Generated by Django 3.2 on 2021-10-12 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_change_idea_to_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='questions',
            field=models.ManyToManyField(related_name='ideas', to='ideas.Question'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='description',
            field=models.CharField(max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
