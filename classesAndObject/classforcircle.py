def gcd(a,b):
    if a>b:
        a,b=b,a
    r=b%a
    while(r>0):
       b=a
       a=r
       r=b%a
    return a



class Frac:
  def __init__(self,x,y):
   self.p=x
   self.q=y

  def __add__(self,other):
    g=gcd(self.q,other.q) 
    denominetor=(self.q*other.q)/g
    nominetor=(self.p*denominetor)/self.q + (other.p*denominetor)/other.q
    return Frac(nominetor,denominetor)
  
  def subtract(self,other):
    g=gcd(self.q,other.q) 
    denominetor=(self.q*other.q)/g
    nominetor=(self.p*denominetor)/self.q - (other.p*denominetor)/other.q
    return Frac(nominetor,denominetor)
  
  def __str__(self):
    print(f"your nominetor {self.p} and denominetor {self.q}")

  def toFloat(self):
     a=(self.p/self.q)
     return a
  
  def invert(self):
     self.p,self.q=self.q,self.p
     self.__str__()

f1=Frac(5,6)
f2=Frac(3,8)
f3=f1+f2
print(f3.p,f3.q) 
f4=f1.subtract(f2)
# print(f4.p,f4.q)
# f1.__str__()
# print('{:.2f}'.format(f1.toFloat()))
# f1.invert()


