# [Judgemental Mom](https://judgementalmom.com)
### [Boston University Department of Computer Science](http://www.bu.edu/cs/)
#### [CS411 A2 Software Engineering](http://sites.bu.edu/perryd/cs411-software-engineering/)Fall 2016
##### Created by nlouie on 10/6/16
##### Last updated by nlouie on 11/5/16
##### https://judgementalmom.com

### Group 8 Team Members
- [Nick Louie](mailto:nlouie@bu.edu)
- [Corey Clemente](mailto:coreycle@bu.edu)
- [Derek Mei](mailto:dmei3010@bu.edu)
- [Cameron Williams](mailto:camwill@bu.edu)

### About
Judgemental Mom is a social media analyzer where a user can connect his/her social media account(s), and get back a JM Report. 
Our first trick is to analyze a user's Facebook data and suggest playlists to match their judged mood.

## Dependencies

### Backend
- [Python 3.5](https://www.python.org/downloads/release/python-350/)
- [Flask](http://flask.pocoo.org)
- [Authomatic](http://peterhudec.github.io/authomatic/index.html)

### Database (with sqllite3)
- [Dataset](https://dataset.readthedocs.io/en/latest/)

### Front End
- [Bootstrap](http://getbootstrap.com/)
- [Angular](https://angularjs.org/) (not implemented yet)
- [Sass](http://sass-lang.com/libsass) (not implemented yet)

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


## Running the Package

###  Start the server 

```$ python app.py ```

### Load web page

```http://localhost:5000```


## Development

### Development environments
- Python 3.5
- PyCharm Professional Edition

## Resources

### APIs
- [Facebook API](https://developers.facebook.com/)
- [Spotify API](https://developer.spotify.com/)
- [Indico Docs](https://indico.io/docs)

### Flask
- [Flask Docs](http://flask.pocoo.org/docs/)
- [Jinja Templates](http://jinja.pocoo.org/docs/dev/templates/)
- [Authomatic Flask](http://peterhudec.github.io/authomatic/examples/flask-simple.html)

### Dataset
- [Dataset docs](https://dataset.readthedocs.io/en/latest/)

### Jetbrains
- [Pycharm](https://www.jetbrains.com/pycharm/)
- [Jetbrains education](https://www.jetbrains.com/student/)


## Todo

### Required functionality

[ ] - Setup database with dataset (sqllite3)
[ ] - Login / logout functionality (research packages for Flask)
[ ] - Connect social Media with `connect.py` and `connect.html`
    [ ] Facebook
[ ] - Gather facebook data with `collect_facebook_.py`
[ ] - Analyze and display facebook data with `analyze.py` and `analyze.html` using Indico
[ ] - Make the UI look pretty

### Optional functionality
[ ] - Login with Facebook
[ ] - Connect your Spotify

