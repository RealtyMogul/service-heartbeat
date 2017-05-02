# service-heartbeat
Contains importable heartbeat views

You probably shouldn't be using this from scratch. Your cookiecutter service generator should already be making use of this.

To make this code available in an already existing project. Add the following to your requirements file::

    -e git+git://github.com/RealtyMogul/service-heartbeat.git#egg=service_heartbeat

The lib should be installed next time you run setup against your requirements.txt

To add the code to your lib, figure out which framework you're interested in. Using pyramid as an example add the following to __init__.py::

    config.include('service_heartbeat.pyramid_views')
