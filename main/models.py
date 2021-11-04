from django.db import models


# Create your models here.
class TextFile(models.Model):
    """ TextFile Model """
    file_name = models.CharField(max_length=100)
    file = models.FileField()

# CensusId,State,County,TotalPop,Men,Women,Hispanic,White,Black,Native,Asian,
# Pacific,Citizen,Income,IncomeErr,IncomePerCap,IncomePerCapErr,Poverty,ChildPoverty,
# Professional,Service,Office,Construction,Production,Drive,Carpool,Transit,Walk,OtherTransp,
# WorkAtHome,MeanCommute,Employed,PrivateWork,PublicWork,SelfEmployed,FamilyWork,Unemployment


class DemographicData(models.Model):
    # CensusId,State,County,TotalPop,Men,Women,Hispanic,White,Black,Native,Asian,
    # id implicitly defined from models.Model
    census_id = models.IntegerField()
    state = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    total_pop = models.IntegerField()
    total_men = models.IntegerField()
    total_women = models.IntegerField()
    hispanic = models.DecimalField(decimal_places=1, max_digits=20)
    white = models.DecimalField(decimal_places=1, max_digits=20)
    black = models.DecimalField(decimal_places=1, max_digits=20)
    native = models.DecimalField(decimal_places=1, max_digits=20)
    asian = models.DecimalField(decimal_places=1, max_digits=20)
    # Pacific,Citizen,Income,IncomeErr,IncomePerCap,IncomePerCapErr,Poverty,ChildPoverty,
    pacific = models.DecimalField(decimal_places=1, max_digits=20)
    citizen = models.IntegerField()
    income = models.IntegerField()
    income_err = models.IntegerField()
    income_per_cap = models.IntegerField()
    income_per_cap_err = models.IntegerField()
    poverty = models.DecimalField(decimal_places=1, max_digits=20)
    child_poverty = models.DecimalField(decimal_places=1, max_digits=20)
    # Professional,Service,Office,Construction,Production,Drive,Carpool,Transit,Walk,OtherTransp,
    professional = models.DecimalField(decimal_places=1, max_digits=20)
    service = models.DecimalField(decimal_places=1, max_digits=20)
    office = models.DecimalField(decimal_places=1, max_digits=20)
    construction = models.DecimalField(decimal_places=1, max_digits=20)
    production = models.DecimalField(decimal_places=1, max_digits=20)
    drive = models.DecimalField(decimal_places=1, max_digits=20)
    carpool = models.DecimalField(decimal_places=1, max_digits=20)
    transit = models.DecimalField(decimal_places=1, max_digits=20)
    walk = models.DecimalField(decimal_places=1, max_digits=20)
    other_transportation = models.DecimalField(decimal_places=1, max_digits=20)
    # WorkAtHome,MeanCommute,Employed,PrivateWork,PublicWork,SelfEmployed,FamilyWork,Unemployment
    work_at_home = models.DecimalField(decimal_places=1, max_digits=20)
    mean_commute = models.DecimalField(decimal_places=1, max_digits=20)
    employed = models.IntegerField()
    private_work = models.DecimalField(decimal_places=1, max_digits=20)
    public_work = models.DecimalField(decimal_places=1, max_digits=20)
    self_employed = models.DecimalField(decimal_places=1, max_digits=20)
    family_work = models.DecimalField(decimal_places=1, max_digits=20)
    unemployment = models.DecimalField(decimal_places=1, max_digits=20)

