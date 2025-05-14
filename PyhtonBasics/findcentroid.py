class Centroid:
    def __init__(self, list):
        self.list = list

    def centroid(self):
         x = []
         y = []
         for l in self.list:
             x.append(l[0])
             y.append(l[1])
         centroid_x = sum(x)/len(self.list)
         centroid_y = sum(y)/len(self.list)

         return [centroid_x, centroid_y]
    
def main():
    list = [[1,1], [2,2], [3,3]]
    init = Centroid(list)

    print(init.centroid())

if __name__ == "__main__":
    main()


