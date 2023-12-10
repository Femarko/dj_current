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

        positions_to_update = StockProduct.objects.filter(stock=instance.id)
        print(f'{type(positions_to_update)} {positions_to_update}')


        for position_index, position in enumerate(positions):
            for positions_to_update_index, position_to_update in enumerate(positions_to_update):
                if position_index == positions_to_update_index:
                    print(f'{type(position_to_update)} {position_to_update}')
                    position_to_update.update(**position)
            # print(positions_to_update)

            # for stock_item in StockProduct.objects.filter(stock=stock.id):
            #     print(stock_item)
            #     StockProduct.objects.update(stock=stock_item, **position)
            # StockProduct.objects.update(pk=position_id, **position)

        return stock
