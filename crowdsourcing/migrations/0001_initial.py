# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityLog',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('activity', models.CharField(max_length=512)),
                ('created_timestamp', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('street', models.CharField(max_length=128, error_messages={'required': 'Please specify the street name!'})),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=128, error_messages={'required': 'Please enter the category name!'})),
                ('deleted', models.BooleanField(default=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(null=True, to='crowdsourcing.Category')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=64, error_messages={'required': 'Please specify the city!'})),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=64, error_messages={'required': 'Please specify the country!'})),
                ('code', models.CharField(max_length=8, error_messages={'required': 'Please specify the country code!'})),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('iso_code', models.CharField(max_length=8)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=64, error_messages={'required': 'Please specify the language!'})),
                ('iso_code', models.CharField(max_length=8)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=128, error_messages={'required': 'Please enter the module name!'})),
                ('description', models.TextField(error_messages={'required': 'Please enter the module description!'})),
                ('keywords', models.TextField()),
                ('status', models.IntegerField(default=1, choices=[(1, 'Created'), (2, 'In Progress'), (3, 'In Review'), (4, 'Finished')])),
                ('price', models.FloatField()),
                ('repetition', models.IntegerField()),
                ('module_timeout', models.IntegerField()),
                ('deleted', models.BooleanField(default=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModuleCategory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(to='crowdsourcing.Category')),
                ('module', models.ForeignKey(to='crowdsourcing.Module')),
            ],
        ),
        migrations.CreateModel(
            name='PasswordResetModel',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('reset_key', models.CharField(max_length=40)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=128, error_messages={'required': 'Please enter the project name!'})),
                ('deadline', models.DateTimeField(auto_now_add=True)),
                ('keywords', models.TextField()),
                ('deleted', models.BooleanField(default=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(to='crowdsourcing.Category')),
                ('project', models.ForeignKey(to='crowdsourcing.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectRequester',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(to='crowdsourcing.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('type', models.IntegerField(default=1, choices=[(1, 'Strict'), (2, 'Flexible')])),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('module', models.ForeignKey(to='crowdsourcing.Module')),
            ],
        ),
        migrations.CreateModel(
            name='QualificationItem',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('attribute', models.CharField(max_length=128)),
                ('operator', models.CharField(max_length=128)),
                ('value1', models.CharField(max_length=128)),
                ('value2', models.CharField(max_length=128)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('qualification', models.ForeignKey(to='crowdsourcing.Qualification')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=64, error_messages={'required': 'Please specify the region!'})),
                ('code', models.CharField(max_length=16, error_messages={'required': 'Please specify the region code!'})),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationModel',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('activation_key', models.CharField(max_length=40)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Requester',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='RequesterRanking',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('requester_name', models.CharField(max_length=128)),
                ('requester_payRank', models.FloatField()),
                ('requester_fairRank', models.FloatField()),
                ('requester_speedRank', models.FloatField()),
                ('requester_communicationRank', models.FloatField()),
                ('requester_numberofReviews', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=32, error_messages={'required': 'Please specify the role name!', 'unique': 'The role %(value)r already exists. Please provide another name!'}, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=128, error_messages={'required': 'Please enter the skill name!'})),
                ('description', models.CharField(max_length=512, error_messages={'required': 'Please enter the skill description!'})),
                ('verified', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(null=True, to='crowdsourcing.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('status', models.IntegerField(default=1, choices=[(1, 'Created'), (2, 'Accepted'), (3, 'Reviewed'), (4, 'Finished')])),
                ('deleted', models.BooleanField(default=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('module', models.ForeignKey(to='crowdsourcing.Module')),
            ],
        ),
        migrations.CreateModel(
            name='TaskWorker',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('task', models.ForeignKey(to='crowdsourcing.Task')),
            ],
        ),
        migrations.CreateModel(
            name='TaskWorkerResult',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('status', models.IntegerField(default=1, choices=[(1, 'Created'), (2, 'Accepted'), (3, 'Reviewed'), (4, 'Finished')])),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('task_worker', models.ForeignKey(to='crowdsourcing.TaskWorker')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=128, error_messages={'required': 'Please enter the template name!'})),
                ('source_html', models.TextField()),
                ('deleted', models.BooleanField(default=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to='crowdsourcing.Requester')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateItem',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=128, error_messages={'required': 'Please enter the name of the template item!'})),
                ('deleted', models.BooleanField(default=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('template', models.ForeignKey(to='crowdsourcing.Template')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateItemProperties',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('attribute', models.CharField(max_length=128)),
                ('operator', models.CharField(max_length=128)),
                ('value1', models.CharField(max_length=128)),
                ('value2', models.CharField(max_length=128)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('template_item', models.ForeignKey(to='crowdsourcing.TemplateItem')),
            ],
        ),
        migrations.CreateModel(
            name='UserCountry',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(to='crowdsourcing.Country')),
            ],
        ),
        migrations.CreateModel(
            name='UserLanguage',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('language', models.ForeignKey(to='crowdsourcing.Language')),
            ],
        ),
        migrations.CreateModel(
            name='UserPreferences',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('login_alerts', models.SmallIntegerField(default=0)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('currency', models.ForeignKey(to='crowdsourcing.Currency')),
                ('language', models.ForeignKey(to='crowdsourcing.Language')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('gender', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])),
                ('birthday', models.DateField(error_messages={'invalid': 'Please enter a correct date format'}, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('picture', models.BinaryField(null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(null=True, to='crowdsourcing.Address')),
                ('friends', models.ManyToManyField(through='crowdsourcing.Friendship', to='crowdsourcing.UserProfile')),
                ('languages', models.ManyToManyField(through='crowdsourcing.UserLanguage', to='crowdsourcing.Language')),
                ('nationality', models.ManyToManyField(through='crowdsourcing.UserCountry', to='crowdsourcing.Country')),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('role', models.ForeignKey(to='crowdsourcing.Role')),
                ('user_profile', models.ForeignKey(to='crowdsourcing.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('profile', models.OneToOneField(to='crowdsourcing.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='WorkerModuleApplication',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('status', models.IntegerField(default=1, choices=[(1, 'Created'), (2, 'Accepted'), (3, 'Rejected')])),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('module', models.ForeignKey(to='crowdsourcing.Module')),
                ('worker', models.ForeignKey(to='crowdsourcing.Worker')),
            ],
        ),
        migrations.CreateModel(
            name='WorkerSkill',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('level', models.IntegerField(null=True)),
                ('verified', models.BooleanField(default=False)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('skill', models.ForeignKey(to='crowdsourcing.Skill')),
                ('worker', models.ForeignKey(to='crowdsourcing.Worker')),
            ],
        ),
        migrations.AddField(
            model_name='worker',
            name='skills',
            field=models.ManyToManyField(through='crowdsourcing.WorkerSkill', to='crowdsourcing.Skill'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='roles',
            field=models.ManyToManyField(through='crowdsourcing.UserRole', to='crowdsourcing.Role'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userlanguage',
            name='user',
            field=models.ForeignKey(to='crowdsourcing.UserProfile'),
        ),
        migrations.AddField(
            model_name='usercountry',
            name='user',
            field=models.ForeignKey(to='crowdsourcing.UserProfile'),
        ),
        migrations.AddField(
            model_name='taskworkerresult',
            name='template_item',
            field=models.ForeignKey(to='crowdsourcing.TemplateItem'),
        ),
        migrations.AddField(
            model_name='taskworker',
            name='worker',
            field=models.ForeignKey(to='crowdsourcing.Worker'),
        ),
        migrations.AddField(
            model_name='requester',
            name='profile',
            field=models.OneToOneField(to='crowdsourcing.UserProfile'),
        ),
        migrations.AddField(
            model_name='projectrequester',
            name='requester',
            field=models.ForeignKey(to='crowdsourcing.Requester'),
        ),
        migrations.AddField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(through='crowdsourcing.ProjectCategory', to='crowdsourcing.Category'),
        ),
        migrations.AddField(
            model_name='project',
            name='collaborators',
            field=models.ManyToManyField(through='crowdsourcing.ProjectRequester', to='crowdsourcing.Requester'),
        ),
        migrations.AddField(
            model_name='module',
            name='categories',
            field=models.ManyToManyField(through='crowdsourcing.ModuleCategory', to='crowdsourcing.Category'),
        ),
        migrations.AddField(
            model_name='module',
            name='owner',
            field=models.ForeignKey(to='crowdsourcing.Requester'),
        ),
        migrations.AddField(
            model_name='module',
            name='project',
            field=models.ForeignKey(to='crowdsourcing.Project'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='user_source',
            field=models.ForeignKey(related_name='user_source', to='crowdsourcing.UserProfile'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='user_target',
            field=models.ForeignKey(related_name='user_target', to='crowdsourcing.UserProfile'),
        ),
        migrations.AddField(
            model_name='country',
            name='region',
            field=models.ForeignKey(to='crowdsourcing.Region'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(to='crowdsourcing.Country'),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(to='crowdsourcing.City'),
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(to='crowdsourcing.Country'),
        ),
    ]
