#Nokta tanımlama
points  =   [
            (5,2),
            (2,9),
            (6,6),
            (7,1)
            ]

#Öklid Mesafe Fonskiyonu
def euclideanDistance(point1,point2):
    x1,y1   =  point1
    x2,y2   =  point2

    distance=(((point2[0]-point1[0])**2)+((point2[1]-point1[1])**2))**0.5
    return(distance)


#Öklid Mesafeler Hesaplaması
distances=[]
for i in range(len(points)): 
 for j in range(i+1,len(points)):
  distanceScore=euclideanDistance(points[i],points[j])
  distances.append(distanceScore)
  print(f"{points[i]} ve {points[j]} noktaları arası mesafe: {distanceScore:.2f}")

#Minimum Mesafeyi Bulmak

minDistance=min(distances)
print(f"Minimum Mesafe:{minDistance}")