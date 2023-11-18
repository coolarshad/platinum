from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page,Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel,InlinePanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks,forms
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.blocks import RichTextBlock

# from .blocks import *
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.models import Page



class HomePage(Page):
    address=models.CharField(max_length=300,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True,blank=True)

    content_panels =Page.content_panels+ [
        FieldPanel('address',classname="full"),
        FieldPanel('email',classname="full"),
        FieldPanel('phone',classname="full"),
    ]
   
    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['image_list'] = CarouselContent.objects.all()[1:]
        context['first_image']=CarouselContent.objects.all().first()
        context['visionmission']=VisionMission.objects.first()
        context['gallery'] = ImagesPage.objects.all()
        context['teampage'] = TeamPage.objects.all().first()
        # context['productpages']=ProductPage.objects.all()
        context['about']=AboutPage.objects.first()
        context['missionvision']=VisionMission.objects.first()
        context['productspecification']=ProductSpecification.objects.all()
        context['productdatasheet']=ProductSafetyDataSheet.objects.all()

        return context

class CarouselImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

class CarouselContent(Page):
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL,null=True, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    content_panels =Page.content_panels+ [
        FieldPanel('image'),
        FieldPanel('caption',classname="full"),
    ]


class AboutPage(Page):
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

class ProductSpecification(Page):
    file_upload = StreamField([
        ('file', DocumentChooserBlock(required=False, help_text='Upload a file')),
    ], blank=True, null=True, use_json_field=True)

    is_file = models.BooleanField(
        default=False,
        help_text='Check to enable the feature',
    )

    content_panels = Page.content_panels + [
        FieldPanel('file_upload'),
        FieldPanel('is_file'),
    ]
  

class SpecificationFirstMenu(Page):
    category = ParentalManyToManyField('home.ProductSpecification', blank=True)
    file_upload = StreamField([
        ('file', DocumentChooserBlock(required=False, help_text='Upload a file')),
    ], blank=True, null=True, use_json_field=True)

    is_file = models.BooleanField(
        default=False,
        help_text='Check to enable the feature'
    )

    content_panels = Page.content_panels + [
        FieldPanel('category'),
        FieldPanel('file_upload'),
        FieldPanel('is_file'),
    ]
   

class SpecificationSecondMenu(Page):
    category = ParentalManyToManyField('home.SpecificationFirstMenu', blank=True)
    file_upload = StreamField([
        ('file', DocumentChooserBlock(required=False, help_text='Upload a file')),
    ], blank=True, null=True, use_json_field=True)

    is_file = models.BooleanField(
        default=False,
        help_text='Check to enable the feature'
    )

    content_panels = Page.content_panels + [
        FieldPanel('category'),
        FieldPanel('file_upload'),
        FieldPanel('is_file'),
    ]
   

class ProductSafetyDataSheet(Page):
    file_upload = StreamField([
        ('file', DocumentChooserBlock(required=False, help_text='Upload a file')),
    ], blank=True, null=True, use_json_field=True)

    is_file = models.BooleanField(
        default=False,
        help_text='Check to enable the feature',
    )

    content_panels = Page.content_panels + [
        FieldPanel('file_upload'),
        FieldPanel('is_file'),
    ]
  

class DataSheetFirstMenu(Page):
    category = ParentalManyToManyField('home.ProductSafetyDataSheet', blank=True)
    file_upload = StreamField([
        ('file', DocumentChooserBlock(required=False, help_text='Upload a file')),
    ], blank=True, null=True, use_json_field=True)

    is_file = models.BooleanField(
        default=False,
        help_text='Check to enable the feature'
    )

    content_panels = Page.content_panels + [
        FieldPanel('category'),
        FieldPanel('file_upload'),
        FieldPanel('is_file'),
    ]
   

class DataSheetSecondMenu(Page):
    category = ParentalManyToManyField('home.DataSheetFirstMenu', blank=True)
    file_upload = StreamField([
        ('file', DocumentChooserBlock(required=False, help_text='Upload a file')),
    ], blank=True, null=True, use_json_field=True)

    is_file = models.BooleanField(
        default=False,
        help_text='Check to enable the feature'
    )

    content_panels = Page.content_panels + [
        FieldPanel('category'),
        FieldPanel('file_upload'),
        FieldPanel('is_file'),
    ]

# class ProductPage(Page):
#     # categories = ParentalManyToManyField('home.ProductCategory', blank=True)
#     image = models.ForeignKey(
#         'wagtailimages.Image', on_delete=models.SET_NULL,null=True, related_name='+'
#     )

#     body = StreamField([
#         ('productblock', ProductBlock()),
#     ])

#     content_panels = Page.content_panels + [
#         ImageChooserPanel('image'),
#         StreamFieldPanel('body'),
#         # FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
#     ]

#     def get_category_wise(self):
#         return ProductDocPage.objects.order_by().values_list('product_name',flat=True).distinct().order_by('product_name')
    
# class ProductDocPage(Page):
#     product_name=models.CharField(max_length=300,null=True,blank=True)
#     description=models.CharField(max_length=1000,null=True,blank=True)
#     product_file = models.ForeignKey(
#         'wagtaildocs.Document',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+'
#     )

#     content_panels = Page.content_panels + [
#         FieldPanel('product_name',classname="full"),
#         FieldPanel('description',classname="full"),
#         DocumentChooserPanel('product_file'),
#         # FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
#     ]


class VisionMission(Page):
    vision=RichTextField()
    mission=RichTextField()

    content_panels=Page.content_panels+[
        FieldPanel('vision',classname="full"),
        FieldPanel('mission',classname="full"),
    ]

class TeamMemberBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=True)
    designation = blocks.CharBlock(required=True)
    image = ImageChooserBlock(required=True)

class TeamPage(Page):
    description = RichTextField(blank=True, null=True, help_text="A description of the image gallery.")
    team_members = StreamField([
        ('team_member', TeamMemberBlock()),
    ], blank=True, null=True,use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('team_members'),
    ]
class ImagesPage(Page):
    images = StreamField([
        ('image', ImageChooserBlock())
    ], blank=True,use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('images'),
    ]