# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)

    class Meta:
        abstract = True


class Registration(TimeStampedModel):
    questioner_first_name = models.CharField(max_length=100, blank=True, null=True)
    questioner_last_name = models.CharField(max_length=100, blank=True, null=True)
    district = models.IntegerField(blank=True, null=True)
    # started_at = models.DateTimeField(blank=True, null=True)
    started_at = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    market_name = models.CharField(max_length=100, blank=True, null=True)
    start_loc_lat = models.FloatField(blank=True, null=True)
    start_loc_long = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.questioner_first_name + ' ' + self.questioner_last_name


class Question(TimeStampedModel):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Group(TimeStampedModel):
    title = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title


class Sku(TimeStampedModel):
    hash_code = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    sub_group = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    sub_brand = models.CharField(max_length=100, blank=True, null=True)
    sent_at = models.IntegerField(blank=True, null=True)
    sent_loc_lat = models.FloatField(blank=True, null=True)
    sent_loc_long = models.FloatField(blank=True, null=True)
    registration = models.ForeignKey(Registration, blank=True, null=True)

    def __str__(self):
        return self.title + ' ' + self.hash_code


class Answer(TimeStampedModel):
    sku = models.ForeignKey(Sku, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.response[:20]


class SkuImage(TimeStampedModel):
    sku = models.ForeignKey(Sku, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.sku.hash_code


