# Generated by Django 2.1.5 on 2019-03-04 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20190225_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='initials',
            field=models.CharField(default='-', help_text="Faculty's Initials", max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='batch',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B4')], help_text="Student's Batch, eg: B2", max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='division',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B')], help_text='Division, eg: B', max_length=1),
        ),
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.CharField(choices=[('F.Y. B.tech', 'F.Y. B.tech'), ('S.Y. B.tech', 'S.Y. B.tech'), ('T.Y. B.tech', 'T.Y. B.tech'), ('L.Y. B.tech', 'L.Y. B.tech')], help_text='choose an option.', max_length=254, unique=True),
        ),
    ]
