from django.db import models
import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('description',)

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock

AX_BASE_FIELDS = [
    MultiFieldPanel(
        [
            FieldPanel('header_title', classname="full"),
            FieldPanel('header_slogan', classname="full"),
            ImageChooserPanel('header_img'),
            FieldPanel('hide_navigation', classname="full"),
        ],
        heading='Header elements', classname="collapsible collapsed"),
    MultiFieldPanel(
        [
            FieldPanel('footer_text', classname="full"),
        ],
        heading='Footer elements', classname="collapsible collapsed"),

]


class HomePage(Page):
    header_title = models.CharField(max_length=512, blank=True)
    header_slogan = models.CharField(max_length=512, blank=True)
    header_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hide_navigation = models.BooleanField(default=False)
    footer_text = RichTextField(blank=True)

    block1_title = models.CharField(max_length=512, blank=True)
    block1_subline = models.CharField(max_length=1024, blank=True)
    block1_subtitle = RichTextField(blank=True)
    block1_content1 = RichTextField(blank=True)
    block1_button1_url = models.URLField(blank=True)
    block1_button1_label = models.CharField(max_length=512, blank=True)
    block1_content2 = RichTextField(blank=True)
    block1_button2_url = models.URLField(blank=True)
    block1_button2_label = models.CharField(max_length=512, blank=True)
    block1_content3 = RichTextField(blank=True)
    block1_button3_url = models.URLField(blank=True)
    block1_button3_label = models.CharField(max_length=512, blank=True)
    block1_content4 = RichTextField(blank=True)
    block1_button4_url = models.URLField(blank=True)
    block1_button4_label = models.CharField(max_length=512, blank=True)
    block1_conversion_title = models.CharField(max_length=512, blank=True)
    block1_conversion_url = models.URLField(blank=True)
    block1_conversion_button_label = models.CharField(max_length=512, blank=True)

    block2_title = models.CharField(max_length=512, blank=True)
    block2_content1 = RichTextField(blank=True)
    block2_content2 = RichTextField(blank=True)
    block2_content3 = RichTextField(blank=True)
    block2_content4 = RichTextField(blank=True)

    block3_content1 = RichTextField(blank=True)
    block3_thumbnail1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    block3_content2 = RichTextField(blank=True)
    block3_thumbnail2 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    block3_content3 = RichTextField(blank=True)
    block3_thumbnail3 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    block3_content4 = RichTextField(blank=True)
    block3_thumbnail4 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    block_conversion_title = models.CharField(max_length=512, blank=True)
    block_conversion_button_label = models.CharField(max_length=128, blank=True)
    block_conversion_button_url = models.URLField(max_length=128, blank=True)

    block4_content1 = RichTextField(blank=True)
    block4_content2 = RichTextField(blank=True)

    block5_title = models.CharField(max_length=512, blank=True)
    block5_content = RichTextField(blank=True)

    class Meta:
        description = "The top level homepage for your site"
        verbose_name = "Homepage"


HOME_BLOCK1_FIELDS = [
    FieldPanel('block1_title', classname="full"),
    FieldPanel('block1_subline', classname="full"),
    FieldPanel('block1_subtitle', classname="full"),
    FieldPanel('block1_content1', classname="full"),
    FieldPanel('block1_button1_label', classname="full"),
    FieldPanel('block1_button1_url', classname="full"),
    FieldPanel('block1_content2', classname="full"),
    FieldPanel('block1_button2_label', classname="full"),
    FieldPanel('block1_button2_url', classname="full"),
    FieldPanel('block1_content3', classname="full"),
    FieldPanel('block1_button3_label', classname="full"),
    FieldPanel('block1_button3_url', classname="full"),
    FieldPanel('block1_content4', classname="full"),
    FieldPanel('block1_button4_label', classname="full"),
    FieldPanel('block1_button4_url', classname="full"),
    FieldPanel('block1_conversion_title', classname="full"),
    FieldPanel('block1_conversion_url', classname="full"),
    FieldPanel('block1_conversion_button_label', classname="full"),

]

HOME_BLOCK2_FIELDS = [
    FieldPanel('block2_title', classname="full"),
    FieldPanel('block2_content1', classname="full"),
    FieldPanel('block2_content2', classname="full"),
    FieldPanel('block2_content3', classname="full"),
    FieldPanel('block2_content4', classname="full"),
]

HOME_BLOCK3_FIELDS = [
    FieldPanel('block3_content1', classname="full"),
    ImageChooserPanel('block3_thumbnail1'),
    FieldPanel('block3_content2', classname="full"),
    ImageChooserPanel('block3_thumbnail2'),
    FieldPanel('block3_content3', classname="full"),
    ImageChooserPanel('block3_thumbnail3'),
    FieldPanel('block3_content4', classname="full"),
    ImageChooserPanel('block3_thumbnail4'),
]

HOME_BLOCK_SIGNUP_FIELDS = [
    FieldPanel('block_conversion_title', classname="full"),
    FieldPanel('block_conversion_button_label', classname="full"),
    FieldPanel('block_conversion_button_url', classname="full"),

]

HOME_BLOCK4_FIELDS = [
    FieldPanel('block4_content1', classname="full"),
    FieldPanel('block4_content2', classname="full"),
]

HOME_BLOCK5_FIELDS = [
    FieldPanel('block5_title', classname="full"),
    FieldPanel('block5_content', classname="full"),
]

HomePage.content_panels = AX_BASE_FIELDS + [
    FieldPanel('title', classname="full title"),
    MultiFieldPanel(HOME_BLOCK1_FIELDS, heading='Block 1 elements', classname="collapsible collapsed"),
    MultiFieldPanel(HOME_BLOCK2_FIELDS, heading='Block 2 elements', classname="collapsible collapsed"),
    MultiFieldPanel(HOME_BLOCK3_FIELDS, heading='Block 3 elements', classname="collapsible collapsed"),
    MultiFieldPanel(HOME_BLOCK_SIGNUP_FIELDS, heading='Block Sign Up elements', classname="collapsible collapsed"),
    MultiFieldPanel(HOME_BLOCK4_FIELDS, heading='Block 4 elements', classname="collapsible collapsed"),
    MultiFieldPanel(HOME_BLOCK5_FIELDS, heading='Block 5 elements', classname="collapsible collapsed"),
]


class OneColumnMainPage(Page):
    header_title = models.CharField(max_length=512, blank=True)
    header_slogan = models.CharField(max_length=512, blank=True)
    header_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    hide_navigation = models.BooleanField(default=False)
    footer_text = RichTextField(blank=True)

    row1_teaser1 = RichTextField(blank=True)
    row1_teaser2 = RichTextField(blank=True)
    row1_teaser3 = RichTextField(blank=True)
    main_content = RichTextField()
    conversion_title = models.CharField(max_length=256, blank=True)
    conversion_url = models.URLField(blank=True)
    conversion_button_label = models.CharField(max_length=256, blank=True)
    activate_olark = models.BooleanField(default=False)
    foot_row = RichTextField(blank=True)


OneColumnMainPage.content_panels = AX_BASE_FIELDS + [
    FieldPanel('title', classname="full title"),
    FieldPanel('row1_teaser1', classname="full"),
    FieldPanel('row1_teaser2', classname="full"),
    FieldPanel('row1_teaser3', classname="full"),
    FieldPanel('main_content', classname="full"),
    FieldPanel('conversion_title', classname="full"),
    FieldPanel('conversion_url', classname="full"),
    FieldPanel('conversion_button_label', classname="full"),
    FieldPanel('activate_olark', classname="full"),
    FieldPanel('foot_row', classname="full"),
]


class TwoColumnMainPage(Page):
    header_title = models.CharField(max_length=512, blank=True)
    header_slogan = models.CharField(max_length=512, blank=True)
    header_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    hide_navigation = models.BooleanField(default=False)
    footer_text = RichTextField(blank=True)

    teaser = RichTextField(blank=True)
    main_content_left = RichTextField()
    main_content_right = RichTextField()
    conversion_title = models.CharField(max_length=256, blank=True)
    conversion_url = models.URLField(blank=True)
    conversion_button_label = models.CharField(max_length=256, blank=True)
    activate_olark = models.BooleanField(default=False)
    foot_row = RichTextField(blank=True)


TwoColumnMainPage.content_panels = AX_BASE_FIELDS + [
    FieldPanel('title', classname="full title"),
    FieldPanel('teaser', classname="full"),
    FieldPanel('main_content_left', classname="full"),
    FieldPanel('main_content_right', classname="full"),
    FieldPanel('conversion_title', classname="full"),
    FieldPanel('conversion_url', classname="full"),
    FieldPanel('conversion_button_label', classname="full"),
    FieldPanel('activate_olark', classname="full"),
    FieldPanel('foot_row', classname="full"),
]


class ProductPage(Page):
    header_title = models.CharField(max_length=512, blank=True)
    header_slogan = models.CharField(max_length=512, blank=True)
    header_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hide_navigation = models.BooleanField(default=False)
    footer_text = RichTextField(blank=True)
    block1_thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    block1_content = RichTextField()
    block2_content = RichTextField()
    block3_content = RichTextField()
    block4_content = RichTextField()
    conversion_title = models.CharField(max_length=256, blank=True)
    conversion_url = models.URLField(blank=True)
    conversion_button_label = models.CharField(max_length=256, blank=True)
    activate_olark = models.BooleanField(default=False)
    foot_row = RichTextField(blank=True)


ProductPage.content_panels = AX_BASE_FIELDS + [
    FieldPanel('title', classname="full title"),
    ImageChooserPanel('block1_thumbnail'),
    FieldPanel('block1_content', classname="full"),
    FieldPanel('block2_content', classname="full"),
    FieldPanel('block3_content', classname="full"),
    FieldPanel('block4_content', classname="full"),
    FieldPanel('conversion_title', classname="full"),
    FieldPanel('conversion_url', classname="full"),
    FieldPanel('conversion_button_label', classname="full"),
    FieldPanel('activate_olark', classname="full"),
    FieldPanel('foot_row', classname="full"),
]


class TeamPage(Page):
    header_title = models.CharField(max_length=512, blank=True)
    header_slogan = models.CharField(max_length=512, blank=True)
    header_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hide_navigation = models.BooleanField(default=False)
    footer_text = RichTextField(blank=True)

    employees = StreamField([
        ('employee', blocks.StructBlock([
            ('forename', blocks.CharBlock()),
            ('surname', blocks.CharBlock()),
            ('job_title', blocks.CharBlock()),
            ('telephone', blocks.CharBlock(required=False)),
            ('email', blocks.CharBlock()),
            ('image', ImageChooserBlock()),
        ]))
    ], null=True, blank=True)

TeamPage.content_panels = AX_BASE_FIELDS + [
    FieldPanel('title', classname="full title"),
    StreamFieldPanel('employees')
]


class BaseFieldsMixin(models.Model):
    header_title = models.CharField(max_length=512, blank=True)
    header_slogan = models.CharField(max_length=512, blank=True)
    header_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    hide_navigation = models.BooleanField(default=False)
    footer_text = RichTextField(blank=True)

    settings_panels = [
        MultiFieldPanel([
            FieldPanel('hide_navigation'),
        ] + Page.settings_panels, "Page settings"),
    ]

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('header_title', classname="full"),
                FieldPanel('header_slogan', classname="full"),
                ImageChooserPanel('header_img'),
            ],
            heading='Header elements', classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('footer_text', classname="full"),
            ],
            heading='Footer elements', classname="collapsible collapsed"
        ),
        FieldPanel('title', classname="full title"),

    ]

    class Meta:
        abstract = True


class UniversalStreamPage(Page, BaseFieldsMixin):
    content = StreamField([
        ('teaser_area', blocks.StructBlock([
            ('headline', blocks.CharBlock()),
            ('content', blocks.RichTextBlock()),
        ], template='core/blocks/teaser_area.html')),

        ('quotation', blocks.StructBlock([
            ('image', ImageChooserBlock()),
            ('text', blocks.TextBlock(help_text="quotation marks (“...”) will be added automatically")),
            ('name', blocks.CharBlock()),
        ], template='core/blocks/quotation.html')),

        ('one_column_text', blocks.StructBlock([
            ('content', blocks.RichTextBlock()),
        ], template='core/blocks/one_column_text.html')),

        ('two_column_50_50_text', blocks.StructBlock([
            ('left_content', blocks.RichTextBlock()),
            ('right_content', blocks.RichTextBlock()),
        ], template='core/blocks/two_column_50_50_text.html')),

        ('two_column_66_33_text', blocks.StructBlock([
            ('left_content', blocks.RichTextBlock()),
            ('right_content', blocks.RichTextBlock()),
        ], template='core/blocks/two_column_66_33_text.html')),

        ('three_column_33_33_33_text', blocks.StructBlock([
            ('left_content', blocks.RichTextBlock()),
            ('center_content', blocks.RichTextBlock()),
            ('right_content', blocks.RichTextBlock()),
        ], template='core/blocks/three_column_33_33_33_text.html')),

        ('call_to_action_area', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('button_label', blocks.CharBlock()),
            ('button_link', blocks.URLBlock()),
        ], template='core/blocks/call_to_action_area.html')),

        ('raw_html', blocks.StructBlock([
            ('html', blocks.RawHTMLBlock()),
        ], template='core/blocks/raw_html.html')),
    ])

    settings_panels = BaseFieldsMixin.settings_panels
    content_panels = BaseFieldsMixin.content_panels + [
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = 'Flexible content page'
