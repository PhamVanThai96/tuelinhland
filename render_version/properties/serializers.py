from rest_framework import serializers
from .models import Property, PropertyType, PropertyImage, PropertyFeature, PropertyFeatureRelation


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = ['id', 'name', 'slug']


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image', 'caption', 'is_primary']


class PropertyFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyFeature
        fields = ['id', 'name', 'icon']


class PropertyListSerializer(serializers.ModelSerializer):
    property_type = PropertyTypeSerializer(read_only=True)
    primary_image = serializers.SerializerMethodField()
    
    class Meta:
        model = Property
        fields = [
            'id', 'title', 'price', 'area', 'bedrooms', 'bathrooms',
            'address', 'district', 'city', 'status', 'featured',
            'property_type', 'primary_image', 'created_at'
        ]
    
    def get_primary_image(self, obj):
        primary_image = obj.images.filter(is_primary=True).first()
        if primary_image:
            return PropertyImageSerializer(primary_image).data
        return None


class PropertyDetailSerializer(serializers.ModelSerializer):
    property_type = PropertyTypeSerializer(read_only=True)
    images = PropertyImageSerializer(many=True, read_only=True)
    features = serializers.SerializerMethodField()
    
    class Meta:
        model = Property
        fields = [
            'id', 'title', 'description', 'price', 'area', 'bedrooms', 'bathrooms',
            'address', 'ward', 'district', 'city', 'status', 'featured',
            'latitude', 'longitude', 'property_type', 'images', 'features',
            'created_at', 'updated_at'
        ]
    
    def get_features(self, obj):
        feature_relations = PropertyFeatureRelation.objects.filter(property=obj)
        features = [relation.feature for relation in feature_relations]
        return PropertyFeatureSerializer(features, many=True).data
