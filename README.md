
Flask Starter Kit
==========

Flask Starter Kit is a starting template for Flask. It has a basic structure for models, configurations 
and some fundamental components added. D3, Bootstrap etc is added since I currently work from China
so CDNs are not a good option from here. Just switch to CDNns if you prefer that. 

Prepare your project
--------------------

After cloning you have a few manual changes to do

### run.y

We will try to load a configuration file which path is set in this environment variable. 
It is likely to be used in production while you can rely on the standard config for development.

app.config.from_envvar('YOURAPP_SETTINGS')

### templates/base.html


<title>*YourApp*</title>


<a class="navbar-brand" href="#">*YourApp*</a>


<div class="mastfoot">
  <div class="inner">
    <p>© 2014 *YourApp*. All rights reserved.</p>
  </div>
</div>


### templates/index.html
<h1 class="cover-heading">*YourApp*</h1>
