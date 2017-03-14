# -*- encoding: utf-8 -*-
from django.db.models import ImageField
from django.db.models.fields.files import ImageFieldFile
from PIL import Image
from django.core.files.base import ContentFile
import cStringIO

def generate_thumb(img, thumb_size, format):
    img.seek(0)
    image = Image.open(img)
    if image.mode not in ('L', 'RGB', 'RGBA'):
        image = image.convert('RGB')
    thumb_w, thumb_h = thumb_size
    if thumb_w == thumb_h:
        xsize, ysize = image.size
        minsize = min(xsize,ysize)
        xnewsize = (xsize-minsize)/2
        ynewsize = (ysize-minsize)/2
        image2 = image.crop((xnewsize, ynewsize, xsize-xnewsize, ysize-ynewsize))
        image2.load()
        image2.thumbnail(thumb_size, Image.ANTIALIAS)
    else:
        image2 = image
        image2.thumbnail(thumb_size, Image.ANTIALIAS)
    io = cStringIO.StringIO()
    if format.upper()=='JPG':
        format = 'JPEG'
    image2.save(io, format)
    return ContentFile(io.getvalue())    

class ImageWithThumbsFieldFile(ImageFieldFile):
    def __init__(self, *args, **kwargs):
        super(ImageWithThumbsFieldFile, self).__init__(*args, **kwargs)
        if self.field.sizes:
            def get_size(self, size):
                if not self:
                    return ''
                else:
                    split = self.url.rsplit('.',1)
                    thumb_url = '%s.%sx%s.%s' % (split[0],w,h,split[1])
                    return thumb_url
                    
            for size in self.field.sizes:
                (w,h) = size
                setattr(self, 'url_%sx%s' % (w,h), get_size(self, size))
                
    def save(self, name, content, save=True):
        super(ImageWithThumbsFieldFile, self).save(name, content, save)
        
        if self.field.sizes:
            for size in self.field.sizes:
                (w,h) = size
                split = self.name.rsplit('.',1)
                thumb_name = '%s.%sx%s.%s' % (split[0],w,h,split[1])

                thumb_content = generate_thumb(content, size, split[1])
                
                thumb_name_ = self.storage.save(thumb_name, thumb_content)        
                
                if not thumb_name == thumb_name_:
                    raise ValueError('There is already a file named %s' % thumb_name)
        
    def delete(self, save=True):
        name=self.name
        super(ImageWithThumbsFieldFile, self).delete(save)
        if self.field.sizes:
            for size in self.field.sizes:
                (w,h) = size
                split = name.rsplit('.',1)
                thumb_name = '%s.%sx%s.%s' % (split[0],w,h,split[1])
                try:
                    self.storage.delete(thumb_name)
                except:
                    pass
                        
class ImageWithThumbsField(ImageField):
    attr_class = ImageWithThumbsFieldFile

    def __init__(self, verbose_name=None, name=None, width_field=None, height_field=None, sizes=None, **kwargs):
        self.verbose_name=verbose_name
        self.name=name
        self.width_field=width_field
        self.height_field=height_field
        self.sizes = sizes
        super(ImageField, self).__init__(**kwargs)