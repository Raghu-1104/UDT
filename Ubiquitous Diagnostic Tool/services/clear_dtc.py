from core.uds_core import UDSService

class ClearDTCService(UDSService):
    service_id = 0x14  # UDS ClearDiagnosticInformation

    def handle_request(self, request_data, context):
        # For demo: always return success
        # UDS positive response: [service_id + 0x40]
        return bytes([self.service_id + 0x40]) 