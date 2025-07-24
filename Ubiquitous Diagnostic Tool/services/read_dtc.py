from core.uds_core import UDSService

class ReadDTCService(UDSService):
    service_id = 0x19  # UDS ReadDTCInformation service

    def handle_request(self, request_data, context):
        # For demo: return a fixed DTC list (simulate 2 DTCs)
        # UDS response: [service_id + 0x40, subfunction, DTC data...]
        subfunction = request_data[0] if request_data else 0x01
        # Example DTCs: 0x123456, 0xABCDEF
        dtc_bytes = b'\x12\x34\x56\xAB\xCD\xEF'
        response = bytes([self.service_id + 0x40, subfunction]) + dtc_bytes
        return response 