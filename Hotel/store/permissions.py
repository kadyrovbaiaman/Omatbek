from rest_framework.permissions import BasePermission
from rest_framework import permissions


class CheckOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'ownerUser':
            return False
        return True


class CheckCRUD(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.status == 'ownerUser'


class CheckOwnerHotel(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user







#
# class CheckOwnerStatus(BasePermission):
#     def has_permission(self, request, view):
#         if request.user.status == 'ownerUser':
#             return False
#         return True
        # elif request.user.status == 'simpleUser':
        #     return True
        # return True


# class CheckOwnerStatus(BasePermission):
#     def has_permission(self, request, view):
#         if request.user.status == 'simpleUser':
#             return True
#         return False

# class CheckStatus(BasePermission):
#     def has_permission(self, request, view):
#         if request.room.room_status == 'Занят':
#             return False
#         return True

