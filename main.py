from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import SegiTiga

p1 = PersegiPanjang(10, 6)
print(p1.info())
print(p1.hitung_luas())

print('-' * 50)

s1 = SegiTiga(20, 2)
print(s1.info())
print(s1.hitung_luas())
