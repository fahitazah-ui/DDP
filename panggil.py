import bangunRuang as br
import bangunDatar as bd

print("~~~~ BANGUN RUANG ~~~~")
print(f"Volum kubus dengan sisi 3 adalah {br.kubus(3)}")
print(f"Volum balok adalah {br.balok(4,5,2)}")
print(f"Volum prisma segitiga adalah {br.prisma(5,4,5)}")
print(f"Volum tabung adalah {br.tabung(7,10)}")
print(f"Volum kerucut adalah {br.kerucut(5,12)}")

print("~~~~ BANGUN DATAR ~~~~")
print(f"luas persegi adalah {bd.persegi(5)}")
print(f"luas persegi panjang adalah {bd.persegi_panjag(15,10)}")
print(f"luas segitiga adalah {bd.segitiga(10,6)}")
print(f"luas lingkaran adalah {bd.lingkaran(5)}")
print(f"luas jajarGenjang adalah {bd.jajarGenjang(4,7)}")