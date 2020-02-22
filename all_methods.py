        -----DISABLE PRINTS
import os
import contextlib

with open(os.devnull, "w") as f, contextlib.redirect_stdout(f):
    print("This won't be printed.")
    
    
    
    



		-----METODO BISSECAO
def bissec(a,b,p):
    while abs(b-a) > p:
    #for i in range(p):
        m=(b+a)/2
        if f(a)*f(m)<0:
            b=m
        else:
            a=m
        
    return (b+a)/2


		-----METODO CORDA / FALSA POSICAO
def fp(a,b,p):
    x=(a*f(b)-b*f(a))/(f(b)-f(a))
    while abs(b-a) > p:
        if f(a)*f(x)<0:
            b=x
        else:
            a=x

    return (b+a)/2


		-----NEWTON
#Expressao de f(x)
def f(x):
    return 2*x**2-5*x-3
    
#Expressao da derivada de f(x) 
def fl(x):
    return 4*x-5

def newton(x, max_iter):
    for i in range(max_iter):
        x = x - (f(x)/fl(x))
        print(i, x)
        
#OU

def newton2(x):
    xn = x - (f(x)/fl(x))
    while x!=xn:
        x=xn
        xn = xn - (f(xn)/fl(xn))
        print(x,xn)


		-----NEWTON_2VAR
def f1(x,y):


def f2(x,y):


def df1x(x,y):


def df2x(x,y): 


def df1y(x,y):


def df2y(x,y):


def jacobian(x,y):
    return df1x(x,y)*df2y(x,y)-df1y(x,y)*df2x(x,y)

def hn(x,y):
    return -((f1(x,y)*df2y(x,y)-df1y(x,y)*f2(x,y))/jacobian(x,y))

def kn(x,y):
    return -((df1x(x,y)*f2(x,y)-f1(x,y)*df2x(x,y))/jacobian(x,y))

def newton2var(x,y,max_iter): 
    for i in range(max_iter):
        xn=x+hn(x,y)
        yn=y+kn(x,y)
        print(i,xn,yn)
        x=xn
        y=yn

def newton2varErr(x,y,p):
    i=0
    xn=x+hn(x,y)
    yn=y+kn(x,y)
    print (i,xn,yn)
    while(abs(xn-x)>p or abs(yn-y)>p):
        i+=1
        x=xn
        y=yn
        xn=x+hn(x,y)
        yn=y+kn(x,y)
        print(i,xn,yn)


		-----PICARDO-PEANO
#Expressao da funcao em ordem a x
def g(x):
    return 0.4*x**2-0.6


def picard_peano(x, max_iter, p):   
    for i in range(max_iter):
        xn=g(x)
        print(i,x)
        if abs(xn-x)<p:
            return (i, xn)
        x=xn


		-----PICARDO-PEANO_2VAR
def f1(x,y):
    return 2*x**2-x*y-5*x+1

def f2(x,y):
    return x+3*m.log(x)-y**2
    
def gx(x,y):						#achando a funcao de x, com f1
    return m.pow((x*(y+5)-1)/2, 1/2)
    

def gy(x,y):						#achando a funcao y, com f2
    return -m.pow(x+m.log(x),1/2)

def pp2Var(x,y,max_iter):
    for i in range(max_iter):
        xn=gx(x,y)
        yn=gy(x,y)
        print(i,xn,yn)
        x=xn
        y=yn


		-----GAUSS
import copy as c

m=[[7,8,9,24],[8,9,10,27],[9,10,8,27]]
r=[0,0,0]
mc=c.deepcopy(m)
dimV=len(m)

#Metodo de Gauss
def gauss(m):
    for diag in range(dimV):
        pivot = m[diag][diag]
        for col in range (dimV+1):
            m[diag][col]/=pivot
        for lin in range(diag+1, dimV):
            pivot2 = m[lin][diag]
            for col in range(diag, dimV+1):
                m[lin][col] -= m[diag][col] * pivot2
                
    #print(m)
    
    for diag in range(dimV-1, -1, -1):
        for lin in range(diag-1, -1, -1):
            factor=m[lin][diag]
            for col in range(dimV, diag-1, -1):
                m[lin][col]-=m[diag][col]*factor
    #print("")
    #print(m)
    return m
gauss(m)
print(m)

#Estabilidade Interna
def residuos(m):
    for eq in range(dimV):
        for sol in range(dimV):
            r[eq] = r[eq] + mc[eq][sol]*m[sol][dimV]
        r[eq] = mc[eq][dimV] - r[eq]
        
    return r

#Estabilidade Externa
"""
A*dx=db-dA*x

db-daA*x =    
[0.5,0.5,0.5]-[[0.5,0.5,0.5],[0.5,0.5,0.5],[0.5,0.5,0.5]]*[-4.3716,-8.9325,28.8401]
= [- 7.268,- 7.268,- 7.268]
"""

print("")
m=[[7,8,9,- 7.268],[8,9,10,- 7.268],[9,10,8,- 7.268]]
gauss(m)
print(m)


		-----GAUSS-JACOBI
#cx etc sao coeficientes das variaveis na matriz A
#b o valor de B

def fx(cx,x,cy,y,cz,z,cw,w,b):
    return (b-cy*y-cz*z-cw*w)/cx

def fy(cx,x,cy,y,cz,z,cw,w,b):
    return (b-cx*x-cz*z-cw*w)/cy

def fz(cx,x,cy,y,cz,z,cw,w,b):
    return (b-cx*x-cy*y-cw*w)/cz

def fw(cx,x,cy,y,cz,z,cw,w,b):
    return (b-cx*x-cy*y-cz*z)/cw

def gaussJacobi(numItr):
    #guesses iniciais
    x=2.12687
    y=2.39858
    z=3.99517
    w=-3.73040
    for i in range(numItr):
        xAnt = x
        yAnt = y
        zAnt = z
        wAnt = w
        x = fx(6,xAnt,0.5,yAnt,3,zAnt,0.25,wAnt,25)
        y = fy(1.2,xAnt,3,yAnt,0.25,zAnt,0.2,wAnt,10)
        z = fz(-1,xAnt,0.25,yAnt,4,zAnt,2,wAnt,7)
        w = fw(2,xAnt,4,yAnt,1,zAnt,8,wAnt,-12)
        
        print("x: ",x)
        print("y: ",y)
        print("z: ",z)
        print("w: ",w)
        print("")


		-----GAUSS-SEIDEL
#cx etc sao coeficientes das variaveis na matriz A
#b o valor na matriz b

def fx(cx,x,cy,y,cz,z,cw,w,b):
    return (b-cy*y-cz*z-cw*w)/cx

def fy(cx,x,cy,y,cz,z,cw,w,b):
    return (b-cx*x-cz*z-cw*w)/cy

def fz(cx,x,cy,y,cz,z,cw,w,b):
    return (b-cx*x-cy*y-cw*w)/cz

def fw(cx,x,cy,y,cz,z,cw,w,b):
    return (b-cx*x-cy*y-cz*z)/cw

def gaussSeidel(numItr):
    #guesses iniciais
    x=2.12687
    y=2.39858
    z=3.99517
    w=-3.73040
    for i in range(numItr):
        x = fx(6,x,0.5,y,3,z,0.25,w,25)
        y = fy(1.2,x,3,y,0.25,z,0.2,w,10)
        z = fz(-1,x,0.25,y,4,z,2,w,7,)
        w = fw(2,x,4,y,1,z,8,w,-12)
        
        print("x: ",x)
        print("y: ",y)
        print("z: ",z)
        print("w: ",w)
        print("")


		-----TRAPEZIOS
def f(x):


def trapezio(a,b,n):
    h = abs((b-a)/n)
    total = 0
    for i in range(1,n):
        total += 2*f(a+i*h)

    total+= f(a)+f(a+n*h)
    total *= h/2
    return total 

# Calculo do coeficiente de convergencia

r1 = trapezio(m.pi/2,m.pi,100)
r2 = trapezio(m.pi/2,m.pi,200)
r3 = trapezio(m.pi/2,m.pi,400)

coeficiente = (r2-r1)/(r3-r2) 
print("r1:",r1)
print("r2:",r2)
print("r3", r3)
print("coeficiente:", coeficiente)

# Calculo do erro 

erro = (r3-r2)/3
print("erro:", abs(erro))


		-----SIMPSON
def f(x): 

    
def simpson(a,b,n):
    total = 0
    h = (b-a)/n
    for i in range(1,n,2):  #odd values
        total += 4*f(a+i*h)
    for i in range(2,n,2):  #even values 
        total+= 2*f(a+i*h)

    total+= f(a)+f(a+n*h)   #get the first value and last value
    total *= h/3

    return total 

# Calculo da convergencia
r1 = simpson(m.pi/2, m.pi, 200)
r2 = simpson(m.pi/2, m.pi, 400)
r3 = simpson(m.pi/2, m.pi, 800)

coeficiente = (r2-r1)/(r3-r2)
 
print("r1:",r1)
print("r2:",r2)
print("r3", r3)
print("coeficiente:", coeficiente)

# Calculo do erro
erro = (r3-r2)/15
print("erro:", abs(erro)) # erros sempre em modulo


		-----TRAPEZIO CUBATURA
total = 0
hx=1
hy=1
xy = [[1.1,1.4,7.7],[2.1,3.1,2.2],[7.3,1.5,1.2]]

for i in range(len(xy)):
    for j in range(len(xy)):
        if((i==0 or i==len(xy)-1) and (j==0 or j==len(xy)-1)):
            total+=xy[i][j]
        elif(i==0 or i==len(xy)-1 or j==0 or j==len(xy)-1):
            total+=2*xy[i][j]
        else:
            total+=4*xy[i][j]
            
total*=(hx*hy)/4
print("valor: ",total)


		-----SIMPSON CUBATURA
total = 0
hx=1
hy=1
xy = [[1.1,1.4,7.7],[2.1,3.1,2.2],[7.3,1.5,1.2]]

for i in range(len(xy)):
    for j in range(len(xy)):
        if((i==0 or i==len(xy)-1) and (j==0 or j==len(xy)-1)):
            total+=xy[i][j]
        elif(i==0 or i==len(xy)-1 or j==0 or j==len(xy)-1):
            total+=4*xy[i][j]
        else:
            total+=16*xy[i][j]
            
total*=(hx*hy)/9
print("valor: ",total)


		-----EULER
def f(x,y):


#arbitrado delta(x) = h

def Euler(x,y,xf,h):
    while (x < xf):
        y = y + h*f(x,y)
        x = x + h 
    print("x:",x)
    return y

r1 = Euler(0,0,6,2*m.pi/20)
r2 = Euler(0,0,6,2*m.pi/40)
r3 = Euler(0,0,6,2*m.pi/80)

print("y1:",r1)
print("y2:",r2)
print("y3:",r3)
quociente = (r2 - r1)/(r3-r2)
erro = (r3-r2)
print("quociente", quociente) 
print("erro:", erro)


		-----RK2
def f(x,y):

def rk2(x,y,xf,h):
    while (x < xf):
        y = y + h*f(x+h/2,y+h/2*f(x,y))
        x = x + h
    return y

r1 = rk2(0,0,6,2*m.pi/160)
r2 = rk2(0,0,6,2*m.pi/320)
r3 = rk2(0,0,6,2*m.pi/640)

print("s1 =", r1) 
print("s2 =", r2)
print("s3 =", r3)

quociente = (r2-r1)/(r3-r2)
print("quociente =", quociente)
erro = (r3-r2)/3
print("Erro =", erro)


		-----RK4
def f(x,y):

def rk4(x,y,xf,h):
    while (x < xf):
        delta_1 = h*f(x,y)
        delta_2 = h*f(x + (h/2), y+ (delta_1/2))
        delta_3 = h*f(x + (h/2), y + (delta_2/2))
        delta_4 = h*f(x + h, y + delta_3)
        
        y = y + (delta_1/6) + (delta_2/3) + (delta_3/3) + (delta_4/6)
        
        x = x + h
    return y

r1 = rk4(0,0,6,2*m.pi/160)
r2 = rk4(0,0,6,2*m.pi/320)
r3 = rk4(0,0,6,2*m.pi/640)

print("s1 =", r1) 
print("s2 =", r2)
print("s3 =", r3)

quociente = (r2-r1)/(r3-r2)
print("quociente =", quociente)
erro = (r3-r2)/15
print("Erro =", erro)


		-----EULER_2
#z = dy/dx
#dz = d2y/dx2

def dz(x,z):
    return 2 + x**2 +x*z

h=0.25
x=1
y=1
z=0

def euler_2(x,y,z,h):
    for i in range(3):
        print("iteracao: ",i)
        deltaz=dz(x,z)
        x+=h
        y+=h*z
        z+=h*deltaz


		-----RK4_2
#z = dy/dx
#dz = d2y/dx2

def dz(x,z):
    return 2 + x**2 +x*z

h=0.25
x=1
y=1
z=0

def rk4_2(x,y,z,h):
    for i in range(3):
        print("iteracao: ",i)
        z1 = (h*z)
        dz1=h*dz(x,z)
        z2=(h * (z + dz1/2))
        dz2=(h * (dz(x + h/2, z + dz1/2)))
        z3=(h * (z + dz2/2))
        dz3=(h * (dz(x + h/2, z + dz2/2)))
        z4=(h * (z + dz3))
        dz4=(h * (dz(x + h, z + dz3)))
        y+=z1/6 + z2/3 + z3/3 + z4/6
        z+=dz1/6 + dz2/3 + dz3/3 + dz4/6
        x+=h;


		-----PESQUISA
def f(x):

def pesquisa(guess, step): 
    if(f(guess) < f(guess+step)):
        step  -= step 

    x0 = guess 
    x1 = guess + step 
    x2 = guess + 2*step 
    while(f(x1) > f(x2)):
        x0 = x1 
        x1 = x2
        x2 = x2 + step
    print(x0,x1,x2)
    return [x0,x1,x2]

#lista = pesquisa(3.14, 0.00001)


		-----TERCOS
#PESQUISA UNIDIMENSIONAL
#TRISECÇÃO
#FUNCAO TEM DE SER CONVEXA ENTRE a E b

#METODO DOS TERÇOS : RAZAO = 1/3

def f(x):

def tercos(a,b,precisao):
    razao = 1/3
    while (abs(b-a) > precisao):
        c = a + razao *(b-a)
        d = b - razao *(b-a)
        if (f(c) < f(d)):
            b = d
        else: 
            a = c
            
    return [a,b]

#tercos(m.pi/2, 3/2*m.pi, 0.00001)

5
		-----AUREA
#TRISSECCAO
#FUNCAO TEM DE SER CONVEXA ENTRE a E b

#METODO SECCAO AUREA
#B = (m.sqrt(5)-1)/2
#A = B**2

import math as m

def f(x):
    return m.sin(x)**2

def aurea(a,b,precisao):
    razao = ((m.sqrt(5)-1)/2)**2
    c = a + razao *(b-a)
    d = b - razao *(b-a)
    fc = f(c)
    fd = f(d)
    while (abs(b-a) > precisao):
        if (fc < fd):   #Metodo para minimos, maximo: trocar fc>fd
            b = d
            #fb = fd
            d = c
            fd = fc
            c = a + razao *(b-a)
            fc = f(c)
        else: 
            a = c
            #fa = fc
            c = d
            fc = fd
            d = b - razao *(b-a)
            fd = f(d)
            
    return [a,b]

#aurea(m.pi/2, 3/2*m.pi, 0.00001)


		-----GRADIENTE
def f(x,y):

def dfx(x,y):

def dfy(x,y):


def gradient(x,y,h):
    for i in range(60): 
        xn = x - h*dfx(x,y)
        yn = y - h*dfy(x,y)
        if (f(xn,yn) < f(x,y)):
            h *= 2
            y = yn
            x = xn

        elif (f(xn,yn) > f(x,y)):
            h/= 2

    return [x,y]

print(gradient(1,1,1))
k = gradient(1,1,1)
print(f(k[0],k[1]))


		----QUADRICA
def f(x,y): 

def dfx(x,y): 

def dfy(x,y): 

def dfxx(x,y): 

def dfyy(x,y):

def dfxy(x,y): 

def dfyx(x,y): 

    
#xn+1 = xn - invert(hessiana).gradient
def quadrica(x,y):
    # se usar while loop da treta. Não sai do primeiro ciclo 
    for i in range(20): 
        x_ant = x
        y_ant = y 
        det = dfxx(x_ant,y_ant) * dfyy(x_ant,y_ant) - dfxy(x_ant,y_ant) * dfyx(x_ant,y_ant) 
        x = x_ant - (dfyy(x_ant,y_ant)*dfx(x_ant, y_ant) - dfxy(x_ant,y_ant)*dfy(x_ant,y_ant))/det
        y = y_ant - (-dfxy(x_ant, y_ant)* dfx(x_ant, y_ant) + dfxx(x_ant, y_ant) * dfy(x_ant, y_ant))/det
        print(x,y)
    return [x,y]

r = quadrica(0,0)
print(f(r[0],r[1]))     


		-----LEVENBERG-MARQUARDT
def f(x,y): 

def dfx(x,y):

def dfy(x,y): 

def dfxx(x,y):

def dfyy(x,y):

def dfyx(x,y):

def dfxy(x,y): 


#xn+1  xn - invert(hessiana).gradient + lambda.gradiente
def levenberg(x,y,h):
    x_ant = x 
    y_ant = y
    for i in range(20): 
        det = dfxx(x_ant,y_ant) * dfyy(x_ant,y_ant) - dfxy(x_ant,y_ant) * dfyx(x_ant,y_ant) 
        x = x_ant - (dfyy(x_ant,y_ant)*dfx(x_ant, y_ant) - dfxy(x_ant,y_ant)*dfy(x_ant,y_ant))/det - h*(dfx(x_ant,y_ant))
        y = y_ant - (-dfxy(x_ant, y_ant)* dfx(x_ant, y_ant) + dfxx(x_ant, y_ant) * dfy(x_ant, y_ant))/det - h*(dfy(x_ant,y_ant))
        if (f(x,y)<f(x_ant,y_ant)):
            h*=2
            x_ant = x
            y_ant = y 
        else:
            h/=2
        print(x,y)
    return [x,y]

r = levenberg(1,1,1)
print(f(r[0],r[1]))