class Raise_Warning(Exception):
    def __init__(self, message_warning = ""):
        self.Message_Warning = message_warning

        super().__init__(self.Message_Warning)

class Raise_JSON_Settings_Error(Exception):
    def __init__(self, message_error):
        self.Message_Error = message_error

        super().__init__(self.Message_Error)