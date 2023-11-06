# Description of Sections


## Dependencies

### glad
- GitHub: https://github.com/Dav1dde/glad

- In the context of OpenGL, "GLAD" is a library that acts as an OpenGL loader generator. It's not part of the OpenGL core API, but it is used to manage the loading of OpenGL functions in a portable and easy way across different platforms.

- OpenGL itself doesn't manage the direct communication between your application and the graphics drivers on your system. Instead, the system's graphics drivers provide the implementation of the OpenGL functions. Since different systems have different capabilities and different sets of functions they can support, these functions are not always available directly to be called.

- GLAD steps in to help with this issue. When developing an application with OpenGL, you can't just call an OpenGL function directly from your code because at compile time, the address of that function is not known. The functions need to be queried and loaded at runtime because their locations are determined by the driver at that time.

- Here's what GLAD does for you:
    1. Function Loading
        - It loads the function pointers (addresses) to OpenGL functions at runtime. This means that your application can use different versions and extensions of OpenGL without having to link to a specific OpenGL library at compile time.
    2. Extension Handling
        - It provides a convenient way to check at runtime whether a certain OpenGL extension is supported by the host system.
    3. Loader Generation
        - You can generate a GLAD loader specific to the version of OpenGL and the set of extensions that you need for your application.
    4. Language Support
        - Although typically used with C or C++, it also has support for other languages.


### imgui
- GitHub: https://github.com/ocornut/imgui

- Dear ImGui, often just referred to as ImGui, is an immediate mode graphical user interface (GUI) toolkit for C++. It is a bloat-free library that is particularly popular in game development and other real-time applications, but it can be used in any context where a simple, portable, and easy-to-integrate GUI is needed.

- Immediate mode GUI libraries like ImGui differ from retained mode GUIs in that they are rebuilt every frame. You don't explicitly create and maintain a persistent set of widgets or controls. Instead, you provide the GUI code in your application's render loop, and it's run every frame to process events and show the UI.

- Dear ImGui is designed to be renderer agnostic, so it does not include the code to display the UI it creates. Instead, you need to provide a rendering backend. This is often done using popular graphics libraries like OpenGL, DirectX, or Vulkan. Similarly, it's designed to be platform agnostic, so it doesn't deal directly with the underlying platform windowing or the input system. Instead, you use platform-specific bindings, like those provided for GLFW, SDL, Win32, etc.

- Some important features include:
    1. Minimize state synchronization.
        - With retained mode GUIs, there's often a complex system in place to ensure that the UI reflects the current state of the application. ImGui avoids this by having no retained state. You create the UI from the current state of your application each frame. This eliminates the need for a separate system to synchronize the UI with the game or application state.
    2. Minimize UI-related state storage on user side.
        - Since ImGui is an immediate mode GUI library, it does not require developers to store the state of UI elements between frames. This greatky reduces the memory footprint and state management complexity on the developer's side.
    3. Minimize Setup and Maintenance
        - ImGui is known for its ease of integration and minimal setup requirements. There's no need for separate UI design files or complex initialization. 
        - A developer can start adding UI elements with just a few lines of code, and changes can be seen and tested immediately.
    4. Easy to create dynamic UI
        - When you're working with data that changes rapidly (like variables in a game debug menu), ImGui's immediate mode approach allows you to create a UI that is a direct reflection of your current dataset without extra work to ensure that changes in the data are reflected in the UI.
    5. Easy to create Code-Driven and Data-Driven Tools
        - Because you are essentially drawing the UI each frame based on the application's current state or data, it's straightforward to build tools that change based on what the code or data dictates. This can range from simple debug tools to complex in-game editors or other development tools.
    6. Easy to create Ad Hoc and Elaborate Tools
        - The simplicity of ImGui's API makes it perfect for quickly creating tools for specific tasks (ad hoc). At the same time, its robustness allows for the development of more permanent and elaborate tools, which can evolve with the needs of the project.
    7. Portable, Minimize Dependencies
        - ImGui has minimal dependencies, relying only on C++ standard libraries. This makes it highly portable and easy to run on various platforms, including consoles and mobile devices where standard OS features might not be available or are different from the desktop environment.
    8. Efficient Runtime and Memory Consumption
        - ImGui is designed to be lightweight and efficient, both in terms of CPU and memory usage. This efficiency is crucial for high-performance applications like games, where resource management is critical.


### nfd
- GitHub: https://github.com/mlabbe/nativefiledialog

- Native File Dialog (NFD) is a small, portable C++ library that provides bindings to the native file dialog APIs of various platforms. When you want to open or save files using a dialog box in a C++ program, you could write your own code using the operating system's APIs or use a cross-platform toolkit like Qt or wxWidgets. NFD offers an alternative that's much lighter-weight than such toolkits.

- The advantage of using NFD is that it gives you a file dialog that looks and feels like it's part of the user's operating system, because it is. THis can be important for desktop applications where you want to match the native look and feel as closely as possible.

- Here are some key points about Native File Dialog:
    1. Cross-Platform
        - NFD provides a consistent interface across different operating systems such as Windows, macOS, and various Linux distributions.
    2. Lightweight
        - It is designed to be minimalistic, doing only one thing and doing it well, without the overhead of larger GUI libraries.
    3. Native Look and Feel
        - It uses the operating system's native file dialog, ensuring that your application's file dialog will look familiar to users.
    4. Easy to Integrate
        - Because it's a small library, it's relatively easy to add to existing projects.
    5. Open Source
        - The library is typically open source, meaning you can use and modify it according to its license.


### sejp
- GitHub: https://github.com/ixchow/sejp

- The Somewhat Eager JSON Parser, abbreviated as SEJP, is a specialized software library that is used for parsing JSON (JavaScript Object Notation) data within C++ programs. JSON is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate. It is commonly used for transmitting data in web applications and for storing configuration settings.

- The primary function of SEJP is to take JSON formatted data that is typically received as a stream — for example, from a file, a network connection, or standard input — and then process that data into a form that is usable within a C++ program. 

- In this context, "dynamically-typed values" means that the data types of the values in the JSON data are determined at runtime rather than at compile time, which is the norm for statically-typed languages like C++. This dynamic typing is beneficial when dealing with JSON because JSON data structures can contain a mix of types such as numbers, strings, booleans, arrays, and objects, and the schema of the JSON might not be known until the data is actually read.


### Command Line Parser for C++11
- GitHub: https://github.com/CLIUtils/CLI11

- CLI11 is a contemporary, header-only library for parsing command line arguments in C++11 and later standards. Developed with usability and flexibility in mind, it provides a straightforward way for C++ developers to create command line interfaces that are both powerful and easy to understand. As a modern library, CLI11 leverages the enhanced features of C++11, such as smart pointers, lambda functions, and automatic type deduction, to facilitate a more expressive and efficient codebase.

- At its core, CLI11 allows developers to define expected arguments, flags, options, and subcommands in their applications with minimal boilerplate. This definition includes the setup of default values, type-checking, and customized help messages. The library handles parsing the command line inputs and automatically converts them to the defined C++ types. It also generates help and error messages, which reduces the need for additional code to handle common command line interface tasks.

- One of the defining features of CLI11 is its support for subcommands, enabling the creation of nested command-line interfaces. This is particularly useful for complex applications that perform a variety of functions, each potentially requiring its own set of options and parameters. Additionally, CLI11's composability means that these subcommands and their interfaces can be defined in isolation and then combined, promoting modular design.

### stb_image.h
- GitHub: https://github.com/nothings/stb

- stb_image.h is a notable part of the "stb" collection of libraries for C/C++ which provides a robust solution for image loading and decoding. It serves as a standalone tool for loading images from various file formats, which includes popular ones such as JPEG, PNG, BMP, TGA, and GIF, among others.

- The usability of stb_image.h extends to its versatility and customization. Programmers can load images with varying channel requirements, converting them on-the-fly to grayscale, RGB, or RGBA. Moreover, it allows for customization through preprocessor macros to toggle features or adjust memory allocation strategies, catering to both simple and advanced use cases.


### stb_image_write.h
- GitHub: https://github.com/nothings/stb

- stb_image_write.h is a complementary header file to stb_image.h within the stb library collection, which is designed to facilitate the saving of images to disk.

-  It can be used to quickly snapshot the state of a rendering application or save procedurally generated textures. Its API is intentionally kept straightforward, which means saving an image can typically be done with a single function call that specifies the desired image format, quality, and destination file path.

- Developers can fine-tune the compression levels for certain formats, and the library offers the ability to define custom memory allocation and deallocation functions, allowing it to be adapted for various environments or stricter memory management regimes.


### stb_perlin.h
- GitHub: https://github.com/nothings/stb

- stb_perlin.h is part of the stb single-file public domain libraries for C/C++, which provides functions to generate Perlin noise. Perlin noise, created by Ken Perlin in the 1980s, is a gradient noise function that is widely used in computer graphics to produce natural-looking textures, terrain, and other procedural generation tasks.

- The functions provided by stb_perlin.h allow generation of Perlin noise values at any point in 2D, 3D, or 4D space. It also offers features such as seamless tiling of noise, which is quite useful for generating textures that can be tiled without visible seams. Additionally, there are options to adjust parameters like octaves, for fractal noise generation, to control the level of detail and how "zoomed in" or "smooth" the noise appears.
