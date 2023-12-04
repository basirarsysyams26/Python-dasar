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


