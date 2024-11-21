def chia_khuyen_mai(gia_moi,phan_tram_khuyen_mai):
    return gia_moi * (100 - phan_tram_khuyen_mai)/100


g =float(input("nhap gia moi: "))
p =float(input("nhap phan tram khuyen mai:"))
print("gia sau khi giam: " , chia_khuyen_mai(g,p))