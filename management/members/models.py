from django.db import models
import uuid

class Member(models.Model):

    class Meta:
        verbose_name_plural = "member"

    uid = models.UUIDField(default = uuid.uuid4, unique=True)
    name = models.CharField(max_length=75)
    fatherName = models.CharField(max_length=75)
    occupation = models.charfield(max_length=75)
    phone = models.IntegerField(max_length=10)
    address = models.CharField(max_length=255)
    dob = models.DateField()
    wifeName = models.CharField(max_length=75)
    gender = models.CharField(max_length=10)
    married = models.BooleanField(default=False)

    yearofMembership = models.DateField()

class Family(models.Model):

    class Meta:
        verbose_name_plural = "family"

    uid = models.UUIDField(default = uuid.uuid4, unique=True)
    familyName = models.CharField(max_length=75)
    head = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='HeadOfFamily')

    def __str__(self):
        return self.family_name

class FamilyMember(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='family_members')
    father = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='father_of_family')
    mother = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='mother_of_family')
    kids = models.ManyToManyField(Member, related_name='kids_of_family')
    dadgf = models.ForeignKey(Member, null=True, blank=True, on_delete=models.SET_NULL, related_name='dadgf_of_family')
    dadgm = models.ForeignKey(Member, null=True, blank=True, on_delete=models.SET_NULL, related_name='dadgm_of_family')
    momgf = models.ForeignKey(Member, null=True, blank=True, on_delete=models.SET_NULL, related_name='momgf_of_family')
    momgm = models.ForeignKey(Member, null=True, blank=True, on_delete=models.SET_NULL, related_name='momgm_of_family')

    def __str__(self):
        return f'{self.family.family_name} Family Members'
