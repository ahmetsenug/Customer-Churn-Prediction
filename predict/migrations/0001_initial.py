# Generated by Django 4.2.6 on 2023-10-05 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='result1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_gender', models.CharField(max_length=50, verbose_name='gender')),
                ('_age', models.CharField(max_length=50, verbose_name='age')),
                ('_days_since_last_login', models.CharField(max_length=50, verbose_name='days_since_last_login')),
                ('_avg_time_spent', models.CharField(max_length=50, verbose_name='avg_time_spent')),
                ('_avg_transaction_value', models.CharField(max_length=50, verbose_name='avg_transaction_value')),
                ('_avg_frequency_login_days', models.CharField(max_length=50, verbose_name='avg_frequency_login_days')),
                ('_points_in_wallet', models.CharField(max_length=50, verbose_name='points_in_wallet')),
                ('_Region_Category', models.CharField(max_length=50, verbose_name='Region_Category')),
                ('_joined_through_referral', models.CharField(max_length=50, verbose_name='joined_through_referral')),
                ('_membership_category', models.CharField(max_length=50, verbose_name='membership_category')),
                ('_preferred_offer_types', models.CharField(max_length=50, verbose_name='preferred_offer_types')),
                ('_medium_of_operation', models.CharField(max_length=50, verbose_name='medium_of_operation')),
                ('_internet_option', models.CharField(max_length=50, verbose_name='internet_option')),
                ('_Discount', models.CharField(max_length=50, verbose_name='Discount')),
                ('_Offer_Application_Preference', models.CharField(max_length=50, verbose_name='Offer_Application_Preference')),
                ('_Past_Complaint', models.CharField(max_length=50, verbose_name='Past_Complaint')),
                ('_Complatint_Status', models.CharField(max_length=50, verbose_name='Complatint_Status')),
                ('_Feedback', models.CharField(max_length=50, verbose_name='Feedback')),
                ('_prediction_method', models.CharField(max_length=50, verbose_name='prediction_method')),
                ('_prediction', models.CharField(max_length=50, verbose_name='Prediction')),
            ],
        ),
    ]
