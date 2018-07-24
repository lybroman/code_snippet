class Meta(type):
	def __init__(cls, *args, **kwargs):
		super(Meta, cls).__init__(*args, **kwargs)
		print 'Meta __init__'

	def __new__(mcs, *args, **kwargs):
		print 'Meta __new__', mcs
		return super(Meta, mcs).__new__(mcs, *args, **kwargs)

	def __call__(cls, *args, **kwargs):
		print 'Meta __call__', cls, args, kwargs
		super(Meta, cls).__call__(*args, **kwargs)

class Base(object):
	__metaclass__ = Meta

	def __init__(self, *args, **kwargs):
		super(Base, self).__init__()
		print 'Base __init__', args, kwargs

	def __new__(cls, *args, **kwargs):
		print 'Base __new__'
		return super(Base, cls).__new__(cls)

	def __call__(self, *args, **kwargs):
		print 'Base __call__'


class Derived(Base):
	def __init__(self, *args, **kwargs):
		super(Derived, self).__init__( *args, **kwargs)
		print 'Derived __init__', args, kwargs

	def __new__(cls, *args, **kwargs):
		print 'Derived __new__', args, kwargs
		return super(Derived, cls).__new__(cls, *args, **kwargs)

	def __call__(self, *args, **kwargs):
		print 'Derived __call__'


print '------------ split line ---------------'
d = Derived(1, b=2)

