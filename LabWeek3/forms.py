from django import forms

from PhoneReview.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        exclude = ['date_published']
        labels = {
            "title": "Title",
            "article": "Article",
            "models": "Models"
        }
        error_messages = {
            "title": {
              "required": "Your title must not be empty!",
              "max_length": "Please enter a shorter title!"
            },
            "article": {
              "required": "Your article must not be empty!",
            }
        }
