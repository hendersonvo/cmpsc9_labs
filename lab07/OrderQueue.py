# OrderQueue

class QueueEmptyException(Exception):
    pass

class OrderQueue:
    def __init__(self):
        self.heapList = [0]

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i].distance > self.heapList[i // 2].distance:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2    
    
    def maxChild(self, i):
        if i * 2 + 1 > len(self.heapList) - 1:
            return i * 2
        else:
            if self.heapList[i * 2].distance > self.heapList[i * 2 + 1].distance:
                return i * 2
            else:
                return i * 2 + 1

    def percDown(self, i):
        while (i * 2) <= len(self.heapList) - 1: # check for left child
            mc = self.maxChild(i) # return index of max child
            if self.heapList[i].distance < self.heapList[mc].distance:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc     

    def addOrder(self, teaOrder):
        self.heapList.append(teaOrder)
        self.percUp(len(self.heapList)-1)

    def processNextOrder(self):
        if len(self.heapList) == 1:
            raise QueueEmptyException()
        
        nextUp = self.heapList[1]
        self.heapList[1] = self.heapList[len(self.heapList) - 1]
        self.heapList.pop()
        self.percDown(1)
        return nextUp.getOrderDescription()

