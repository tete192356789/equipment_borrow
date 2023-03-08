from rest_framework import serializers
from .models import *

class FacultiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculties
        fields = ('f_id','f_name')

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('item_id','item_id_type','item_name','item_category',
                  'item_description','item_faculty','item_department',
                  'item_status','item_created_at','item_updated_at')