# devblog-part4 august 15, 2015

I realized that I should be using spherical harmonics to do the
positional encodings because sinusoidal encodings are not going to be
very useful at the poles. I found this paper (Rußwurm et al. 2024) which
describes [this repo](https://github.com/MarcCoru/locationencoder) which
seems like a good place to start.

So anyways, I implemented this in the `gebco-ae.ipynb` notebook. Next I will implement this in the `data_preprocessing.py` file where there is the `GebcoDataset(torch.utils.data.Dataset)` class. Then I will start trying to build an autoencoder that can create an embedding vector for the bathymetry of every 1 by 1 degree square.

Also, it occurs to me that this embedding bathymetry stuff might be a nice ICLR paper given they accept all sorts of stuff like that. The deadline is:

* Abstract submission: 11:59pm, Sep 19
* Submission date: 11:59pm, Sep 24

[link is here for the conference](https://iclr.cc/Conferences/2026/CallForPapers)

Maybe that is an option for this. Not a lot of time but its 9 pages so maybe worth submitting. Anyways maybe it will go easier since this devblog seems to have a good momentum. Only will matter if i can train a model that works lol.

I also added a github action that generates the references if I have
them. All references go into the refs.bib file so everything is ready
when I happen to write a paper or something. But anyways, thats cool.
:-)

# References

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-russwurm2024locationencoding" class="csl-entry">

Rußwurm, Marc, Konstantin Klemmer, Esther Rolf, Robin Zbinden, and Devis
Tuia. 2024. “Geographic Location Encoding with Spherical Harmonics and
Sinusoidal Representation Networks.” In *Proceedings of the
International Conference on Learning Representations (ICLR)*.
<https://iclr.cc/virtual/2024/poster/18690>.

</div>

</div>
