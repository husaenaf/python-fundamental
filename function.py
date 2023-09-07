from typing import Callable
def luas_segitiga(alas: float, tinggi: float) -> float:
    luas = alas * tinggi // 2
    return luas
print("Luas Segitiga tersebut adalah: ", luas_segitiga(100, 150))


if __name__ == '__main__':
    segitiga: float = luas_segitiga(alas=10, tinggi=15)
    print(segitiga)