# How does Django Work?

Django follows the MVT design pattern (Model View Template).

<ul>
    <li>Model - The data you want to present, usually data from a database.</li>
    <li>View - A request handler that returns the relevant template and content - based on the request from the user.</li>
    <li>Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.</li>
</ul>

# Model

The model provides data from the database.

In Django, the data is delivered as an Object Relational Mapping (ORM), which is a technique designed to make it easier to work with databases.

The most common way to extract data from a database is SQL. One problem with SQL is that you have to have a pretty good understanding of the database structure to be able to work with it.

Django, with ORM, makes it easier to communicate with the database, without having to write complex SQL statements.

The models are usually located in a file called models.py.

# View

A view is a function or method that takes http requests as arguments, imports the relevant model(s), and finds out what data to send to the template, and returns the final result.

The views are usually located in a file called views.py.

Template
A template is a file where you describe how the result should be represented.

Templates are often .html files, with HTML code describing the layout of a web page, but it can also be in other file formats to present other results, but we will concentrate on .html files.

Django uses standard HTML to describe the layout, but uses Django tags to add logic:

    <h1>My Homepage</h1>

    <p>My name is {{ firstname }}.</p>

The templates of an application is located in a folder named templates.

# URLs

Django also provides a way to navigate around the different pages in a website.

When a user requests a URL, Django decides which view it will send it to.

This is done in a file called urls.py.

# So, What is Going On?

When you have installed Django and created your first Django web application, and the browser requests the URL, this is basically what happens:

<ol>
    <li>Django receives the URL, checks the urls.py file, and calls the view that matches the URL.</li>
    <li>The view, located in views.py, checks for relevant models.</li>
    <li>The models are imported from the models.py file.</li>
    <li>The view then sends the data to a specified template in the template folder.</li>
    <li>The template contains HTML and Django tags, and with the data it returns finished HTML content back to the browser.</li>
</ol>

Django can do a lot more than this, but this is basically what you will learn in this tutorial, and are the basic steps in a simple web application made with Django.
