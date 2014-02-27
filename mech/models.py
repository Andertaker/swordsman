# -*- coding: utf-8 -*-


from django.db import models



class Mech(models.Model):
    class Meta:
        permissions = (
            ("view_gallery", "Может просматривать фотогаллерии"),
        )