from django.db import models

# Create your models here.
class PupilMoney(models.Model):
    
    full_name = models.CharField(max_length=255)
    age = models.PositiveBigIntegerField(default=1, null=True, blank=True)
    classNum = models.CharField(max_length=255)

    monday_spendMoney = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    tuesday_spendMoney = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    wednesday_spendMoney = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    thursday_spendMoney = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    friday_spendMoney = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    saturday_spendMoney = models.PositiveBigIntegerField(default=0, null=True, blank=True)

    weekly_spendMoney = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    monthly_spendMoney = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    yearly_spendMoney = models.PositiveBigIntegerField(default=0, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name = 'PupilMoney'
        verbose_name_plural = 'PupilMoney'

    def __str__(self):
        return self.full_name # model ni jadvalda name bn korinib turishi un


    def weekly_result(self):
        return self.monday_spendMoney + self.tuesday_spendMoney + self.wednesday_spendMoney 
        + self.thursday_spendMoney + self.friday_spendMoney + self.saturday_spendMoney

    
    # def monthly_result(self):
    #     return self.weekly_result # 