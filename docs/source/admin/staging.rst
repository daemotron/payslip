Staging System
==============

The staging system is a Heroku application with automatic deployments from the
:ref:`blessed Git repository's <blessed-repository>` master branch.

It is accessible under this URL:

https://ach-payslip-staging.herokuapp.com/


Heroku Configuration
--------------------

Due to security consideration and the specific behaviour of Heroku dynos, some
configuration has to be set up in Heroku to ensure consistent deployment results

Build Configuration
~~~~~~~~~~~~~~~~~~~

The following build configurations are required to build and deploy the application
correctly on a Heroku dyno:

================== ==================================================================
heroku/python      Standard Python build configuration provided by Heroku
================== ==================================================================

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

The following environment variables are needed to run the application. If one of them
is not set, the application will not start.

================= ====== ============================================================
``DATABASE_URL``  String Will be set automatically by Heroku if set up correctly
``SECRET_KEY``    String Needs to be set to provide the secret session key
================= ====== ============================================================


Deployment Prerequisites
------------------------

Automatic deployment will only be triggered for the master branch after all configured
CI checks have been run and provide a green status. Currently, two main checks are set up
for the master branch:

* Travis CI will build the application and run all unit tests available
* Quantifiedcode will scan all code in the master branch for potential issues


Automatic Deployment
--------------------

Any commit pushed to the master branch with green prerequisites will be automatically deployed.
This includes deployment of the application alongside with collecting all static files. However,
database migration has to be triggered manually (if needed).


Post-Deployment Activities
--------------------------

In case a commit includes new migrations, the database migration has to be triggered manually.
For security and reliability reasons, automatic migration has been excluded from the build
configuration.

To trigger migration manually, issue the following command on your local computer (Heroku Toolbelt
needs to be installed and set up correctly):

.. code-block:: bash

   heroku run -a ach-payslip-staging python manage.py migrate
