# Generated by Django 2.0.6 on 2018-06-14 01:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Enfant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('sexe', models.CharField(choices=[('Famme', 'famme'), ('Homme', 'homme')], max_length=25)),
                ('date_de_naissance', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Enseignament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexe', models.CharField(choices=[('Famme', 'famme'), ('Homme', 'homme')], max_length=25)),
                ('numero_telephone', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=255)),
                ('nb_enfant', models.IntegerField()),
                ('nb_enfant_max', models.IntegerField()),
                ('niveau', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adr', models.CharField(blank=True, max_length=255, null=True)),
                ('numero_telephone', models.CharField(blank=True, max_length=255, null=True)),
                ('sexe', models.CharField(choices=[('Famme', 'famme'), ('Homme', 'homme')], max_length=25)),
                ('adr_tr', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RemarqueEnseignant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarque', models.CharField(max_length=1000)),
                ('enfant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='montesory.Enfant')),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='montesory.Enseignant')),
            ],
        ),
        migrations.CreateModel(
            name='RemarqueParent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarque', models.CharField(max_length=1000)),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='montesory.Enseignant')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='montesory.Parent')),
            ],
        ),
        migrations.AddField(
            model_name='enseignament',
            name='enseignant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='montesory.Enseignant'),
        ),
        migrations.AddField(
            model_name='enseignament',
            name='groupe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='montesory.Groupe'),
        ),
        migrations.AddField(
            model_name='enseignament',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='montesory.Module'),
        ),
        migrations.AddField(
            model_name='enfant',
            name='groupe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='montesory.Groupe'),
        ),
        migrations.AddField(
            model_name='enfant',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='montesory.Parent'),
        ),
    ]
