# Generated by Django 4.2.1 on 2023-05-16 18:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "0008_alter_meetingdocument_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="meetingdocument",
            options={
                "ordering": ["-publication_date", "publishing_meeting", "document_type"]
            },
        ),
    ]
