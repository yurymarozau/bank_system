from rest_framework import permissions


class IsUserManagerAddDepositType(permissions.BasePermission):
    '''Permission to check if current user has permission to add deposit types.'''

    message = 'You don\'t have permissions to add a new deposit type.'

    def has_permission(self, request, view):
        return bool(request.user and request.user.has_perm('deposit_app.add_deposittype'))


class IsUserManagerChangeDepositType(permissions.BasePermission):
    '''Permission to check if current user has permission to change deposit types.'''

    message = 'You don\'t have permissions to change the deposit type.'

    def has_permission(self, request, view):
        return bool(request.user and request.user.has_perm('deposit_app.change_deposittype'))


class IsUserManagerDeleteDepositType(permissions.BasePermission):
    '''Permission to check if current user has permission to delete deposit types.'''

    message = 'You don\'t have permissions to delete the deposit type.'

    def has_permission(self, request, view):
        return bool(request.user and request.user.has_perm('deposit_app.delete_deposittype'))


class IsUserManagerViewDepositType(permissions.BasePermission):
    '''Permission to check if current user has permission to view deposit types.'''

    message = 'You don\'t have permissions to view the deposit type.'

    def has_permission(self, request, view):
        return bool(request.user and request.user.has_perm('deposit_app.view_deposittype'))


class IsUserManagerAddDepositContract(permissions.BasePermission):
    '''Permission to check if current user has permission to add deposit contracts.'''

    message = 'You don\'t have permissions to add a new deposit contract.'

    def has_permission(self, request, view):
        return bool(request.user and request.user.has_perm('deposit_app.add_depositcontract'))


class IsUserManagerChangeDepositContract(permissions.BasePermission):
    '''Permission to check if current user has permission to change deposit contracts.'''

    message = 'You don\'t have permissions to change the deposit contract.'

    def has_permission(self, request, view):
        return bool(request.user and request.user.has_perm('deposit_app.change_depositcontract'))


class IsUserManagerDeleteDepositContract(permissions.BasePermission):
    '''Permission to check if current user has permission to delete deposit contracts.'''

    message = 'You don\'t have permissions to delete the deposit contract.'

    def has_permission(self, request, view):
        return bool(request.user and request.user.has_perm('deposit_app.delete_depositcontract'))


class IsUserManagerViewDepositContract(permissions.BasePermission):
    '''Permission to check if current user has permission to view deposit contracts.'''

    message = 'You don\'t have permissions to view the deposit contract.'

    def has_permission(self, request, view):
        return bool(request.user and request.user.has_perm('deposit_app.view_depositcontract'))
