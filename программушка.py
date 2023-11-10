Var0 = int(input())
def Var1 (Var0):
	if Var0 == 0:
		return(1)
	else:
		return(Var0*Var1(Var0-1))
print(Var1(Var0))
input('Ведай любую кнопушку')