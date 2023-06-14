program epsilon
    real*8,dimension(1:100)::frequencyx,frequencyy,frequencyz,xx,yy,zz
    real*8::beta,random1,beta2,random2,beta3,random3
    character*8 epsilonx, epsilony,epsilonz
      open (1, file="XX", status="unknown")
      open (2, file="YY", status="unknown")
      open (3, file="ZZ", status="unknown")
      do i = 1,10
        read(1,*)frequencyx(i),epsilonx,beta1,random1,xx(i)
        read(2,*)frequencyy(i),epsilony,beta2,random2,yy(i)
        read(3,*)frequencyz(i),epsilonz,beta3,random3,zz(i)
      end do

      do i = 1,10
      print*,frequencyx(i),xx(i),yy(i),zz(i)
      end do
end program
