# django_sass_base_template
Generally we gets fed up to setup the base css files for a new project, What we does is to write code from the beginning or just copy and paste the code from the other existing project.
So no more wasting time from now on. Just clone this project repo, follow the usage and you are done.

##Requirements
- [django-sass-processor](https://github.com/jrief/django-sass-processor "django-sass-processor") (Follow its doc for setup)

##Usage

####Step 1
Clone it and change the django_sass_base_template -> **your_project_name**

####Step 2
Import the common stylesheet directly in your each sass file to access all the variables, mixins and classes.

```sass
import  "../style.scss"
```
##Customization
**Colors**
Define the colors used in your project by replacing the following variable values :
> File location : /static/common/css/variables.scss

```sass
$color-primary : #00AAFD;         // Replace your project's primary color
$color-primary-light : #5CC8FD;   // Replace your project's primary-light color
$color-primary-dark : #007CB9;    // Replace your project's primary-dark color
$color-primary-disabled : #B9E7FE;// Replace your project's primary-disabled color

$color-accent : #ffeea8;          // Replace your project's accent color
$color-accent-light : #FFDEA5;    // Replace your project's accent-light color
$color-accent-dark : #c8ae81;     // Replace your project's accent-dark color
$color-accent-disabled : rgba(255, 222, 165, 0.48); // Replace your project's accent-disabled color
```
**Buttons**
All the premade basic buttons are available here(No external css framework used). You can just use it by using the default identifier values or customize it by replacing its values:
Check demo of all the premade buttons by running the server.
> File location : /static/common/css/variables.scss

```sass
$default-btn-identifier : '.btn';
$default-btn-floating-identifier : '.btn-floating'; 
$default-btn-primary-identifier : '.btn-primary';
$default-btn-outline-primary-identifier : '.btn-outline-primary';
```
##Scope
This project is made only to reduce the timing of setup the project when we work on sass projects. So this is a basic idea implemented here and there are so many things that can be improved here.
- Project Structure
- Code Styling
- Easy way to do this setup done.

This is my first github open source project made only for developers to reduce their precious time when making a new SASS project.
So PR's are most welcome :smile: .

###End
