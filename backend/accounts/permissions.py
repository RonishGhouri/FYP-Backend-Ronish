# authapp/permissions.py

from rest_framework.permissions import BasePermission

class IsArtist(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'artist'


class IsArtistManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'artist_manager'


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'manager'


class IsCompany(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'company'


class IsConsumer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'consumer'
