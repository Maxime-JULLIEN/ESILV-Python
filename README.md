# ESILV-Python
ESILV Project - Python for data analysis 

ADD EXPLANATION

## Installation

### Jupyter Notebook - MUST BE MODIFIED

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

### Interface and API

To start the API, you have to build the docker containers :

```bash
docker-compose up --build
```

We use Traefik to deploy this project aside other projects.
If you want to deploy it, you must change the domain name of your server for those lines:

```yaml
- "traefik.http.routers.interface_python_data.rule=Host(`python-data.linkable.tech`)"
- "traefik.http.routers.backend_python_data.rule=Host(`python-data.linkable.tech`) && PathPrefix(`/api`)"
```


## Usage

### Jupyter Notebook ??????????


```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

### API

The API was developed using [Flask](https://pypi.org/project/Flask/).

The route /api/predict was created to receive a POST request containing the key "content" in a JSON body. The content represent an email.

```yaml
{
    "content": "a SPAMMMMM email !!!!"
}
```

The request response must be like this if there is no error :

```yaml
{
    "prediction": true
}
```

True means the email is a SPAM and False means the email is NOT a SPAM


## Conclusion

