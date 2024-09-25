class solution:
    def _init_(self):
        self.MAX=20
        self.A=[0]*self.MAX
    def placement(self,i,j):
        for k in range(1,i):
            if(self.A[k]==j) or abs(self.A[k]-j)==abs(k-i):
                return False
        print(self.A)
        return True
    def printplacedqueen(self,N):
        print('Arrangement--->')
        print()
        for i in range(1,N+1):
            for j in range(1,N+1):
                if self.A[i] != j:
                    print('\t_',end=' ')
                else:
                    print('\tQ',end=' ')
            print()
            print()
    def N_Queens(self,i,j):
        for k in range(1,N+1):
            if self.placement(i,k):
                self.A[i]=k
                if i == N:
                    self.printplacedqueen(N)
                else:
                    self.N_Queens(i+1,N)
N=int(input("Enter the queens value:"))
obj=solution()
obj.N_Queens(1,N)
