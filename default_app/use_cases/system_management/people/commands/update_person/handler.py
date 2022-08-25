"""
    ToDo: DocString
"""
from django.http import Http404
from mediatr import Mediator
from common_library.utils import Messages, str_yyyymmdd_t
from default_app.domain.system_management import Person
from .command import UpdatePersonCommand
from .view_model import UpdatePersonVm


@Mediator.handler
class UpdatePersonHandler:
    """ ToDo: DocString """

    def handle(self, command: UpdatePersonCommand) -> UpdatePersonVm:
        """ ToDo: DocString """
        person = Person.get_by_uid(str_uid = command.uid)
        if not person:
            raise Http404(Messages.ID_NOT_FOUND)

        if command.name is not None:
            person.name = command.name
        if command.last_name is not None:
            person.last_name = command.last_name
        person.save()

        update_person_vm = UpdatePersonVm(
            uid = str(person.uid),
            name = person.name,
            last_name = person.last_name,
            created_at = str_yyyymmdd_t(person.created_at),
            modified_at = str_yyyymmdd_t(person.modified_at))

        return update_person_vm
