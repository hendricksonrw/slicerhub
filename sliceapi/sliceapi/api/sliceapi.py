"""Externally Facing Slice API layer
"""

from slicebase import SliceBase

def process_slice_request(request):
	"""
	"""
	return SliceBase.process_slice_request(request)	

def return_static_slice(requst, slice_id):
    """
    """
    return None

def write_slice_data(request, slice_id):
    """
    """
    return None

def serve_config_by_slice_id(request, slice_id):
    """
    """

    return None

def write_gcode_by_slice_id(request, slice_id):
    """
    """

    return None

def serve_stls_by_slice_id(request, slice_id):
    """
    """

    return None

def serve_state_by_slice_id(request, slice_id):
    """
    """

    return None

def write_state_by_slice_id(request, slice_id):
    """
    """

    return None

