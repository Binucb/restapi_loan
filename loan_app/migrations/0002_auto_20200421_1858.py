# Generated by Django 3.0.5 on 2020-04-21 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='approval',
            name='applicantincome',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='approval',
            name='area',
            field=models.CharField(choices=[('Rural', 'Rural'), ('Semiurban', 'Semiurban'), ('Urban', 'Urban')], default=0, max_length=15),
        ),
        migrations.AddField(
            model_name='approval',
            name='coapplicatincome',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='approval',
            name='credithistory',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='approval',
            name='dependants',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='approval',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=15),
        ),
        migrations.AddField(
            model_name='approval',
            name='graduatededucation',
            field=models.CharField(choices=[('Graduate', 'Graduated'), ('Not_Graduate', 'Not_Graduate')], default='Graduate', max_length=15),
        ),
        migrations.AddField(
            model_name='approval',
            name='loanamt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='approval',
            name='loanterm',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='approval',
            name='married',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=15),
        ),
        migrations.AddField(
            model_name='approval',
            name='selfemployed',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=15),
        ),
    ]
