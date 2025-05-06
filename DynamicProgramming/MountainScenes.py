class Test:
	def foo(self, x, y):
		return x + y

	def bar(self):
		return self.foo(1,2)


T = Test()
print(T.bar())