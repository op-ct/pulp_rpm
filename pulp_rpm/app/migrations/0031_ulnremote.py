# Generated by Django 2.2.19 on 2021-03-18 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_call_handle_artifact_checksums_command'),
        ('rpm', '0030_DATA_fix_updaterecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='UlnRemote',
            fields=[
                ('remote_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='rpm_ulnremote', serialize=False, to='core.Remote')),
                ('uln_server_base_url', models.CharField(max_length=512, null=True)),
            ],
            options={
                'default_related_name': '%(app_label)s_%(model_name)s',
            },
            bases=('core.remote',),
        ),
    ]
