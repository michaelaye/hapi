# hapi

> DISCLAIMER: I only created this package out of the hapi.py modue file from hitran.org and did not participate in the writing of the physical code inside it. I only put together the installer scripts.


This is the hitran.org Python API for the HITRAN database.
This software can be downloaded at http://hitran.org/hapi/

Because I got surprised by un-announced difference between the version I downloaded in April 2015 and my colleague who downloaded their version in June/July 2015, I decided to archive versions here and add an installer so that people can just do

```python
python setup.py install
```
to add it to their environment.

## Some comments on code

* The delivered `hapi.py` module contains everything, but for a proper setup script functionality I need to distinguish between project name and package name. To avoid import chaos, I do an `from hapi import *` inside the `__init__.py` script
