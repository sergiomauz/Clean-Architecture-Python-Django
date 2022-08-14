"""
    ToDo: DocString
"""
from django.http import Http404
from mediatr import Mediator
from common_library.utils import Messages
from default_app.domain.system_management import Person
from .command import DeletePersonCommand
from .view_model import DeletePersonVm


@Mediator.handler
class DeletePersonHandler:
    """ ToDo: DocString """

    def handle(self, command: DeletePersonCommand) -> DeletePersonVm:
        """ ToDo: DocString """
        people = Person.get_list_by_uids(uids_list = command.uids)
        if people.count() != len(command.uids):
            raise Http404(Messages.ID_NOT_FOUND)
        people.delete()

        delete_person_vm = DeletePersonVm(
            were_deleted = True)

        return delete_person_vm
