from core.uds_core import UDSService

class ECUResetService(UDSService):
    service_id = 0x11  # UDS ECUReset

    def handle_request(self, request_data, context):
        # For demo: always return positive response with reset type
        reset_type = request_data[0] if request_data else 0x01
        response = bytes([self.service_id + 0x40, reset_type])
        return response 