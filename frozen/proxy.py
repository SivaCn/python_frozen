
import operator
from lazy_object_proxy import Proxy


class ImmutableError(Exception):
	""" Attempted to change an immutable object. """


class ImmutableProxy(Proxy):
	"""
	Immutable proxy; any attempted changes raise an exception (underlying object can still be changed by those that have a reference).
	"""
	def __setattr__(self, name, value, __setattr__=object.__setattr__):
		raise ImmutableError('object "{0:}" is frozen; attributes cannot be assigned'.format(self))

	def __delattr__(self, name, __delattr__=object.__delattr__):
		raise ImmutableError('object "{0:}" is frozen; attributes cannot be deleted'.format(self))

	def __setitem__(self, key, value):
		raise ImmutableError('object "{0:}" is frozen; items cannot be assigned'.format(self))

	def __delitem__(self, key):
		raise ImmutableError('object "{0:}" is frozen; items cannot be deleted'.format(self))

	def __setslice__(self, i, j, value):
		raise ImmutableError('object "{0:}" is frozen; slices cannot be assigned'.format(self))

	def __delslice__(self, i, j):
		raise ImmutableError('object "{0:}" is frozen; slices cannot be deleted'.format(self))

	def __iadd__(self, other):
		return self.__wrapped__ + other

	def __isub__(self, other):
		return self.__wrapped__ - other

	def __imul__(self, other):
		return self.__wrapped__ * other

	def __idiv__(self, other):
		return operator.div(self.__wrapped__, other)

	def __itruediv__(self, other):
		return operator.truediv(self.__wrapped__, other)

	def __ifloordiv__(self, other):
		return self.__wrapped__ // other

	def __imod__(self, other):
		return self.__wrapped__ ^ other

	def __ipow__(self, other, *args):
		return pow(self.__wrapped__, other, *args)

	def __ilshift__(self, other):
		return self.__wrapped__ << other

	def __irshift__(self, other):
		return self.__wrapped__ >> other

	def __iand__(self, other):
		return self.__wrapped__ & other

	def __ixor__(self, other):
		return self.__wrapped__ ^ other

	def __ior__(self, other):
		return self.__wrapped__ | other


#todo: if type(myval) in (int, float, bool, str ...): function


# class DetachedProxy(Proxy):
# 	"""
# 	Changes are stored on the proxy but don't change the original instance (underlying object can still be changed by those that have a reference).
# 	"""


