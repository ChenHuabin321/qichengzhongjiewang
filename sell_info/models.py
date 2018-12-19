from django.db import models
# Create your models here.

class Guoyuan_info(models.Model):
    name = models.CharField(max_length=10)#姓名
    jiating_address = models.CharField(max_length=300,null=True,blank = True)#家庭住址
    phone = models.CharField(max_length=20)#电话
    shuliang = models.IntegerField(null=True,blank = True)#果树的数量，单位：棵
    chanliang = models.IntegerField(null=True,blank = True)#果园产量 ，单位：斤
    area = models.FloatField(null=True,blank = True)#果园面积，单位：亩
    guoyuan_address = models.CharField(max_length=300,null=True,blank = True)#果园地址
    guojin_min = models.FloatField(null=True,blank = True)#脐橙最果径，单位：厘米
    guojin_max = models.FloatField(null=True, blank=True)  # 脐橙最果径，单位：厘米
    qita = models.TextField(null=True,blank = True)#果园其他描述信息
    is_checked = models.BooleanField(default=False)#是否已经通过审核
    publish = models.DateField(auto_now_add=True)#发布时间，自动生成
    is_finished = models.BooleanField(default=False)#交易是否结束，默认未结束

    class Meta:
        ordering = ("publish",)
    def __str__(self):
        return '{}    {}株    预计产量{}斤    {}'.format(self.name , self.shuliang , self.chanliang , self.publish)