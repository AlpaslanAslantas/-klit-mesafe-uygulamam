import math

# Öklid mesafesi hesaplama fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Kullanıcıdan noktaları alma
def getPoints():
    points = []
    n = int(input("Kaç nokta girmek istiyorsunuz? "))
    for i in range(n):
        x = float(input(f"Nokta {i+1} için x koordinatını girin: "))
        y = float(input(f"Nokta {i+1} için y koordinatını girin: "))
        points.append((x, y))
    return points

# Mesafelerin saklanacağı liste
distances = []

# Kullanıcıdan noktaları al
points = getPoints()

# Her nokta çifti arasındaki mesafeyi hesaplayarak distances listesine ekleme
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafeyi bulma
min_distance = min(distances)

# Sonucu yazdırma
print("Minimum mesafe:", min_distance)