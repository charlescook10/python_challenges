# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None
#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# And a new rule: passwords must be unique (not reused in other services).
#
# Example usage:
#   > password_manager = PasswordManager2()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('youtube', '3@245256')  # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.list_services()
#   ['gmail', 'facebook', 'youtube']
#   > password_manager.remove('facebook')
#   > password_manager.list_services()
#   ['gmail', 'youtube']
#   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('gmail')
#   '12ab5!678'
#   > password_manager.update('gmail', '%21321415')  # Valid password
#   > password_manager.get_for_service('gmail')
#   '%21321415'
#   > password_manager.sort_services_by('service')
#   ['gmail', 'youtube']
#   > password_manager.sort_services_by('added_on', 'reverse')
#   ['youtube', 'gmail']

# There are many more examples possible but the above should give you a good
# idea.

# == YOUR CODE ==

from datetime import datetime
class PasswordManager2():
    def __init__(self):
        #   dictionary with dictionaries
        #   {
        #      service: {password: password, date_added: date},
        #   }
        self.storage = {}
    def __is_valid_length(self, password):
        return len(password) > 7
    def __contains_special_char(self, password):
        special_chars = "!@$%&"
        return any(char in password for char in special_chars)
    def __password_is_unique(self, password):
        return list(filter(lambda d: d[1]["password"] == password, self.storage.items())) == []
    def __is_valid(self, password):
        return self.__is_valid_length(password) and self.__contains_special_char(password) and self.__password_is_unique(password)
    def add(self, service, password):
        if self.__is_valid(password):
            self.storage[service]= {"password": password, "date_added": datetime.today()}
        return None
    def remove(self, service):
        del self.storage[service]
        return None
    def update(self, service, password):
        self.add(service, password)
        return None
    def list_services(self):
        return list(self.storage.keys())
    def get_for_service(self, service):
        if service in self.storage:
            return self.storage[service]["password"]
        else: 
            return None
    def sort_services_by(self, sort, reverse_param=None):
        #sort by service or by added_on date
        reverse_bool = reverse_param == "reverse"
        if sort == "service":
            return sorted(self.list_services(), reverse=reverse_bool)
        elif sort == "added_on":
            sorted_dict = dict(sorted(self.storage.items(), key=lambda service: service[1]["date_added"], reverse=reverse_bool))
            return list(sorted_dict.keys())