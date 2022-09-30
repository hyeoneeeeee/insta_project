from django.db import models



class UserModel(models.Model):
    class Meta:
        db_table = 'my_insta'

    user_id = models.EmailField(max_length=50, default='')
    # user_phone = models.CharField(max_length=50, Null=True)
    user_nick_name = models.CharField(("닉네임"), max_length=100, default='')
    user_password = models.CharField(max_length=20,default='')
    user_create_at = models.DateTimeField(auto_now_add=True)