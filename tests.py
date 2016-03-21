
"""
py.test
"""

from copy import copy
from pytest import raises
from frozen import frozen, ImmutableError
import sys


class Cls:
	def __init__(self):
		self.attr = 42
		self.li = [42]
	def mthd(self):
		pass


def test_simple_immutables_immutable():
	for val in (42, 3.1415, 'hello', (1, 2, 3)):
		q = copy(val)
		p = frozen(q)
		try:
			p += val
		except ImmutableError:
			""" It may or may not raise an error (it probably doesn't); all that matters is that q is unchanged. """
		assert q == val, 'type "" changed after becoming frozen'.format(type(q))
		del p


def test_list_immutable():
	q = [37]
	p = frozen(q)
	with raises(ImmutableError):
		p[0] = 42
	with raises(ImmutableError):
		p.append(42)
	with raises(ImmutableError):
		p.pop()


def test_list_mutable():
	q = [37]
	p = frozen(q)
	q.append(42)
	q[0] = 0
	assert len(p) == 2
	assert q == p
	assert p[0] == 0


def test_dict_immutable():
	q = {True: 37}
	p = frozen(q)
	with raises(ImmutableError):
		p[True] = 42
	with raises(ImmutableError):
		p[False] = 42
	with raises(ImmutableError):
		p.pop(True)


def test_dict_mutable():
	q = {True: 37}
	p = frozen(q)
	q[False] = 42
	q.pop(True)
	assert p == q == {False: 42}


def test_set_immutable():
	q = {37,}
	p = frozen(q)
	with raises(ImmutableError):
		p.add(42)
	with raises(ImmutableError):
		p.remove(37)
	with raises(ImmutableError):
		p &= {42}


def test_set_mutable():
	q = {37,}
	p = frozen(q)
	q.add(42)
	q.remove(37)
	q &= {42}
	assert p == q


def test_instance_immutable():
	q = Cls()
	p = frozen(q)
	with raises(ImmutableError):
		p.attr += 37
	with raises(ImmutableError):
		p.attr = 37
	with raises(ImmutableError):
		del p.attr
	with raises(ImmutableError):
		p.mthd = lambda self: None


def test_instance_mutable():
	q = Cls()
	p = frozen(q)
	q.attr += 37
	assert q.attr == p.attr
	assert q.__dict__ == p.__dict__
	del q.attr
	assert hasattr(p, 'attr') is False


def test_module():
	p = frozen(sys)
	with raises(ImmutableError):
		p._random_test_value = 42


def test_nesting_immutable():
	q = Cls()
	p = frozen(q)
	with raises(ImmutableError):
		p.li.append(37)
	q = [[0]]
	p = frozen(q)
	with raises(ImmutableError):
		p[0][0] = 1


def test_nesting_mutable():
	q = Cls()
	p = frozen(q)
	q.li.append(37)
	assert p.li == q.li
	q = [[0]]
	p = frozen(q)
	q[0][0] = 1
	assert p == q


def test_idempotent():
	q = Cls()
	p = frozen(q)
	r = frozen(p)
	assert p is not q
	assert p is r
	assert p.li is not q.li
	assert p.li is r.li


