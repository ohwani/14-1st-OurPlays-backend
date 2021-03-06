from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'categories'
    
class Region(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'regions'

class Place(models.Model):
    title                       = models.CharField(max_length = 100)
    region                      = models.ForeignKey(Region, on_delete = models.CASCADE)
    address                     = models.CharField(max_length = 200)
    latitude                    = models.FloatField(default=0.0)
    longtitude                  = models.FloatField(default=0.0)
    price_per_hour              = models.IntegerField(default = 10000)
    area                        = models.FloatField(default = 0)
    floor                       = models.IntegerField(default = 1)
    maximum_parking_lot         = models.IntegerField(default = 0)
    allowed_members_count       = models.IntegerField(default = 1)
    description                 = models.TextField(default = '')
    using_rule                  = models.TextField(default = '')
    info_nearby                 = models.TextField(default = '')
    minimum_rental_hour         = models.IntegerField(default = 1)
    delegate_place_image_url    = models.CharField(max_length = 200)
    surcharge_rule              = models.IntegerField(default = 0)
    user                        = models.ForeignKey('user.User', on_delete = models.CASCADE, related_name = 'related_place_user')
    category                    = models.ForeignKey(Category, on_delete = models.CASCADE)
    ratings                     = models.ManyToManyField('user.User', through = 'Rating')

    class Meta:
        db_table = 'places'

class Rating(models.Model):
    starpoint  = models.FloatField(default=0)
    comment    = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    place      = models.ForeignKey(Place, on_delete = models.CASCADE, related_name = 'related_rating_place')
    user       = models.ForeignKey('user.User', on_delete = models.CASCADE)

    class Meta:
        db_table = 'ratings'

class PlaceImage(models.Model):
    url   = models.URLField(max_length = 200)
    place = models.ForeignKey(Place, on_delete = models.CASCADE)

    class Meta:
        db_table = 'place_images'

class Tag(models.Model):
    name        = models.CharField(max_length = 50, unique = True)
    created_at  = models.DateTimeField(auto_now_add = True)
    places_tags = models.ManyToManyField(Place)

    class Meta:
        db_table = 'tags'

class InvalidBookingDay(models.Model):
    day   = models.DateField()
    place = models.ForeignKey(Place,on_delete = models.CASCADE)

    class Meta:
        db_table = 'invalid_booking_days'
        
