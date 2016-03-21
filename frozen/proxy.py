
from lazy_object_proxy import Proxy


class ImmutableProxy(Proxy):
	"""
	Immutable proxy; any attempted changes raise an exception (underlying object can still be changed by those that have a reference).
	"""
	def __setattr__(self, name, value, __setattr__=object.__setattr__):
		if hasattr(type(self), name):
			__setattr__(self, name, value)
		else:
			setattr(self.__wrapped__, name, value)

	def __delattr__(self, name, __delattr__=object.__delattr__):
		if hasattr(type(self), name):
			__delattr__(self, name)


class DetachedProxy(Proxy):
	"""
	Changes are stored on the proxy but don't change the original instance (underlying object can still be changed by those that have a reference).
	"""


