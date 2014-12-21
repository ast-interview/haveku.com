from django.db import models



class Catalogue(models.Model):
    name        = models.CharField(max_length=100)
    weight      = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name



class Tag(models.Model):
    catalogue   = models.ForeignKey(Catalogue, null=True, blank=True)
    
    name        = models.CharField(max_length=100)
    weight      = models.IntegerField(default=0)
    
    def __str__(self):
        if self.catalogue:
            return "%s - %s" % (self.catalogue.name, self.name)
        else:
            return self.name



class Vedio(models.Model):
    tag           = models.ForeignKey(Tag, null=True, blank=True)
    
    url           = models.URLField()
    
    title         = models.CharField(null=True, blank=True, max_length=200)
    description   = models.TextField(null=True, blank=True)
    
    vid           = models.CharField(null=True, blank=True, max_length=300)
    thumbnail     = models.URLField(null=True, blank=True) #, editable=False
    
    datetime      = models.DateTimeField()
    
    def __str__(self):
        return self.title






