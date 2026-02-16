# generateprofile
This little library makes it simplier to generate random profiles to make requests : it randomly gets an ip address and a user agent from a giant list

Place the folder in your project folder and you can try this code out

```python:main.py
from generateprofile import profile

prof = profile.GenerateProfile()
print(prof.getProxy())
print(prof.getUserAgent())
```

If everything works it should ouptput something like that
````md
216.24.57.13:80
Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7
````
