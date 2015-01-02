from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.formtools.wizard.views import SessionWizardView
from django.utils.decorators import method_decorator
from django.forms.models import modelformset_factory

from players import forms
from players.models import Session, Action, ActiveDisciplines, Feeding

@login_required
def profile(request):
    return render(request, 'profile.html', {'character': request.user.character,
                                                     'session_list': Session.objects.all()})

@login_required
def session(request, session):
    session = get_object_or_404(Session, pk=session)
    character = request.user.character
    data =  {'session': session,
             'character': character}
    return render(request, 'session.html', data)

@login_required
def wizard(request, session):
    data = {
        'user': request.user,
        'character': request.user.character,
        'session': get_object_or_404(Session, pk=session)
    }
    initial = {
        '0': data,
        '1': data,
        '2': data,
    }
    return SubmitWizard.as_view([
        modelformset_factory(ActiveDisciplines,
                            formset=forms.DisciplineActivationFormSet,
                            fields=['disciplines']),
        modelformset_factory(Feeding,
                            formset=forms.FeedingFormSet,
                            fields=['domain', 'feeding_points', 'discipline', 'description']),
        modelformset_factory(Action,
                            formset=forms.ActionFormSet,
                            fields=['action_type', 'description'])],
                            initial_dict=initial)(request, **data)


class SubmitWizard(SessionWizardView):
    template_name = 'submit_wizard.html'

    def done(self, form_list, **kwargs):
        character = self.request.user.character
        for f in form_list:
            f.fill_save()
        return HttpResponseRedirect('/s/%s' % kwargs['session'].id)
