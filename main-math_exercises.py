import math

# circle
radius = float(input("enter radius : "))

area = math.pi * pow(radius, 2)

print(f"the area of circle is {round(area, 5)}cm")


# rectangle
panjang = int(input("masukan panjang persegi panjang : "))
lebar = int(input("masukan lebar persegi panjang : "))

luas_persegiPanjang = panjang * lebar

print(f"luas persegi panjang adalah {luas_persegiPanjang}")


# pythagoras
a = int(input("enter panjang a : "))
b = int(input("enter panjang b : "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"hasilnya adalah {int(c)}")