# devblog-part 3 August 14, 2025

I realized that if i do mean pooling on the gebco bathymetry data im
leaving a ton of information on the table. Thus I decided that I should
make a basic autoencoder to create embeddings to describe every 1x1
degree section instead of simply doing mean pooling. This will increase
the width of the training data per section. But it will also give a good
milestone for the project since the embeddings can be released by
themselves.
