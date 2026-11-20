import lib1
import numpy

primos = numpy.array(lib1.calcular_primos(100))

print(f"Total:   {primos.size}")
print(f"Suma:    {primos.sum()}")
print(f"Media:   {primos.mean()}")
print(f"Mínimo:  {primos.min()}")
print(f"Mediana: {numpy.median(primos)}")
print(f"Máximo:  {primos.max()}")
