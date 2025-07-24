from core.uds_core import UDSService

class ReadDataByIdentifierService(UDSService):
    service_id = 0x22  # UDS ReadDataByIdentifier

    def handle_request(self, request_data, context):
        # For demo: return fixed data for a few identifiers
        if len(request_data) < 2:
            return bytes([0x7F, self.service_id, 0x13])  # InvalidFormat
        did = int.from_bytes(request_data[:2], 'big')
        # Simulate a few DIDs
        if did == 0xF190:
            value = b'DEMO_VIN_1234567890'
        elif did == 0xF187:
            value = b'ECU_SN_0001'
        else:
            return bytes([0x7F, self.service_id, 0x31])  # RequestOutOfRange
        response = bytes([self.service_id + 0x40]) + request_data[:2] + value
        return response 