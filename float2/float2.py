from math import floor
class Float():
    def __init__(self, numbers,fpoint,sign="+"):
        self.numbers = numbers
        self.asharLen = fpoint
        self.sign=sign
        self.totalLen=len(self.numbers)
        self.sahihLen=self.totalLen-self.asharLen
    ##########################incomplete########################
    #tavanedo va jazr va tashkhise khataye overflow va kharej shodan as range
    def __lt__(self,other):
        #incomplete
            return True
    def __le__(self,other):
        #incomplete
          return True
    def __eq__(self,other):
        #incomplete
        #Return self==value.
        return True
    def __floor__(self, other):
        #incomplete
        #Return self==value.
        return True
    def __round__(self):
        #ya __int__(self) masalan va __round__(...). saghf joda bashe
        #incomplete
        return True
        
    def __neg__(self):
    #incomplete
    #return -self
        return True
    def __truediv__(self, other):
        #incomplete
        #Return value/self.
      return True
    #####################################################    
    def jam(self,other):
        #m:jame do adad bedoone tavajoh be sign
        sumAsharLen,var1,var2=self.convert(other)
        var1.display()
        var2.display() 
        c=0
        sumNumbers=[]
        for i in range (var1.totalLen-1,-1,-1):
            sumNumbers.insert(0,(var1.numbers[i]+var2.numbers[i]+c)%10)
            c=(var1.numbers[i]+var2.numbers[i]+c)//10
        sumNumbers.insert(0,c)
        sum=Float(sumNumbers,sumAsharLen)
        print("---")
        return sum
    
    def tafrigh(self,other):
        #m:tafrighe do adad bedoone tavajoh be sign
        sumAsharLen,var1,var2=self.convert(other)
        var1.display()
        var2.display() 
        b=0
        c=0
        b1=0
        sumNumbers=[]
        for i in range (var1.totalLen-1,-1,-1):
            b0=b1
            b1=0
            if(var1.numbers[i]<var2.numbers[i]):
                b1=1
                c=10
            sumNumbers.insert(0,(var1.numbers[i]-var2.numbers[i]-b0+c))
            c=0
            b0=0
        sum=Float(sumNumbers,sumAsharLen)
        print("---")
        return sum
    
    def display(self):
        #m:namayeshe flaot be soorate string
        nl = self.sign
        for i in range(self.totalLen):
            if(i==self.totalLen-self.asharLen):
                nl=nl+"." 
            nl=nl+str(self.numbers[i])
        print (nl )
        
    def __str__(self):
        #m:namayeshe flaot be soorate string (ba dastoor str/print(...)
        nl = self.sign
        for i in range(self.totalLen):
            if(i==self.totalLen-self.asharLen):
                nl=nl+"." 
            nl=nl+str(self.numbers[i])
        return nl
 
    def __gt__(self,other):
        #m: a>b
        sumAsharLen,var1,var2=self.convert(other)
        if(self.sign=="+"and other.sign=="-"):
            return True
        elif(self.sign=="-"and other.sign=="+"):
            return False
        for i in range (0,var1.totalLen):
            if(var1.numbers[i]>var2.numbers[i]):
                return True
            elif(var1.numbers[i]<var2.numbers[i]):
                return False
        return False #barabar true nist

    def  __mul__(self, other):
        #m: Return self*value.
        self.display()
        other.display() 
        c=0
        c1=0
        sumNumbers=(self.totalLen+other.totalLen)*[0]
        i=0
        mIndex=0
        for n in range (other.totalLen-1,-1,-1):
            i=mIndex
            for m in range (self.totalLen-1,-1,-1):
                c1=(sumNumbers[i]+self.numbers[m]*other.numbers[n]+c)//10
                sumNumbers[i]=(sumNumbers[i]+self.numbers[m]*other.numbers[n]+c)%10
                c=c1
                i=i+1
                
            mIndex=mIndex+1
            sumNumbers[i]=c
            c=0
        
        sumNumbers.reverse()
        if(self.sign==other.sign):
            sumSign="+"
        else:
            sumSign="-"
        sum=Float(sumNumbers,self.asharLen+other.asharLen,sumSign)      
        print("---")
        sum.display()
        return sum


    def __ge__(self,other):
        #m: a>=b
        sumAsharLen,var1,var2=self.convert(other)
        if(self.sign=="+"and other.sign=="-"):
            return True
        elif(self.sign=="-"and other.sign=="+"):
            return False
        for i in range (0,var1.totalLen):
            if(var1.numbers[i]>var2.numbers[i]):
                return True
            elif(var1.numbers[i]<var2.numbers[i]):
                return False
        return True
    
    def absolute(self):
        #m:
        return Float(self.numbers,self.asharLen,"+")
    
    def convert(self,other):
        #m:yeki kardane tedad ashar va sahihe 2adad baraye jam o moghayese o ...
        #m:var1=self,var2=other
         if(self.asharLen>other.asharLen):
            sumAsharLen=self.asharLen
            var2=Float(other.numbers+(self.asharLen-other.asharLen)*[0],sumAsharLen,other.sign)
            var1=self
         else:
            sumAsharLen=other.asharLen
            var2=other
            var1=Float(self.numbers+(other.asharLen-self.asharLen)*[0],sumAsharLen,self.sign)
         if(var1.sahihLen>var2.sahihLen):
            var2=Float((var1.sahihLen-var2.sahihLen)*[0]+var2.numbers,sumAsharLen,var2.sign)
         else:
            var1=Float((var2.sahihLen-var1.sahihLen)*[0]+var1.numbers,sumAsharLen,var1.sign)
        
         return sumAsharLen,var1,var2
        
    def __add__(self,other):
        #m: operatore jam ba tavajoh be sign
        if(self.sign=="+"and other.sign=="+"):
            sum=self.jam(other)
        elif(self.sign=="+"and other.sign=="-"):
            sum=self.tafrigh(other)
            if (other.absolute()>self.absolute()):
                sum.sign="-"
        elif(self.sign=="-"and other.sign=="+"):
            sum=self.tafrigh(other)
            if (self.absolute()>other.absolute()):
                sum.sign="-"
        elif(self.sign=="-"and other.sign=="-"):
            sum=self.jam(other)
            sum.sign="-"
        
        sum.display()
        return sum
     
    def __sub__(self,other):
      #m: operatore tafrigh ba tavajoh be sign
        if(self.sign=="+"and other.sign=="+"):
            #barabare add + -
            sum=self.tafrigh(other)
            if (other.absolute()>self.absolute()):
                sum.sign="-"
        elif(self.sign=="+"and other.sign=="-"):
            #barabare add + +
            sum=self.jam(other)  
        elif(self.sign=="-"and other.sign=="+"):
            #barabare add - -
            sum=self.jam(other)
            sum.sign="-"
        elif(self.sign=="-"and other.sign=="-"):
            #barabare add - +
            sum=self.tafrigh(other)
            if (self.absolute()>other.absolute()):
                sum.sign="-"
        
        sum.display()
        return sum
def assertFalse(exp):
    assert (exp)==False

a=Float([1,2,3],1)
b=Float([1,2,3],2)
