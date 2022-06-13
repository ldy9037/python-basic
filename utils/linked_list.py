# 파이썬은 linked list가 없길래 그냥 간단하게 구현해 봄.(최소한의 기능만 포함)
# 필요한 기능은 그때그때 추가해서 사용할 것.
# 중복 코드가 조금 많음. 기능을 좀 더 잘게 나눠야 겠음.
from sqlite3 import connect


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        self.head = node

    def setTail(self, node):
        self.tail = node

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def length(self):
        result = 0
        current = self.getHead()

        while current != None:
            current = current.getNext()
            result += 1

        return result

    def add(self, index, node):             
        current = self.findNodeByIndex(index)
        
        if current == None: self.append(node)
        else: self.connectNode(current.prev(), node, current)

    # find 함수 분리, node set 분리
    def addAfterValue(self, value, node):
        current = self.getHead()
        
        while current != None: 
            if current.getValue() == value: 
                node.setNext(current.getNext())
                node.setPrev(current)
                current.setNext(node)

                next_node = node.setNext()
                if next_node == None: self.setTail(node)
                else: next_node.setPrev(node)

                break
            
            current = current.getNext()
        return -1

    # set 분리
    def append(self, node):
        tail = self.getTail()
        self.setTail(node)

        if tail != None: 
            tail.setNext(node)
            node.setPrev(tail)
        else: self.setHead(node)

    def connectNode(self, prev, current, next):
        current.setPrev(prev)
        current.setNext(next)

        if current.getNext() == None: self.setTail(current)
        else: current.getNext().setPrev(current)

        if current.getPrev() == None: self.setHead(current)
        else: current.getPrev().setNext(current)

    def findNodeByIndex(self, index):
        current = {"index": 0, "node": self.getHead()}
        
        while current != None and current["index"] < index:
            current["index"] += 1
            current["node"] = current["node"].getNext()

        return current["node"]        

    def findNodeByValue(self, value):
        current = self.getHead()

        while current != None and current.getValue() != value:
            current = current.getNext()

        return current

    # find, node set
    def remove(self, index): 
        current = {"index": 0, "node": self.getHead()}
        prev = None

        while current["index"] <= index:
            if current["index"] == index:
                if prev == None: self.setHead(current["node"].getLink())
                else: prev.setLink(current["node"].getLink())
                return current["node"].getValue()
            
            prev = current["node"]
            current["node"] = current["node"].getLink()
            current["index"] += 1
        
        return None

    def removeByValue(self, value):
        current = {"index": 0, "node": self.getHead()}
        prev = None

        while current["node"] != None:
            if current["node"].getValue() == value:
                prev.setLink(current["node"].getLink())
                return current["index"]

            prev = current["node"]
            current["node"] = current["node"].getLink() 
            
        return -1

    def getValue(self, index):
        current = {"index": 0, "node": self.getHead()}
        
        while current["node"] != None: 
            if current["index"] == index: return current["node"].getValue()

            current["node"] = current["node"].getLink()
            current["index"] += 1
        
        return None

    def toList(self):
        result = []

        current = self.getHead()
        while current != None: 
            result.append(current.getValue())
            
            current = current.getLink()
        
        return result

class Node:
    def __init__(self, value, link=None, next=None, prev=None):
        self.value = value
        self.link = link
        self.next = next
        self.prev = prev

    def setLink(self, node):
        self.link = node
    
    def setNext(self, next):
        self.next = next

    def setPrev(self, prev):
        self.prev = prev

    def setValue(self, value):
        self.value = value

    def getLink(self):
        return self.link 
    
    def getNext(self):
        return self.next 

    def getPrev(self):
        return self.prev 

    def getValue(self):
        return self.value
    
