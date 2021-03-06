# [Judgemental Mom](https://judgementalmom.com)
### [Boston University Department of Computer Science](http://www.bu.edu/cs/)
#### [CS411 A2 Software Engineering](http://sites.bu.edu/perryd/cs411-software-engineering/) Fall 2016
##### Created by nlouie on 10/6/16
##### Last updated by nlouie on 12/01/16
##### https://judgementalmom.com

### Group 8 Team Members
- [Nick Louie](mailto:nlouie@bu.edu)
- [Corey Clemente](mailto:coreycle@bu.edu)
- [Derek Mei](mailto:dmei3010@bu.edu)
- [Cameron Williams](mailto:camwill@bu.edu)

### About
Judgemental Mom is a social media analyzer where a user can connect his/her social media account(s), and get back a JM Report. 
Our first trick is to analyze a user's Facebook data and suggest playlists to match their judged mood.


## Development

### Development environments
- Python 3.5
- PyCharm Professional Edition

## Dependencies

### Backend
- [Python 3.5](https://www.python.org/downloads/release/python-350/)
- [Flask](http://flask.pocoo.org)
- [Authomatic](http://peterhudec.github.io/authomatic/index.html)

### Database (with sqllite3)
- [Dataset](https://dataset.readthedocs.io/en/latest/)

### Front End
- [Bootstrap](http://getbootstrap.com/)

### External APIs
- [Indico](https://indico.io)

## Setting up the Package

First, clone or fork our repository 

```git clone https://github.com/nlouie/judgemental-mom.git```

Create a new virtual environment for the Flask project. (optional) 

I suggest using PyCharm and when setting the interpreter, create a new virtual environment

### Installing Dependencies

```pip install -r requirements.txt```

*OR*


```$ pip install flask```
```$ pip install indicoio```
```$ pip install authomatic```
```$ pip install datasets```

### Set up your database

We use a sqlite3 database, located in the `data` directory.

## Running the Package

###  Start the server 

```$ python app.py ```

### Load web page

``` http://localhost:5000 ```


## Resources

### APIs
- [Facebook API](https://developers.facebook.com/)
    - [Graph API](https://developers.facebook.com/docs/graph-api/)
    - [API Explorer - Super useful!](https://developers.facebook.com/tools/explorer/)
- [Spotify API](https://developer.spotify.com/)
    - [Spotify Web API](https://developer.spotify.com/web-api/console/)
- [Indico Docs](https://indico.io/docs)

### Flask
- [Flask Docs](http://flask.pocoo.org/docs/)
- [Jinja Templates](http://jinja.pocoo.org/docs/dev/templates/)
- [Authomatic Flask](http://peterhudec.github.io/authomatic/examples/flask-simple.html)
- [WTF Forms](http://flask.pocoo.org/docs/0.11/patterns/wtforms/)
- [Sessions](http://code.runnable.com/Uhf58hcCo9RSAACs/using-sessions-in-flask-for-python)

### Dataset
- [Dataset docs](https://dataset.readthedocs.io/en/latest/)

### Jetbrains
- [Pycharm](https://www.jetbrains.com/pycharm/)
- [Jetbrains education](https://www.jetbrains.com/student/)

### Security
- [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)


### Required functionality

- [x] Setup database with dataset (sqllite3)
- [ ] Login / logout functionality (research packages for Flask)
- [x] Connect social Media
- [x] Gather facebook data with `collect_facebook_.py`
- [x] Analyze and display facebook data with `analyze.py` and `analyze.html` using Indico
- [ ] Make the UI look pretty

### Optional functionality
- [x] Login with Facebook
- [ ] Connect your Spotify

### Future Enhancements
- [Angular](https://angularjs.org/) (not implemented yet)
- [Sass](http://sass-lang.com/libsass) (not implemented yet)