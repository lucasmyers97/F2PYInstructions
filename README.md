# F2PY Instructions
What follows is a brief guide for how to use the F2PY package to compile Fortran code into an importable Python package. Additionally, there is a brief guide about how to set up the relevant compiler on a machine running Windows. 
## Setting up the necessary Fortran and C compilers on Windows
Before starting, I'll note that there is a really good Stack Overflow post [here][SO1] explaining how to do this. Now, if you don't already have a Fortran compiler installed (one is not installed by default on Windows), you will need to do that. For this tutorial, we use [gfortran][fg] which comes with the [MinGW][MGW] framework which incorporates a bunch of compilers. MinGW can be downloaded [here][MGWD]. I recommend using the "Online Installer" for ease of use. However, note that you will need to change the default architecture from i686 to x86_64 if you are on a machine running x86 architecture (which you probably are). 

After you have completed the installation, you'll need to add the MinGW binary files folder to your Path environment variable so that your computer knows where to look for the compilers. To do this, you first need to find where MinGW is kept. Search "This PC" in the search bar and click the `This PC` app. If it is installed in the default folder, you should be able to get to it by navigating `C:\Program Files\mingw-w64\x86_64-8.1.0-posix-seh-rt_v6-rev0\mingw64\bin`. It may be that you have installed a slightly different version, so you'll have to navigate through `Program Files`, `mingw-w64`, etc. by just clicking through until you find the `bin` folder. In any case, once you find it copy the folder path. 

To add this path to your Path environment variable, seach "Environment Variables" in your Windows search bar and then click the `Edit the system environment variables` prompt. Then click the `Environment Varibles...` button. There should be a variable called `Path`. Double clicking that should bring up the paths stored in your Path environment variable. Double click on an empty space and paste in the folder path. That's all!

## Compiling simple Fortran programs and making them more "pythonic"


[SO1]: https://stackoverflow.com/questions/48826283/compile-fortran-module-with-f2py-and-python-3-6-on-windows-10
[fg]: https://gcc.gnu.org/wiki/
[MGW]: http://www.mingw.org/
[MGWD]: https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/7.2.0/threads-posix/seh/
