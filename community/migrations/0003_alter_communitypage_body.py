# Generated by Django 3.2.13 on 2022-05-11 10:40

import re

import django.core.validators
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("community", "0002_alter_communitypage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="communitypage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("paragraph", wagtail.blocks.RichTextBlock()),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                    (
                        "card",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Add a title", required=True
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.RichTextBlock(required=False),
                                ),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "image_align",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[("left", "Left"), ("right", "Right")],
                                        help_text="Whether to align the image left or right on the block.",
                                        required=False,
                                    ),
                                ),
                                (
                                    "button",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "button_text",
                                                wagtail.blocks.CharBlock(
                                                    required=False
                                                ),
                                            ),
                                            (
                                                "page_link",
                                                wagtail.blocks.PageChooserBlock(
                                                    required=False
                                                ),
                                            ),
                                        ],
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "card_row",
                        wagtail.blocks.ListBlock(
                            wagtail.blocks.StructBlock(
                                [
                                    (
                                        "page",
                                        wagtail.blocks.PageChooserBlock(required=True),
                                    ),
                                    (
                                        "text",
                                        wagtail.blocks.CharBlock(required=False),
                                    ),
                                ],
                                label="Page",
                            ),
                            template="streams/blocks/card_row.html",
                        ),
                    ),
                    (
                        "target",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "target_slug",
                                    wagtail.blocks.CharBlock(
                                        help_text="Used to link to a specific location within this page. Slug should only contain letters, numbers, underscore (_), or hyphen (-).",
                                        validators=(
                                            django.core.validators.RegexValidator(
                                                re.compile("^[-a-zA-Z0-9_]+\\Z"),
                                                "Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.",
                                                "invalid",
                                            ),
                                        ),
                                    ),
                                )
                            ]
                        ),
                    ),
                ],
                null=True,
            ),
        ),
    ]
