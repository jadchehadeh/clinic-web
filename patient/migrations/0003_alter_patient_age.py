# Generated by Django 4.1.3 on 2023-10-13 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_patient_age_patient_alergies_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
