# ESILV Python Project - Python for data analysis 

We decided to work on the Spambase Data Set. 

We had to __visualize__ the data and create a __model__ which predicts if a given email is a spam or not, based on several attributes.

- 48 float attributes which represent the frequency of a __specific word__
- 6 float attributes of type which represent the frequency of a __specific character__
- 1 float attribute which represents the __average__ length of uninterrupted __sequences of capital letters__
- 1 integer attribute which represents the length of __longest__ uninterrupted __sequence of capital letters__
- 1 integer attribute wich represents the __total__ number of __capital letters in the e-mail__
- 1 nominal class attribute which denotes whether the e-mail was considered __spam__ (1) or __not__ (0)

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

We had to discuss about the best __metric__ to use to evaluate our model. The __accuracy__ was the first metric we tought about, but it doesn’t take into account the __cost of False Positive cases__. Indeed, if the model classifies safe emails as spams, it will be a real problem for the user.

So we decided to focus on the __precision__ (= True Positive/Total Predicted Positive), which is a far better metric when the __cost of False Positive is high__.

Using the metrics we just described, we selected the __Gradient Boosting__ and __Random Forest__ classifiers as our best models
