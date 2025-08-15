# devblog-part4 august 15, 2015

I realized that I should be using spherical harmonics to do the
positional encodings because sinusoidal encodings are not going to be
very useful at the poles. I found this paper (Rußwurm et al. 2024) which
describes [this repo](https://github.com/MarcCoru/locationencoder) which
seems like a good place to start.

I also addeda github action that generates the references if I have
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
