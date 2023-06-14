##  techful_library

<img src="icon.png" align="right" />

##### Techful README [![Techful](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome#readme)
> Enrich you with ideas !

A library management software where you can view all the book present in your library, issue books to student. 📚

### Links

[Github](https://github.com/sotoriz)       
[project](https://sotoriz.github.com/landing.html)              
[project blog](https://medium.com/)       
[LinkedIn](https://https://www.linkedin.com/in/sotonye-orifama-6520bab0)
                
### 👉 If you like this repo then please give it a ⭐️

### Short Description
This is a software which can efficiently manage your library. This app keeps track of the books present in the library -

* Add a new book(s)
* Delete any book
* View all the books in the library
* Issue book to student
* Accept books Return by student

### Specifications

I choose to use tkinter to build the project because i want a graphical user intetface(GUI) experience

###  Screenshots

<img src="images/capture1.jpg"
     alt="Homecaptures  Screen"
     style="float: left; margin-right: 10px;"
     width="200"/> <img src="images/capture2.jpg"
     alt="Home Screen"
     style="float: left; margin-right: 10px;"
     width="200"/> <img src="images/capture3.jpg"
     alt="Home Screen"
     style="float: left; margin-right: 10px;"
     width="200"/> <img src="images/capture4.jpg"
     alt="Home Screen"
     style="float: left; margin-right: 10px;"
     width="200"/> <img src="images/capture5.jpg"
     alt="Home Screen"
     style="float: left; margin-right: 10px;"
     width="200"/> <img src="images/capture6.jpg"
     alt="Home Screen"
     style="float: left; margin-right: 10px;"
     width="200"/>

     ## NOTE:
This project is subject to change by the developer and is still in development

### Installations
The following packages are required or should be installed for the project.

	tkinter - pip install tkinter
	Pillow - pip install pillow
	PyMySql - pip install pymysql


### Description of Tables

   Create Tables
   create database db;

create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));

create table books_issued(bid varchar(20) primary key, issuedto varchar(30));

### Usage

Running this is as simple as it gets. Follow this steps
1. Clone this repository
2. Double click on `main.py`
3. For Homepage run 
> python3 main.py


###  Contributing

Contributions are always welcome! Please read the `contribution guidelines` first.

###  Related projects

Library Management System – Python Project by Bartleby.com

### Author

Sotonye Orifama <sotorisfx@gmail.com>

### Licensing

This project is licensed under the MIT license. Feel free to edit and distribute this template as you like.

See `LICENSE` for more information.

```Copyright 2023 sotonye orifama

Getting Started

For help getting started with tkinter, view our online [documentation](https://docs.python.org/2/library/tkinter.html).
