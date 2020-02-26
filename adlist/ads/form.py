from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.exceptions import ValidationError
from django.core import  validators

from .models import Ad
from .humanize import naturalsize

# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
# https://stackoverflow.com/questions/2472422/django-file-upload-size-limit
# https://stackoverflow.com/questions/32007311/how-to-change-data-in-django-modelform
# https://docs.djangoproject.com/en/3.0/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other


class CreateForm(forms.ModelForm):
    max_upload_limit = 1 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)

    # Call this 'picture' so it gets copied from the form to the in-memory model
    # It will not be the "bytes", it will be the "InMemoryUploadedFile"
    # because we need to pull out things like content_type
    picture = forms.FileField(required=False, label=f'File to upload no more than {max_upload_limit_text}')
    upload_field_name = 'picture'

    # Hint: this will need to be changed for use in the ads application :)
    class Meta:
        model = Ad
        fields = ['title', 'price', 'text', 'picture']    # Picture is manual

    # Validate the size of the picture
    def clean(self):
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')

        if pic is None:
            return
        elif len(pic) > self.max_upload_limit:
            self.add_error('picture', f'File must less than {self.max_upload_limit_text}.')

    # Convert uploaded File object to a picture
    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)

        # We only need to adjust picture if it is a freshly uploaded file
        file = instance.picture    # Make a copy
        if isinstance(file, InMemoryUploadedFile):    # Extract data from the form to the model
            byte_array = file.read()
            instance.content_type = file.content_type
            instance.picture = byte_array    # Overwrite with the actual image data

        if commit:
            instance.save()

        return instance


# strip means to remove whitespace from the beginning and the end before storing the column
class CommentForm(forms.Form):
    comment = forms.CharField(required=True, max_length=500, min_length=3, strip=True)
