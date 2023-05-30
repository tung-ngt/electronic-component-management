# Electronic Component Management System

## Member:
- Nguyễn Thanh Tùng - BI12-473 (views, mvc coordination, appflow design)
- Đoàn Hoài Nhi - BI12-338 (models design)
- Nguyễn Phan Gia Bảo - BI12-048 (controllers)
- Chu Bảo Minh - BI12-281 (models serializer and connector)
- Cấn Trung Hiếu - BI12-160 (connector and database)


## Description

In the project, we have built a GUI system for managing electric components. The Gui is completed with a dashboard (chart, summaries, ...) and screens to add and update components, manufacturers, customers, and orders.

In the project, we have followed the Object-Oriented Programming paradigm and Model-View-Controller pattern.

**Domain:**
- There are 4 main entities of concern Component, Manufacturer, Customer, and Order.
- Each Component has a Manufacturer.
- Each Order has a Customer and many Components.
- There are 5 subclasses of Component representing 5 big categories IC (Integrated Circut), Inductor, Capacitor, Sensor, and Resistor. They inherit from Component and have their own properties like clock, resistance, ...

**Serializers:** serializers are classes to translate Objects from the program into the database and vice versa.
- Every Serializer inherits from the base Serializer class which contains basic functions: load, load_many (create Object from the database query) and dump, dump_many (convert data from Object to data that can be pushed to the database)
- The subclass will override the load method to process data correctly.

**Controllers:**
- Each domain class has a corresponding controller. The controller uses the appropriate Serializers and database function to store and manipulate data of that type. It encapsulates logic and provides an interface for the View to access data.
- The AppController also provides additional methods such as compressing and decompressing images.
- We use SQLite as a storage system.
- The system also has the feature to store images of components and manufacturers. The images are compressed and stored in a folder. Their path is stored in the database. This way we can easily access the images and reduce their size. The image compression is done on the closing of the system. And decompression on the loading of the system.


**View (GUI):**
- The GUI class is the main class providing functions to build the navbar and screens; maintaining and navigating between them.
- All screens like dashboard, component, ... are inherited from the base Screen class. Screen is a tab with Subcreens.
- Button, Label, Frame, TreeView, ... are all inherited from the base class and customized.

A feature of the GUI is state retention. State retention is the ability to hold state or data of user interaction with the system like what they have entered in an entry or which screen they are on between navigation. To implement this feature we have developed 2 systems:
- Screen navigation: Screen can be navigated via the navbar without rerendering so the state is preserved. This is achieved by placing and unplacing the screen with <tt>grid</tt> and <tt>grid_forget</tt> functions. The list of available Screens is controlled by the GUI class.
- Subscreen navigation stack: Every Screen has its own navigation stack. Subscreens can be pushed or popped from this stack. Each Subscreen of a Screen is a class with a state property and a render function. The render function is run only when the Subscreen is pushed on the navigation stack and depends on the state. The state is clear on rerendering. A Subscreen can be popped from the stack and pushed back in for rerendering.


## Manual

### Initialize database steps

- Run generate_data.py to generate mock data
- Run generate_database.py to create the database


## Screenshots

![image](https://github.com/tung-ngt/electronic-component-management/assets/71141898/3823f5d9-0953-4940-ac28-6335acd72d59)
![image](https://github.com/tung-ngt/electronic-component-management/assets/71141898/c441e372-9318-4d47-86b8-bd02589c7077)
![image](https://github.com/tung-ngt/electronic-component-management/assets/71141898/a4650749-99dc-42d7-b02a-ed14e84bde1e)
![image](https://github.com/tung-ngt/electronic-component-management/assets/71141898/66146638-e65c-4148-82a4-a90b2a1f6830)
![image](https://github.com/tung-ngt/electronic-component-management/assets/71141898/4d3a75d6-850d-4c48-a521-37b4b92437de)


