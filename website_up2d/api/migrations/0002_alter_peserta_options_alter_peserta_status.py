# Generated by Django 4.0.1 on 2022-01-25 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='peserta',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='peserta',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]