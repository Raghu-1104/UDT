class ErrorInjector:
    def __init__(self):
        self.inject_can_error = False
        self.inject_uds_error = False
        self.custom_error_code = None

    def enable_can_error(self, enable=True):
        self.inject_can_error = enable

    def enable_uds_error(self, enable=True, code=None):
        self.inject_uds_error = enable
        self.custom_error_code = code

    def should_inject_can_error(self):
        return self.inject_can_error

    def should_inject_uds_error(self):
        return self.inject_uds_error, self.custom_error_code 