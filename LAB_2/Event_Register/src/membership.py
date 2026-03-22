
class MemberService:
    def __init__(self):
        # Property: a list of all members
        self.all_members = []

    def add_member(self, name):
        """
        Registers a new member in the club.
        Target for Unit Test (Spy).
        """
        if name not in self.all_members:
            self.all_members.append(name)
            return True
        return False

class Event:
    def __init__(self, event_name):
        self.event_name = event_name
        self.registered_members = []

    def sign_up(self, name):
        """
        Writes a member up on the event list.
        Target for Unit Test.
        """
        if name not in self.registered_members:
            self.registered_members.append(name)
            return True
        return False

    def register_new_member(self, name, member_service):
        """
        Registers a new member in the club AND writes them up on the event.
        Target for Integration Test.
        """
        # 1. Register globally via the service
        member_service.add_member(name)

        # 2. Sign up for the specific event
        self.sign_up(name)