class LazyProperty(object):
	def __init__(self, func):
		self.func = func

	def __get__(self, instance, cls):
		if instance is None:
			return self
		else:
			value = self.func(instance)
			setattr(instance, self.func.__name__, value)
			return value


class ImmutableLazyProperty(object):
	def __init__(self, func):
		self.func = func

	def __get__(self, instance, cls):
		if instance is None:
			return self
		else:
			prop = '_lazy_' + self.func.__name__

			if hasattr(instance, prop):
				return instance.__dict__[prop]
			else:
				value = self.func(instance)
				setattr(instance, prop, value)
				return value


# also immutable
def lazyproperty(func):
	name = '_lazy_' + func.__name__

	@property
	def lazy(self):
		if hasattr(self, name):
			return getattr(self, name)
		else:
			value = func(self)
			setattr(self, name, value)
			return value
	return lazy


class Foo(object):
	@LazyProperty
	def bar(self):
		# some intensive task
		return 'bar'

	@ImmutableLazyProperty
	def baz(self):
		# some intensive task
		return 'baz'

	@lazyproperty
	def qux(self):
		# some intensive task
		return 'qux'


foo = Foo()
print foo.__dict__
print foo.bar, foo.baz, foo.qux
print foo.__dict__

