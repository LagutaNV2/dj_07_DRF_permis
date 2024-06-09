from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        '''
        Валидацию удаления чужого объявления следует делать,
        определяя дополнительный класс-наследник BasePermission,
        дополнительно добавляя его в список get_permissions (предпочтительно).
        '''
        
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        print(f'get_permission {obj.creator.id=}, {request.user.is_authenticated=}')
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Instance must have an attribute named `owner`.
        return obj.creator.id == request.user.id and request.user.is_authenticated
        