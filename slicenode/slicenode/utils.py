

def generate_slice_id():
	"""Will generate a unique ID for the slice."""
	import uuid
	
	slice_id = str(uuid.uuid4())

	return slice_id

