from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images', blank=True, null=True, verbose_name='프로필 사진')
    email = models.CharField(max_length=200)
    nickname = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    login_type= models.CharField(blank=True, max_length=255, choices=LOGIN_TYPE)

    class Meta:
        db_table = 'users'
    
    def __str__(self):
        list = [self.id , self.user_id, self.profile_image, self.email, self.password, self.login_type]
        return ','.join(list)

class Profile(models.Model) :
    user = models.Foreignkey(User, related_name='User', on_delete = models.Cascade)