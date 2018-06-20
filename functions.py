def basic():
    print("Hello")
    
basic()
basic()
basic()

def country(origin):
    message = ("I am from $s")
    print (message %(origin))
    
country("America")

def addition(num1,num2):
    sum = num1 + num2
    return sum
    
sum1 = addition(2,3)
print sum1
sum2 = addition(4,6)
sum3 = addition(sum1,sum2)
print sum3

#or
#def country(origin = "Canada"):
    #message = ("I am from $s")
    #print (message %(origin))

def main():
    count_char('ahsjdfhjdhfjdhf jdfkjdkfj skdjalurylskd jbzkdkvlzskdj djflsdkfklkd nfnlsidfhl sfnlsjdhflsdndfls kdjgsdljsdfjs')