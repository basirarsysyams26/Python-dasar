# Variable #
firstName = "Basir"
lastName = "Syams"
print("nama saya adalah " + firstName + " " + lastName) #  nama saya adalah Basir Syams

# Mendapatkan tipe data #
firstName = "Basir"
x = 2
print(type(firstName)) # <class 'str'>
print(type(x)) # <class 'int'>

# Banyak nilai ke banyak variable #
x, y, z = "Jeruk", "Apel", "Mangga"
print(x) # Jeruk
print(y) # Apel
print(z) # Mangga

# Satu nilai untuk banyak variable #
x = y = z = "Durian"
print(x)
print(y)
print(z)

# Membongkar kumpulan data #
Animal = ["Sapi", "Kuda", "Jerapah"]
print(Animal[0]) # Sapi
print(Animal[1]) # Kuda
print(Animal[2]) # Jerapah
x, y, z = Animal
print(x) # Sapi
print(y) # Kuda
print(z) # Jerapah

# Variable keluaran #
x = "mobil"
print("Saya memiliki" + x)

x = "mobil"
y = "fortuner"
z = x + " " +y
print(z)

# Variable global #
# Variable global adalah variable yang dibuat diluar function
x = "Susu"
def myfunc():
    print(x)
myfunc()
# Membuat variable global didalam fungsi, apakah bisa? ya, bisa
x = "kuda"
def myfunc():
    global x 
    x = "Ini variable global didalam fungsi"
    print(x)
myfunc()
print(x)
# 
