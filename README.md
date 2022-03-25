# kolibri-desktop-auth-plugin

Authentication backend that allows an HTTP client to authenticate by providing
a desktop user token

# Testing

This is a kolibri plugin, you need to install the python package in the kolibri
python environment using pip and then enable the plugin.

```
 .../kolibri $ pip install -e ../kolibri-desktop-auth-plugin
 .../kolibri $ kolibri plugin enable kolibri_desktop_auth_plugin
```

To test you can launch the fake user info dbus daemon included in this
repository:

```
./fake-dbus-daemon.py
```

After enabling the fake dbus daemon you can try to autologin in your kolibri
with the plugin opening the following url in your browser:

http://localhost:8000/kolibri_desktop_auth_plugin/login/TOKEN1

You can change the TOKEN at the end of the url above to test with different
user data:

 * TOKEN1: adminuser, user with admin rights
 * TOKEN2: eosuser, user without admin rights

You can test also with a non existent token that should redirect to the login
page.

It's also possible to redirect after the authentication passing the next url as
a get parameter to the url, for example:

http://localhost:8000/kolibri_desktop_auth_plugin/login/TOKEN1?next=/learn

# Development

Setup the Python environment:

```
pipenv install
```

Setup pre-commit:

```
pipenv run pre-commit install
```

Enter the Python environment for development:

```
pipenv shell
```


# Releasing

## Creating a release

If you are releasing a new version, use `bump-version` with with `major`, `minor`, or `patch`. For example:

```
yarn bump-version patch
```

This creates a new commit and a git tag. Push this to the remote:

```
git push
git push --tags
```

Create a `.whl` file:

```
python setup.py bdist_wheel --universal
```

Finally, upload the `.whl` file to PyPi:

```
twine check -s dist/*
twine upload -s dist/*
```

