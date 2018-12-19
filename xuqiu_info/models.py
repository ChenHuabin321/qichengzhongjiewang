from django.db import models

class Xuqiu_info(models.Model):
    name = models.CharField(max_length=10)#姓名
    jiating_address = models.CharField(max_length=300,null=True,blank = True)#家庭住址
    phone = models.CharField(max_length=20)#电话
    xuqiuliang = models.IntegerField(null=True,blank = True)#需求量,单位：斤
    caizhairiqi = models.DateField(null=True,blank = True)#期望的采摘日期
    guojin_min = models.FloatField(null=True, blank=True)  # 脐橙最小果径，单位：厘米
    guojin_max = models.FloatField(null=True, blank=True)  # 脐橙最大果径，单位：厘米
    qita = models.TextField(null=True,blank = True)#需求其他描述信息
    is_checked = models.BooleanField(default=False)#是否已经通过审核
    publish = models.DateField(auto_now_add=True)#发布时间，自动生成
    is_finished = models.BooleanField(default=False)  # 交易是否结束，默认未结束
    class Meta():
        ordering = ("publish",)
    def __str__(self):
        return '{}    需求量：{}斤    期望采摘日期{}    {}'.format(self.name , self.xuqiuliang , self.caizhairiqi , self.publish)