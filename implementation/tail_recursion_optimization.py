import sys


def tail_recursion_optimization_decorator(func):
	class TailRecurseException(Exception):
		def __init__(self, *args, **kwargs):
			self.args = args
			self.kwargs = kwargs

	def _wrapper(*args, **kwargs):
		f = sys._getframe()
		if f.f_back and f.f_back.f_back and \
			f.f_back.f_back.f_code == f.f_code:
			raise TailRecurseException(*args, **kwargs)

		while True:
			try:
				return func(*args, **kwargs)
			except TailRecurseException as e:
				args = e.args
				kwargs = e.kwargs

	return _wrapper


@tail_recursion_optimization_decorator
def same_better_foo(n, total):
	if n == 0:
		return total
	return same_better_foo(n - 1, total + n)


same_better_foo(9999, 0)
