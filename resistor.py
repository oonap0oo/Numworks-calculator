E12 = (1.0,1.2,1.5,1.8,2.2,2.7,3.3,3.9,4.7,5.6,6.8,8.2)
E24 = (1.0,1.1,1.2,1.3,1.5,1.6,1.8,2.0,2.2,2.4,2.7,3.0, \
       3.3,3.6,3.9,4.3,4.7,5.1,5.6,6.2,6.8,7.5,8.2,9.1)  

def series_parallel(Rx, Evalues):
    Rser_best=0;Rpar_best=0
    for exponent1 in range(1,6):
        for manitissa1 in Evalues:
            R1=float(str(manitissa1)+"E"+str(exponent1))
            if R1==Rx: # the requested res value exists in the Evalues
                return (round(R1),)
            for exponent2 in range(1,6):
                for manitissa2 in Evalues:
                    R2=float(str(manitissa2)+"E"+str(exponent2))
                    Rs=R1+R2
                    Rp=1/(1/R1+1/R2)
                    if abs(Rs-Rx)<abs(Rser_best-Rx):
                        Rser_best=Rs
                        R1ser_best=round(R1)
                        R2ser_best=round(R2)
                    if abs(Rp-Rx)<abs(Rpar_best-Rx):
                        Rpar_best=Rp
                        R1par_best=round(R1)
                        R2par_best=round(R2)
    return (R1ser_best,R2ser_best,R1par_best,R2par_best)

def find_best_res(rx=None):
    print("Match Rx with 2 res.")
    if rx==None:
        rx=float(input("Resistance value? "))
    else:
        print("Resistance value =",rx)
    E12match=series_parallel(rx,E12)
    E24match=series_parallel(rx,E24)
    if len(E12match)==1:
        print("Value exists as E12\n",E12match[0])
    else:
        print("E12 values:")
        print("Best series combination\n",*E12match[0:2])
        print("Best parallel combination\n",*E12match[2:4])
    if len(E24match)==1:
        print("Value exists as E24\n", E24match[0])
    else:
        print("E24values:")
        print("Best series combination\n",*E24match[0:2])
        print("Best parallel combination\n",*E24match[2:4])
        
find_best_res()
