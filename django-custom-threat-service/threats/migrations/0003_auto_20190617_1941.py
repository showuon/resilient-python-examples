# Generated by Django 2.2.2 on 2019-06-17 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threats', '0002_auto_20150715_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifact',
            name='type',
            field=models.CharField(choices=[('file.content', 'file.content'), ('file.name', 'file.name'), ('file.path', 'file.path'), ('email', 'email'), ('email.body', 'email.body'), ('email.header', 'email.header'), ('email.header.sender_address', 'email.header.sender_address'), ('email.header.sender_name', 'email.header.sender_name'), ('email.header.to', 'email.header.to'), ('hash.md5', 'hash.md5'), ('hash.sha1', 'hash.sha1'), ('hash.fuzzy', 'hash.fuzzy'), ('cert.x509', 'cert.x509'), ('net.ip', 'net.ip'), ('net.name', 'net.name'), ('net.port', 'net.port'), ('net.uri', 'net.uri'), ('net.http.request.header', 'net.http.request.header'), ('net.http.response.header', 'net.http.response.header'), ('process.name', 'process.name'), ('system.name', 'system.name'), ('system.mutex', 'system.mutex'), ('system.registry', 'system.registry'), ('system.service.name', 'system.service.name')], max_length=32),
        ),
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('string', 'string'), ('number', 'number'), ('uri', 'uri'), ('ip', 'ip'), ('latlng', 'latlng')], max_length=32),
        ),
    ]
