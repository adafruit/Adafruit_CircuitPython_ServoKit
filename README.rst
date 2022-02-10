Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-servokit/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/servokit/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_ServoKit/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_ServoKit/actions/
    :alt: Build Status

CircuitPython helper library for the PWM/Servo FeatherWing, Shield and Pi HAT and Bonnet kits.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
* `Register <https://github.com/adafruit/Adafruit_CircuitPython_Register>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
--------------------

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-servokit/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-servokit

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-servokit

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-servokit

Usage Example
=============

.. code-block:: python

    import time
    from adafruit_servokit import ServoKit

    # Set channels to the number of servo channels on your kit.
    # 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
    kit = ServoKit(channels=8)

    kit.servo[0].angle = 180
    kit.continuous_servo[1].throttle = 1
    time.sleep(1)
    kit.continuous_servo[1].throttle = -1
    time.sleep(1)
    kit.servo[0].angle = 0
    kit.continuous_servo[1].throttle = 0


Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/servokit/en/latest/>`_.

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_ServoKit/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
