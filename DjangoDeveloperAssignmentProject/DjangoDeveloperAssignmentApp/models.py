from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to='videos/')
    class Meta:
        db_table = "Video_Table"


class LiveStream(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    stream_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "LiveStream_Table"
