# Devblog part 1 - August 11, 2025

This is the first iteration of the dev blog for the Agartha model.

Right now I am working on putting together all of the data that I want to use to train the model. The main steps at this point are:

1. downloading data
2. conforming the data to a basic structure

Because the data is different sizes it all needs to be smoothed out to be the same size, for example the bathymetric data is 15 arc seconds but the vp/vs data is 1 degree. This can be solved with mean pooling so I am not super worried, better to get all the data into a single place.

I also need to find more data sets because this isn't enough. I would like to also include

1. gravity
2. magnetic
3. heat flow

And maybe some other data sets.

My goal is to have these data all put together and then calculate the positional encodings.

I also want to write a generic loader so that I can add more data easily to the data sets.

## TODO

1. Next I need to take the data that I have already downloaded and start constructing the positional vectors for the modeling. To get started it should look something like:

| lat | lon | depth | values.... |

That should get me started and then I can build stuff from there.

The overall goal here is that I have essentially a two stage modeling process. The first stage is creating a lower resolution but more globally complete model from all of these different models. The second stage will be to create a fine tuned version of the model that uses the LILY database for IODP boreholes.