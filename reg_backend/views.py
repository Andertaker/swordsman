# -*- coding: utf-8 -*-



from registration import signals
#from registration.backends.simple.views import RegistrationView #simple.views  чтоб не было отправки почты
from registration.backends.default.views import RegistrationView
from registration.models import RegistrationProfile
from registration.forms import RegistrationFormUniqueEmail


from django import forms
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


class RegistrationForm(RegistrationFormUniqueEmail):
    last_name= forms.CharField(label="Фамилия", required=True)
    first_name= forms.CharField(label="Имя", required=True)



#the same but also save lastname and firstname
class RegistrationViewUniqueEmail(RegistrationView):
    form_class = RegistrationForm

    
    def register(self, request, **cleaned_data):
        """
        Given a username, email address and password, register a new
        user account, which will initially be inactive.

        Along with the new ``User`` object, a new
        ``registration.models.RegistrationProfile`` will be created,
        tied to that ``User``, containing the activation key which
        will be used for this account.

        An email will be sent to the supplied email address; this
        email should contain an activation link. The email will be
        rendered using two templates. See the documentation for
        ``RegistrationProfile.send_activation_email()`` for
        information about these templates and the contexts provided to
        them.

        After the ``User`` and ``RegistrationProfile`` are created and
        the activation email is sent, the signal
        ``registration.signals.user_registered`` will be sent, with
        the new ``User`` as the keyword argument ``user`` and the
        class of this backend as the sender.

        """
        username, email, password = cleaned_data['username'], cleaned_data['email'], cleaned_data['password1']
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        new_user = RegistrationProfile.objects.create_inactive_user(username, email,
                                                                    password, site)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        
        #  *** was added
        user = User.objects.get(username__exact=username)  
        user.last_name = cleaned_data['last_name']
        user.first_name = cleaned_data['first_name']
        user.save()
        #  *** was added 
        
        return new_user