from rest_framework import (
    serializers
)
from app.models import (
    User
)

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'lastname',
            'identification',
            'phone',
            'username',
            'email',
            'password',
            'is_active',
        )
        extra_kwargs ={"password":{
            "write_only": True,
        }}
        

class UserTokenSerializer(UserSerializers):
    # menus = serializers.SerializerMethodField()
    # groups_permission = serializers.ReadOnlyField()
    
    class Meta(UserSerializers.Meta):
        fields = UserSerializers.Meta.fields

    # def get_menus(self, obj):
    #     user_groups = obj.groups.all()
    #     menu_items = MenuItem.objects.filter(groups__in=user_groups, parent=None).distinct().order_by('order')
    #     return self.get_menu_tree(menu_items)

    # def get_menu_tree(self, items):
    #     result = []
    #     for item in items:
    #         item_dict = {
    #             'id': item.id,
    #             'name': item.name,
    #             'path': item.path,
    #             'icon': item.icon,
    #             'order': item.order,
    #             'parent': item.parent_id,
    #         }
    #         children = MenuItem.objects.filter(parent=item).order_by('order')
    #         if children:
    #             item_dict['children'] = self.get_menu_tree(children)
    #         result.append(item_dict)
    #     return result