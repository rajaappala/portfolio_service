from django.db import models

class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract=True

class Script(BaseModel):
    name = models.CharField(unique=True, max_length=200)
    nifty_code = models.CharField(unique=True, max_length=200)


class ScriptDetail(BaseModel):
    script = models.ForeignKey(Script, on_delete=models.CASCADE, null=True)
    trade_type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    traded_on = models.DateField()


class Dividend(BaseModel):
    script = models.ForeignKey(Script, on_delete=models.CASCADE, null=True)
    per_share = models.DecimalField(decimal_places=2, max_digits=6)
    received_on = models.DateField()


class Split(BaseModel):
    script = models.ForeignKey(Script, on_delete=models.CASCADE, null=True)
    ratio = models.CharField(max_length=50)
    split_on = models.DateField()


class Bonus(BaseModel):
    script = models.ForeignKey(Script, on_delete=models.CASCADE, null=True)
    ratio = models.CharField(max_length=50)
    bonus_on = models.DateField()