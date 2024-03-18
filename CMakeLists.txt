cmake_minimum_required( VERSION 3.5 )
set (CMAKE_CXX_STANDARD 20)

project( GLFW-Cmake-ImGUI-Starter )

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin/lib)

find_package( OpenGL REQUIRED )

include_directories( ${OPENGL_INCLUDE_DIRS} imgui )

set( GLFW_BUILD_DOCS OFF CACHE BOOL  "GLFW lib only" )
set( GLFW_INSTALL OFF CACHE BOOL  "GLFW lib only" )
set( GLAD_GL "" )

add_subdirectory( glfw )

option( GLFW-CMAKE-STARTER-USE-GLFW-GLAD "Use GLAD from GLFW" ON )

if( GLFW-CMAKE-STARTER-USE-GLFW-GLAD )
    include_directories("${GLFW_SOURCE_DIR}/deps")
    set( GLAD_GL "${GLFW_SOURCE_DIR}/deps/glad/gl.h" )
endif()

if( MSVC )
    SET( CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /ENTRY:mainCRTStartup" )
endif()

set( SRC
        main.cpp
        UIManager.cpp
        UIManager.h
        UIWindow.h
)

set ( APP
        app/HelloWorld.cpp
        app/HelloWorld.h
)

set( IMGUI_SOURCES
        imgui/imgui.cpp
        imgui/imgui_demo.cpp
        imgui/imgui_draw.cpp
        imgui/imgui_widgets.cpp
        imgui/imgui_tables.cpp
        imgui/backends/imgui_impl_glfw.cpp
        imgui/backends/imgui_impl_glfw.h
        imgui/backends/imgui_impl_opengl3.cpp
        imgui/backends/imgui_impl_opengl3.h
)

add_executable( GLFW-Cmake-ImGUI-Starter WIN32 ${SRC} ${APP} ${GLAD_GL} ${IMGUI_SOURCES} )
target_include_directories(GLFW-Cmake-ImGUI-Starter PRIVATE imgui imgui/backends)  # Include the IMGUI headers
target_link_libraries( GLFW-Cmake-ImGUI-Starter ${OPENGL_LIBRARIES} glfw )

if( MSVC )
    if(${CMAKE_VERSION} VERSION_LESS "3.6.0")
        message( "\n\t[ WARNING ]\n\n\tCMake version lower than 3.6.\n\n\t - Please update CMake and rerun; OR\n\t - Manually set 'GLFW-Cmake-ImGUI-Starter' as StartUp Project in Visual Studio.\n" )
    else()
        set_property( DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY VS_STARTUP_PROJECT GLFW-Cmake-ImGUI-Starter )
    endif()
endif()
