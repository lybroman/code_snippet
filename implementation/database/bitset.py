import mmap

BYTE_SIZE = 8
PAGE_SIZE = 4096


class MmapBitSet(object):
	def __init__(self, size):
		self.allocated_byte_size = (size / BYTE_SIZE + 1) * PAGE_SIZE
		# -1 for anonymous memory, see: https://landley.net/writing/memory-faq.txt
		self.storage_proxy = mmap.mmap(-1, self.allocated_byte_size)
		self.allocated_bit_size = self.allocated_byte_size * BYTE_SIZE

	def _write_byte(self, pos, byte):
		self.storage_proxy.seek(pos)
		self.storage_proxy.write(byte)

	def _read_byte(self, pos):
		self.storage_proxy.seek(pos)
		return self.storage_proxy.read_byte()

	def set(self, bit_pos, val):
		raw_byte = ord(self._read_byte(bit_pos / BYTE_SIZE))
		if val:
			update_byte = raw_byte | 1 << bit_pos % BYTE_SIZE
		else:
			update_byte = raw_byte & (1 << BYTE_SIZE) - 1 - (1 << bit_pos % BYTE_SIZE)

		if raw_byte != update_byte:
			self._write_byte(bit_pos / BYTE_SIZE, chr(update_byte))

	def get(self, bit_pos):
		raw_byte = ord(self._read_byte(bit_pos / BYTE_SIZE))
		return (raw_byte & 1 << bit_pos % BYTE_SIZE) >> bit_pos % BYTE_SIZE


if __name__ == '__main__':
	mbs = MmapBitSet(1024)
	mbs.set(100, True)
	print mbs.get(100)
	print mbs.get(105)
