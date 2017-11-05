# microframework

Copy-pasted from StackOverflow & written from scratch code snippets I use in projects. You can use them as you wish.

## Disclaimer

This isn't a one-purpose framework and will never be.

## Documentation

### class PereodicTask

`PereodicTask(task, interval)` — repeat procedures in background with interval in seconds

Example:

```python
def rss_update():
    # some stuff here
    print('rss updated')

r = PereodicTask(rss_update, 10)
# some other stuff
```

This code will run `rss_update` in background once per 10 seconds while `some other stuff` keep working in the main thread.

You can stop task with `r.stop()` method or just `del r`

### class JSONDB

JSON config or database (very simple) backend. Example:

`config.json`

```json
{
    "password": "12345"
}
```

`auth.py`

```python
credentials = JSONDB('config.json')

password = input('Password: ')

if password == credentials.get('password'):
    print('Login success')

new_password = input('Enter new password: ')
credentals.update('password', new_password)
credentials.save() # write to disk

```

## License

MIT