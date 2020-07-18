c file: add1.f
c
      subroutine add1(a, b, m, n)
c
      integer m
      integer n
      real*8 a(m+2, n+2)
      real*8 b(m, n)
      do i=1,m
         do j=1,n
            a(i,j) = b(i,j) + 1
         enddo
      enddo
      end 
c endfile: add1.f