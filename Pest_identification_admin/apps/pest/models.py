from django.db import models


# Create your models here.
class Orders(models.Model):
    """目表"""
    name = models.CharField(verbose_name='目名称', max_length=255, unique=True)  # 目名称
    code = models.CharField(verbose_name='目代码', max_length=255, blank=True, unique=True)  # 目代码

    def __str__(self):
        return '%s - %s' % (self.name, self.code)

    class Meta:
        verbose_name = '目'
        verbose_name_plural = verbose_name


class Family(models.Model):
    """科表"""
    name = models.CharField(verbose_name='科名称', max_length=255, unique=True)  # 科名称
    code = models.CharField(verbose_name='科代码', max_length=255, blank=True, unique=True)  # 科代码

    def __str__(self):
        return '%s - %s' % (self.name, self.code)

    class Meta:
        verbose_name = '科'
        verbose_name_plural = verbose_name


class Genus(models.Model):
    """属表"""
    name = models.CharField(verbose_name='属名称', max_length=255, unique=True)  # 属名称
    code = models.CharField(verbose_name='属代码', max_length=255, blank=True, unique=True)  # 属代码

    def __str__(self):
        return '%s - %s' % (self.name, self.code)

    class Meta:
        verbose_name = '属'
        verbose_name_plural = verbose_name


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


class Lonlat(models.Model):
    """经纬度表"""
    longitude = models.TextField(verbose_name='经度')  # 经度
    latitude = models.TextField(verbose_name='纬度')  # 纬度

    def __str__(self):
        return '%s - %s' % (self.longitude, self.latitude)

    class Meta:
        verbose_name = '经纬度'
        verbose_name_plural = verbose_name


class Crop(models.Model):
    """危害作物表"""
    name = models.CharField(verbose_name='作物名', max_length=255, unique=True)  # 作物名

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '危害作物'
        verbose_name_plural = verbose_name


class Area(models.Model):
    """害虫分布区域表"""
    province = models.ForeignKey('Province', verbose_name='省', on_delete=models.CASCADE)  # 省
    city = models.ForeignKey('City', verbose_name='市', on_delete=models.CASCADE)  # 市
    address = models.ForeignKey('Address', verbose_name='区', on_delete=models.CASCADE)  # 区
    lonlat = models.ForeignKey('Lonlat', verbose_name='经纬度', on_delete=models.CASCADE)  # 经纬度

    def __str__(self):
        return '%s - %s - %s' % (self.province.name, self.city.name, self.address.name)

    class Meta:
        verbose_name = '分布区域'
        verbose_name_plural = verbose_name


class Pest(models.Model):
    """害虫表"""
    name = models.CharField(verbose_name='害虫名称', max_length=255, unique=True, db_index=True)  # 害虫名称
    code = models.CharField(verbose_name='害虫代码', max_length=255, unique=True, blank=True)  # 害虫代码
    Latin = models.CharField(verbose_name='拉丁名称', max_length=255, unique=True, blank=True)  # 拉丁名称
    egg = models.DateField(verbose_name='卵时期', )  # 卵时期
    larva = models.DateField(verbose_name='幼虫/若虫时期', )  # 幼虫/若虫时期
    pupa = models.DateField(verbose_name='蛹时期', blank=True)  # 蛹时期，一些害虫为不完全变态，无蛹时期
    adult = models.DateField(verbose_name='成虫时期', )  # 成虫时期
    order = models.ForeignKey('Orders', verbose_name='目', on_delete=models.CASCADE)  # 目
    family = models.ForeignKey('Family', verbose_name='科', on_delete=models.CASCADE)  # 科
    genus = models.ForeignKey('Genus', verbose_name='属', on_delete=models.CASCADE)  # 属
    crops = models.ManyToManyField('Crop', verbose_name='危害作物', blank=True)  # 危害作物
    areas = models.ManyToManyField('Area', verbose_name='分布区域')  # 害虫分布区域
    encyclopedias = models.TextField(verbose_name='百科', blank=True, null=True)  # 百科

    def __str__(self):
        return '%s - %s' % (self.name, self.code)

    class Meta:
        verbose_name = '害虫列表'
        verbose_name_plural = verbose_name
