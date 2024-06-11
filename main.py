nama = ["Nama: Yogi Ario Pratama", "NPM: 23130320004", "Kelas: 1J", "Modul: Bubble Short"]
for i in nama:
    print(i)
print("\n")
def caribinnary(ar, find):
    j=0
    k=len(ar)-1
    mid=int((j+k)/2)
    hasil="tidak ditemukan apapun"

    while (j<=k):
        if ar[mid] == find:
            hasil = f"ditemukan pada index {mid}"
            break
        elif ar[mid] > find:
            k = mid-1
            mid = int((k+j)/2)
        elif ar[mid] < find:
            j = mid+1
            mid = int((k+j)/2)

    return hasil
def result():
    pass