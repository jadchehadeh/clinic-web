# Generated by Django 4.1.3 on 2023-10-13 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0003_alter_patient_age'),
        ('doctor', '0002_doctor_gender_doctor_residency_doctor_univrsity'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('diagnosis', models.CharField(max_length=1000)),
                ('treatment', models.CharField(max_length=1000)),
                ('test_result', models.CharField(max_length=1000)),
                ('doctor_notes', models.CharField(max_length=1000)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
