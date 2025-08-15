# devblog-part4 august 15, 2015

I realized that I should be using spherical harmonics to do the
positional encodings because sinusoidal encodings are not going to be
very useful at the poles. I found this paper
[@russwurm2024locationencoding] which describes [this
repo](https://github.com/MarcCoru/locationencoder) which seems like a
good place to start.

# References {#bibliography .unnumbered}
