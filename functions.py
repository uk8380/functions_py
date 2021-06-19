#function is defines as block of code.
#it is 2 types
#1.user defined 2.bulit_in
#syntax
def my_fun():
    print("hello world")
my_fun()#calling function
#arguments:info that can pass through fuction
def my_love(uk):
    print(uk+"uday"+" kumar")
my_love("mannepalli ")

#multiple arguments
def my_wife(name,age,profession):
    print(name,"\n",age,"\n",profession)
my_wife("golu",19,"Data scientist @ walmart")

def anudeep(name,age,gender,kills,game):
    print(name)
    print(age)
    print(game)
    print(kills)
    print(gender)
anudeep("anudeep",12,"hybrid_ninja",10,"ff((free fire))")
#arbitary arguments(*args)
def my_darling(*baby):
    print("my baby is : ",baby[1])
my_darling("golu","mouni","mounika")
#keyword arguments
def my_mouni(name,age):
    print(name+"'s age is",age)
    print("world famous lover")

my_mouni(name="uday",age= 20)

#**kwargs(keyword+arbitary)
def dad(**lname):
    print("Mannepalli",lname["last_name"])

dad(last_name="Ravindra")
#return values
def return_1(x):
    return 5*x
print(return_1((2)))
#lamda function
#syntax lamda fun:expression
x=lambda a,b:a*b
print(x(5,3))
