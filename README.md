### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

In order to run this project, install Python 3 or higher with the following Python libraries: sys, numpy, pandas, sklearn, sqlalchemy, Ipython, seaborn, and plotly.

## Project Motivation<a name="motivation"></a>

For this project, I was interestested in using audio features from Spotify Top 50 tracks to understand:

1. How do audio features impact the popularity of songs on Spotify?
2. Can a song's audio features indicate the likely popularity of the 
   song before it is released?

## File Descriptions<a name="files"></a>

The Spotify Download.ipynb file gathers the tracks from the desired playlists and their audio features.

The Undsertanding the Data.ipynb file compiles, cleans, and completes the intial analysis of data from the downloaded tracks.

The above mentioned ipynb files can be found in the data folder along with saved images and saved csv files from running the ipynb files.

Lastly, the regression_model.ipynb file contains the regression analysis of the compiled data frame and the output predictions from the model of popularity scores.

## Results<a name="results"></a>

The findings from my analysis can be found on a medium blog available [here](https://jadefreese98.medium.com/audio-features-and-track-popularity-4309b42f9aae).

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

I must give credit to Spotify for the data.  You can find information on the Spotify API [here](https://developer.spotify.com/documentation/web-api/).  Otherwise, the code found here is open for use however you would like.
