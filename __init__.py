# only import if running as a custom node
try:
	import importlib.util
	spec = importlib.util.find_spec("comfy.utils")
	if spec is None:
		raise ImportError
	importlib.import_module("comfy.utils")
except ImportError:
	pass
else:
	NODE_CLASS_MAPPINGS = {}

	from .nodes.simple import NODE_CLASS_MAPPINGS as NetNodes
	NODE_CLASS_MAPPINGS.update(NetNodes)

	from .nodes.advanced import NODE_CLASS_MAPPINGS as AdvNodes
	NODE_CLASS_MAPPINGS.update(AdvNodes)

	from .nodes.images import NODE_CLASS_MAPPINGS as ImgNodes
	NODE_CLASS_MAPPINGS.update(ImgNodes)

	from .nodes.latents import NODE_CLASS_MAPPINGS as LatNodes
	NODE_CLASS_MAPPINGS.update(LatNodes)

	from .nodes.workflows import NODE_CLASS_MAPPINGS as WrkNodes
	NODE_CLASS_MAPPINGS.update(WrkNodes)

	NODE_DISPLAY_NAME_MAPPINGS = {k:v.TITLE for k,v in NODE_CLASS_MAPPINGS.items()}
	__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
