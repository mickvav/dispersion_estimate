# Simple dispersion estimationo experiment

Context:
Article
Bundgaard et al. 2020. Effectiveness of adding a mask recommendation to other public health measures to prevent SARS-CoV-2 infection in Danish mask wearers: a randomized controlled trial. Annals of Internal Medicine.
https://www.acpjournals.org/doi/10.7326/M20-6817


Citing:
"""
A total of 3030 participants were randomly assigned to the recommendation to wear masks, and 2994 were assigned to control; 4862 completed the study. Infection with SARS-CoV-2 occurred in 42 participants recommended masks (1.8%) and 53 control participants (2.1%). The between-group difference was −0.3 percentage point (95% CI, −1.2 to 0.4 percentage point; P = 0.38) (odds ratio, 0.82 [CI, 0.54 to 1.23]; P = 0.33). Multiple imputation accounting for loss to follow-up yielded similar results. Although the difference observed was not statistically significant, the 95% CIs are compatible with a 46% reduction to a 23% increase in infection.
"""

The question is: what is the probability, that this 0.3% of difference between the values is caused by random effects?

How to answer this question? Let's do some numeric expperiments.

Setup:

0-Hypothesis: probability of being infected is 0.5*(1.8+2.1)=1.95% and it does not depend on wear/not wearing masks.
Question: if we take 3030 tosses of the coin (with 1.95% chance of success) and count number of successes (n1), 
afterwards we take another 2994 tosses of the same coin, (n2), n1 - n2 will have some distribution, that we can 
describe if the entire procedure is repeated many times. This will give probability that under 0-hypothesis n2 - n1 >= (53-42).

1-Hypothesis: probability of being infected with mask is 1.8% and without - 2.1%. Doing the same test, as for 0-hypothesis.
Thus we will get probability that under 1-hypothsis n2 - n1 >= (53-42).

Each numerical experiment was repeated 10000 times (see python code attached)

Results:

python3 testrand.py
0-hypothesis P_(n2-n1 >= 11): 0.1509
1-hypothesis P_(n2-n1 >= 11): 0.4268
python3 testrand.py
0-hypothesis P_(n2-n1 >= 11): 0.1492
1-hypothesis P_(n2-n1 >= 11): 0.4243
python3 testrand.py
0-hypothesis P_(n2-n1 >= 11): 0.1512
1-hypothesis P_(n2-n1 >= 11): 0.4308

Conclusion:

Probability that the observed results are caused by random reasons under 0-hypothesis is ~15%. Under 1-hypothesis - 42%.
