class Raise_Warning(Exception):
    def __init__(self, message_warning = ""):
        self.Message_Warning = message_warning

        super().__init__(self.Message_Warning)