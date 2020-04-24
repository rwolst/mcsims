# MC Sims
Repo contains the latex files for generating the note on how many Monte Carlo
simulations are needed to estimate Bernoulli probabilities within some desired
confidence bounds.

The pdf is put under version control. Ideally I would have a Git hook so that
every time I commit it re-generates the pdf.

## Outline
The standard case is easy where we observe a number of independent Bernoulli
trials with some fixed probability. We also consider the over-dispersed case
where each trial a probability is sampled from a Beta distribution. This leads
to more interesting results.

The key idea is that for `N` (unknown) samples of the probability from the Beta
distribution we can run `n` Monte Carlo sims. We want to choose `N` and `n` in
an optimal way so that our final estimates are within some desired confidence
regions.

## Code
Included is code for testing that our confidence regions are indeed correct.

## Paper
See `latex/MCSims.pdf` for the (hopefully if I remembered to build) latest
version of the paper.
