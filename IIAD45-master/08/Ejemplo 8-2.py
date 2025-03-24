# Ejemplo 8-2. Metodo depth de la clase Tree

def depth(self, p):
	"""Devuelve el numero de niveles separando posiciones P desde la raiz"""
	if self.is_root(p):
		return 0
	else:
		return 1 + self.depth(self.parent(p))