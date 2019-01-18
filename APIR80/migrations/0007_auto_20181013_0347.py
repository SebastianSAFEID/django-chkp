# Generated by Django 2.1.1 on 2018-10-13 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APIR80', '0006_auto_20181013_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='MGMTServerObjectsTCPPorts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MGMTServerFilePathTCPPorts', models.CharField(default='/home/carlos/django-chkp/APIR80/tmp/chkpports.txt', max_length=250)),
                ('MGMTServerObjectsID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIR80.MGMTServer')),
            ],
        ),
        migrations.RemoveField(
            model_name='mgmtserverobjects',
            name='MGMTServerObjectsID',
        ),
        migrations.DeleteModel(
            name='MGMTServerObjects',
        ),
    ]