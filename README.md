<p align="center">
  <img src="https://i.imgur.com/156crxI.gif" />
  <h1 align="center">Project Billboard API</h1>
</p>

## Table of Contents
* [Introduction](#introduction)
* [Features](#features)
* [Technologies](#technologies)
* [Setup](#setup)
* [Team](#team)
* [Contributing](#contributing)
* [Others](#others)

### Introduction
Project Billboard API forms part of Project Billboard whose objective is to produce a model that is capable of predicting the potential of a song to be a billboard hit. This repository contains the work done for our frontend and API used to host our song prediction models online. For the repository that contains our work on model training, please refer to the project billboard model repository:
```
https://github.com/tjtanjin/project_billboard_model
```
Currently, the project is live on the following website:
```
http://project-billboard.herokuapp.com/
```

### Features
The API serves up a single endpoint for POST requests in making song predictions:
```
/api/v1/predict/{songname}
```
It identifies the song name to carry out prediction on base on the URL path and also accepts 1 of 3 models as POST data in the format below:
```
{"chosen_model": "model"}
```
The current list of available models are as below:
```
1) Logistic Regression
2) K Nearest Neighbours
3) XGBoost
```
### Technologies
Technologies used by Project Billboard API are as below:
##### Done with:

<p align="center">
  <img height="150" width="150" src="https://i.imgur.com/lXu9kox.png"/>
</p>
<p align="center">
HTML
</p>
<p align="center">
  <img height="150" width="150" src="https://i.imgur.com/SQKE9WW.png"/>
</p>
<p align="center">
CSS
</p>
<p align="center">
  <img height="150" width="150" src="https://i.imgur.com/1D3AoId.png"/>
</p>
<p align="center">
JavaScript
</p>
<p align="center">
  <img height="150" width="150" src="https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png"/>
</p>
<p align="center">
Python
</p>

##### Deployed on:
<p align="center">
  <img height="150" width="150" src="https://img.icons8.com/color/240/000000/heroku.png" />
</p>
<p align="center">
Heroku
</p>

##### Project Repository
```
https://github.com/tjtanjin/project_billboard_api
```

### Setup
The following section will guide you through setting up your own Project Billboard API!
* As this project is hosted on heroku, it would be easier to fork this repository instead of cloning it locally so as to facilitate easier automatic deploys later on in the guide. However, if you wish to clone this repository, go ahead and cd to where you wish to store the project and clone it as shown in the example below:
```
$ cd home/user/exampleuser/projects/
$ git clone https://github.com/tjtanjin/project_billboard_api.git
```
* Next, you will need to obtain a [spotify token](https://developer.spotify.com/documentation/general/guides/authorization-guide/) and create a new application on [heroku](https://dashboard.heroku.com/).
* Within the heroku dashboard, configure either heroku git or github for automatic deploys (hence my suggestion to fork instead of cloning the repository).
* Once you are able to deploy your application, go under settings and create a new config var with the name spotify_token. The value of it would be the spotify token you obtained in step 2.

### Team
* [Tan Jin](https://github.com/tjtanjin)
* [Arthur Chionh](https://github.com/artc95/)
* [Toh Yue Feng](https://github.com/m3thx6)

### Contributing
If you have code to contribute to the project, open a pull request and describe clearly the changes and what they are intended to do (enhancement, bug fixes etc). Alternatively, you may simply raise bugs or suggestions by opening an issue.

### Others
For any questions regarding the implementation of the project, please drop an email to: cjtanjin@gmail.com.
