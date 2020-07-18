C File: ChangeToOnes.f
C This function just changes all the entries in an array to 1's
C
      subroutine changeToOnes(a,n)
C
      integer n
      real*8 a(n)
      do i=1,n
         a(i) = 1.0d0
      enddo
      end
C end file: ChangeToOnes.f