# GLFW CMake ImGUI starter

This starter project allows you to use CMake to create a project with GLFW and ImGUI. The code is multi-platform and runs on Windows, Linux and MacOS.

GLFW homepage: [glfw.org](https://www.glfw.org/)    
GLFW on GitHub: [github.com/glfw/glfw](https://www.github.com/glfw/glfw)

Original Repo, of which this is a fork- [juliettef/GLFW-CMake-starter](
https://github.com/juliettef/GLFW-CMake-starter)


## Getting the code

The easiest way to get hold of the starter code is to run the following command using a shell you can run git from:

```  
git clone --recursive https://github.com/MrStudentGuy/GLFW-Cmake-ImGUI-Starter  
```  

If you are on Windows you can download git from [git-scm.com/download/win](https://git-scm.com/download/win) and use the right click menu in Windows File Explorer to "Git Bash here" and then run git commands.

This will create the directory _GLFW-Cmake-ImGUI-Starter_ and get the latest source code, using the ```--recursive``` option to download the GLFW and ImGUI code which is included in the repository as a submodule. If you want to run further git commands from the command line you'll need to cd into the directory:

```  
cd GLFW-Cmake-ImGUI-Starter
```  

Alternatively you can use a git GUI program such as [Fork](https://git-fork.com/) to get the code. Most of these will automatically download the git submodules.

If you download the code from GitHub via the "Download ZIP" approach, you'll also need to download GLFW into the _glfw_ folder. The correct version can be found by clicking on the _glfw_ folder you see on the [front page of the _GLFW-CMake-starter_ GitHub repository](https://github.com/juliettef/GLFW-CMake-starter).

## Using CMake to create the project

From a command prompt in the `GLFW-CMake-starter` directory:
1. `mkdir out`
2. `cd out`
3. `cmake ..` (for MinGW the build system generator needs to be specified using the -G option: `cmake .. -G "MinGW Makefiles"`)
4. Either run `make all` or for Visual Studio open `GLFW-CMake-starter.sln` or for MinGW run `mingw32-make`

## Using the framework

All application files should be added to the `/app` directory, inside which, is a `README.md` file with further, and more detailed instructions.

Happy Coding!