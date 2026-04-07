
class Excursion:
    def __init__(self):
        self.members = []
        self.rentals = {} # dict: {member_name: [item_names]}

    def add_member(self, name):
        if name not in self.members:
            self.members.append(name)
            self.rentals[name] = []

    def remove_member(self, name):
        if name in self.members:
            self.members.remove(name)
            del self.rentals[name]

    def get_members(self):
        return self.members

    def register_item_rented(self, member_name, item_name):
        if member_name in self.rentals:
            self.rentals[member_name].append(item_name)

    def register_item_returned(self, member_name, item_name):
        if member_name in self.rentals and item_name in self.rentals[member_name]:
            self.rentals[member_name].remove(item_name)

    def get_all_who_has_not_returned_items(self):
        return [name for name, items in self.rentals.items() if len(items) > 0]