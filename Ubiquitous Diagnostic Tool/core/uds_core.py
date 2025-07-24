from typing import Dict, Callable, Any

class UDSService:
    """
    Base class for UDS service modules. Each service should inherit from this and implement handle_request.
    """
    service_id: int = None  # Each service must define its UDS service ID

    def handle_request(self, request_data: bytes, context: Dict[str, Any]) -> bytes:
        raise NotImplementedError("UDSService subclasses must implement handle_request.")

class UDSCore:
    """
    Core UDS protocol logic: manages service registry, dispatch, and session state.
    """
    def __init__(self):
        self.services: Dict[int, UDSService] = {}
        self.session_state: Dict[str, Any] = {}
        self.error_handler: Callable[[Exception, bytes], bytes] = self.default_error_handler

    def register_service(self, service: UDSService):
        if service.service_id is None:
            raise ValueError("Service must define a service_id.")
        self.services[service.service_id] = service

    def set_error_handler(self, handler: Callable[[Exception, bytes], bytes]):
        self.error_handler = handler

    def handle_request(self, request: bytes, context: Dict[str, Any] = None) -> bytes:
        """
        Dispatches incoming UDS request to the appropriate service.
        """
        if context is None:
            context = {}
        try:
            if not request:
                raise ValueError("Empty UDS request.")
            service_id = request[0]
            service = self.services.get(service_id)
            if not service:
                raise ValueError(f"Unsupported UDS service: 0x{service_id:02X}")
            return service.handle_request(request[1:], context)
        except Exception as e:
            return self.error_handler(e, request)

    def default_error_handler(self, exc: Exception, request: bytes) -> bytes:
        # Simple error response: negative response code 0x7F + serviceId + error code
        service_id = request[0] if request else 0x00
        NRC = 0x13  # Example: 0x13 = InvalidFormat
        return bytes([0x7F, service_id, NRC]) 