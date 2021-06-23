from django.db import models
from django.contrib.auth.models import AbstractUser  # 引入原来的Abstract类
from django.conf import settings
from django.utils.html import format_html


# from django.contrib.auth import get_user_model
#
# User = get_user_model()


# Create your models here.
# 创建新的类来继承原来的类，并拓展自己的字段
class UserProfile(AbstractUser):
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(
        choices=(
            ('male', '男'),
            ('female', '女'),
            ('secrecy', '保密')
        ), verbose_name='性别', default='secrecy', max_length=10)
    address = models.CharField(max_length=50, verbose_name='地址', default='')
    mobile = models.CharField(max_length=11, verbose_name='联系电话', null=True, blank=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Province(models.Model):
    """省表"""
    name = models.CharField(verbose_name='省', max_length=255, unique=True)  # 省

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '省'
        verbose_name_plural = verbose_name


class City(models.Model):
    """市表"""
    name = models.CharField(verbose_name='市', max_length=255, unique=True)  # 市

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '市'
        verbose_name_plural = verbose_name


class Address(models.Model):
    """区表"""
    name = models.CharField(verbose_name='区', max_length=255, unique=True)  # 区

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '区'
        verbose_name_plural = verbose_name


class LonLat(models.Model):
    """经纬度表"""
    longitude = models.TextField(verbose_name='经度', )  # 经度
    latitude = models.TextField(verbose_name='纬度', )  # 纬度

    def __str__(self):
        return '%s - %s' % (self.longitude, self.latitude)

    class Meta:
        verbose_name = '经纬度'
        verbose_name_plural = verbose_name


class Area(models.Model):
    """无人机分布区域表"""
    province = models.ForeignKey('Province', verbose_name='省', on_delete=models.CASCADE)  # 省
    city = models.ForeignKey('City', verbose_name='市', on_delete=models.CASCADE)  # 市
    address = models.ForeignKey('Address', verbose_name='区', on_delete=models.CASCADE)  # 区
    lonlat = models.ForeignKey('Lonlat', verbose_name='经纬度', on_delete=models.CASCADE)  # 经纬度

    def __str__(self):
        return '%s - %s - %s' % (self.province.name, self.city.name, self.address.name)

    class Meta:
        verbose_name = '分布区域'
        verbose_name_plural = verbose_name


class Type(models.Model):
    """设备类型表"""
    name = models.CharField(verbose_name='设备类型名称', max_length=255, unique=True)  # 设备类型名

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '设备类型'
        verbose_name_plural = verbose_name


class State(models.Model):
    """机器状态表"""
    name = models.CharField(verbose_name='状态', max_length=255, unique=True)  # 状态名
    code = models.CharField(verbose_name='状态码', max_length=255, unique=True)  # 状态码

    def __str__(self):
        return '%s - %s' % (self.name, self.code)

    class Meta:
        verbose_name = '机器状态'
        verbose_name_plural = verbose_name


class FaultCode(models.Model):
    """故障码表"""
    name = models.CharField(verbose_name='故障名', max_length=255, unique=True)  # 故障名
    code = models.CharField(verbose_name='故障码', max_length=255, unique=True)  # 故障码

    def __str__(self):
        return '%s - %s' % (self.name, self.code)

    class Meta:
        verbose_name = '故障码'
        verbose_name_plural = verbose_name


class UAV(models.Model):
    """无人机表"""
    ma_code = models.CharField(verbose_name='机器编码', max_length=255, unique=True)  # 机器编码
    ma_type = models.ForeignKey('Type', verbose_name='机器类型', on_delete=models.CASCADE)  # 机器类型
    state = models.ForeignKey('State', verbose_name='在线状态', on_delete=models.CASCADE)  # 在线状态
    area = models.ForeignKey('Area', verbose_name='分布区域', on_delete=models.CASCADE)  # 无人机与分布区域
    last_time = models.DateTimeField(verbose_name='上次传输时间', )  # 上次传输时间
    last_content = models.TextField(verbose_name='上次传输内容', )  # 上次传输内容
    startup_time = models.DateTimeField(verbose_name='开机时间', )  # 开机时间
    uptime = models.DateTimeField(verbose_name='正常运行时间', )  # 正常运行时间
    fault_code = models.ManyToManyField('FaultCode', verbose_name='故障码', blank=True)  # 故障码
    director = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='负责人', on_delete=models.CASCADE)  # 负责人

    def __str__(self):
        return '%s - %s - %s - %s - %s' % (self.ma_code, self.ma_type, self.state, self.fault_code, self.director)

    class Meta:
        verbose_name = '无人机列表'
        verbose_name_plural = verbose_name
