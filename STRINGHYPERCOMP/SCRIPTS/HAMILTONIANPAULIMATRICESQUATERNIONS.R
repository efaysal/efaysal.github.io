rm(list=ls(all=TRUE))

A=cbind(c(1,-1), c(-1,1))
a=runif(2)
b=runif(2)
alx=rbind()
for( epsilon in (1:100)/1000)
{
  #  epsilon=0.0000000001
  
A[2,1]=a[1]-1i*a[2]*epsilon
A[1,2]=a[1]+1i*a[2]*epsilon
A[1,1]=1i*b[2]*epsilon+b[1]
A[2,2]=-1i*b[2]*epsilon+b[1]
eigen(A)
A[2,1]=a[1]-1i*a[2]*epsilon
A[1,2]=a[1]+1i*a[2]*epsilon
A[1,1]=b[2]*epsilon+b[1]
A[2,2]=-b[2]*epsilon+b[1]
eigen(A)
# print(epsilon)
# print(eigen(A)$vectors)

w1=Re(eigen(A)$vectors[1,1]*Conj(eigen(A)$vectors[1,1]))
w2=Re(eigen(A)$vectors[1,2]*Conj(eigen(A)$vectors[1,2]))
w12=Re(eigen(A)$vectors[2,1]*Conj(eigen(A)$vectors[2,1]))
w22=Re(eigen(A)$vectors[2,2]*Conj(eigen(A)$vectors[2,2]))
alx=rbind(alx,c(epsilon,w1,w2,w12,w22))
} 
alx=data.frame(alx)
plot(alx$X1,alx$X1)
points(alx$X1,alx$X3)
points(alx$X1,alx$X2)
points(alx$X1,alx$X4)
points(alx$X1,alx$X5)




