# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import oauth2_provider.generators
import oauth2_provider.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('token', models.CharField(db_index=True, max_length=255)),
                ('expires', models.DateTimeField()),
                ('scope', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('client_id', models.CharField(db_index=True, unique=True, max_length=100, default=oauth2_provider.generators.generate_client_id)),
                ('redirect_uris', models.TextField(help_text='Allowed URIs list, space separated', validators=[oauth2_provider.validators.validate_uris], blank=True)),
                ('client_type', models.CharField(max_length=32, choices=[('confidential', 'Confidential'), ('public', 'Public')])),
                ('authorization_grant_type', models.CharField(max_length=32, choices=[('authorization-code', 'Authorization code'), ('implicit', 'Implicit'), ('password', 'Resource owner password-based'), ('client-credentials', 'Client credentials')])),
                ('client_secret', models.CharField(db_index=True, default=oauth2_provider.generators.generate_client_secret, max_length=255, blank=True)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('skip_authorization', models.BooleanField(default=False)),
                ('user', models.ForeignKey(related_name='oauth2_provider_application', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('code', models.CharField(db_index=True, max_length=255)),
                ('expires', models.DateTimeField()),
                ('redirect_uri', models.CharField(max_length=255)),
                ('scope', models.TextField(blank=True)),
                ('application', models.ForeignKey(to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RefreshToken',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('token', models.CharField(db_index=True, max_length=255)),
                ('access_token', models.OneToOneField(related_name='refresh_token', to='oauth2_provider.AccessToken')),
                ('application', models.ForeignKey(to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='application',
            field=models.ForeignKey(to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='user',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
