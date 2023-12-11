from rest_framework import serializers
from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for position in positions:
            StockProduct.objects.create(stock=stock, **position)

        return stock


    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        positions_to_update = StockProduct.objects.filter(stock=instance)

        if not positions_to_update.exists():
            for position in positions:
                StockProduct.objects.create(stock=instance, **position)
        else:
            for position in positions:
                product_match_position = positions_to_update.filter(product=position.get('product'))
                if product_match_position:
                    matched_entry = StockProduct.objects.get(stock=instance, product=position['product'])
                    matched_entry.quantity = position['quantity']
                    matched_entry.price = position['price']
                    matched_entry.save()
                else:
                    StockProduct.objects.create(stock=instance, **position)

        return stock
