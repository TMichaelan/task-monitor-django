from django.conf import settings
from request_logging.middleware import LoggingMiddleware


class SafeLoggingMiddleware(LoggingMiddleware):
    """Custom request_logging middleware to handle edge cases."""

    def __call__(self, request):
        """Override to provide custom logic."""
        # Get content length and type from request metadata
        content_length = int(request.META.get("CONTENT_LENGTH", 0))
        content_type = request.META.get("CONTENT_TYPE", "")

        # Determine if the request is multipart
        is_multipart = content_type.startswith("multipart/form-data")
        max_upload_size = int(settings.FILE_UPLOAD_MAX_MEMORY_SIZE)

        # Check if the request body should be cached based on size and type
        if is_multipart and content_length > max_upload_size:
            cached_request_body = None
        else:
            cached_request_body = request.body

        # Cache the request body in the request object
        if cached_request_body is not None:
            request._cached_request_body = cached_request_body

        # Get the response
        response = self.get_response(request)

        # Process the request and response with logging
        self.process_request(request)
        self.process_response(request, response)

        return response
