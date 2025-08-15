# devblog part 2 - August 12, 2025

I have implemented a pytorch Dataset container class for the gebco
bathymetry data.

## Notes and thoughts

I think the seiscrust data should be, for the time being, relegated to
the `fine tuning` group because it currently isn't really global. Like i
think the stage 1 of the modeling should be only from globally complete
data (even if it is lower resolution), and i guess it is fine for data
to be globally complete up to $\pm$ 80 degrees or something like that,
and then all the other data can be used in stage 2. All these modeling
opinions that I put here will likely change when I actually get to
modeling things.

I have created two files:

`dataexplorer.ipynb`

and

`data_preprocessing.py`

### `dataexplorer.ipynb`

`dataexplorer.ipynb` is a notebook that simply shows the data and
imports it and shows maybe the head of the data and also some kind of
visualization (probably a map). It isn't meant as a research tool, more
of a "make sure it works at the most basic level" kind of notebook. But,
it will be nice since you can run it start to finish and show the raw
data is working

### `data_preprocessing.py`

`data_preprocessing.py` imports the data and puts it into
`torch.utils.data.Dataset` inhereted class containers. These will make
it easier to put all of the data into one big data set that can then be
used for modeling. We can kind of think of it as a multi-stage approach:

raw data $\rightarrow$ preprocessing `Datasets` $\rightarrow$ combined
data $\rightarrow$ processing step

At the processing step is where we can start doing things like
calculating the sinusoidal positional embeddings, mean pooling high
resolution data to match lower resolution data, etc. But in the mean
time it is just getting it all in one place.

## Other thoughts

my imagination is that I may be prematurely converting everything to
`torch.utils.data.Dataset` containers but whatever. Probably it will be
easier if everything goes into an xarray. I think maybe it is better to
keep everything as xarray inside of it anyways. I dunno.

I think i need to only use index for `Dataset.__getitem__` because the
`DataLoader` class requires this so i can't get clever here and do
something different. Essentially the goal should be that every data set
that is being input into a `Dataset` container should return a `tensor`.

I also should be using the github large file storage because these data
sets are going ot be annoying to move around otherwise.
