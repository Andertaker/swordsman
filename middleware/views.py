from django.shortcuts import render





def permissiond_denied_view(request):
    context = {}
    return render(request, 'middleware/permission_denied.html', context)