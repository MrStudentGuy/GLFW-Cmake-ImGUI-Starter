# How to Register and Create a New Window in Your Application
This guide will walk you through the process of registering and creating a new window in your application. We will be using the ImGui library for creating the window and the GLFW library for creating the OpenGL context.


## Note
There are two ways to do create and register a new window. 

1. You can use the Python script "AddWindow.py". Just run the script and follow the instructions. 
2. You can follow the steps below to create and register a new window manually.


## Step 1: Create a New Window Class
First, you need to create a new class for your window. This class should inherit from the UIWindow base class and implement the Render method. Here's an example:



    // MyWindow.h  
      
    #include "../UIWindow.h"  
      
    class MyWindow : public UIWindow {  
    public:  
	    MyWindow();
		void Render() override;
     };  

And the implementation:

    // MyWindow.cpp  
      
    #include "MyWindow.h"  
    #include <imgui.h>  
      
    MyWindow::MyWindow() 
    {  
	    // Register this window with the UIManager  
	    UIManager::RegisterUIWindow(this);  
    }  
      
    void MyWindow::Render() 
    {  
	    // Add code to draw your window using ImGui here
	    ImGui::Begin("My Window");  
	    ImGui::Text("Hello, world!");  
	    ImGui::End();  
    }  

## Step 2: Register the Window
In the constructor of your new window class, you should register the window with the UIManager using the RegisterUIWindow method. This is done in the MyWindow constructor in the example above.

## Step 3: Create an Instance of the Window
Finally, you need to create an instance of your new window class. This can be done in the main.cpp file:


    // main.cpp  
      
    #include "app/MyWindow.h" // Include your new window class  
      
    int main(void)  
    {  
	    // Create an instance of your new window class  
	    MyWindow myWindow;  
	    
		// Rest of your main function
	}  



### Attention!
Remember to replace MyWindow with the actual name of your new window class. This will create an instance of your new window when your application starts, and it will be registered with the UIManager due to the constructor of your new window class. Now, when UIManager::RenderUIWindows() is called in the main loop, it should render your new window.  That's it! You have successfully registered and created a new window in your application. You can add more windows by creating new classes that inherit from UIWindow, registering them with the UIManager in their constructors, and creating instances of them in the main.cpp file.