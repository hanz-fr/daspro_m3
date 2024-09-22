buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]

print(f"value awal : {buah}")

buah[2] = "cherry"
print(f"ganti ceri menjadi cherry : {buah}")

new_item = input("Nama item : ")
index = int(input("Index     : "))

buah.insert(index, new_item)
print(f"insert {new_item} pada index ke-{index} : {buah}")

buah.sort()
print(f"list yang sudah di sort : {buah}")
