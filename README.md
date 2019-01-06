# arxiv_techminer
Topic modelling for aritcles in arXiv.org

## Tools
* arxiv.py handles the xml file from arxiv.org and convert it to txt to prepare for hlta

  (See https://github.com/kmpoon/hlta for more detail)

* vanilla_lda wrap lda by Scikit_Learn to use txt file we get from arxiv.py to do the vanilla favor LDA


## Notes
* Use vanilla favor LDA as baseline for topic modelling.
* The result from hlta with default conf works pretty good.

* However, how to define the abstraction level of "Technology" is ambiguous.
* Status quo of R&D should be monitoring.


## TODO
* Patent data contains only short description?
* How different variants of LDA perform?
* Can Sentiment analysis perform good on advanced tasks such as "maturity measuring"? (Probably no.)
* How to measure maturity? (e.g. plot Technolgy in Gartner's Hype cycle based on 'Visibility', how to justify...)
* As an unsupervised learning task, how to evaluate the performance (likelihood, etc.) However, plausibility is questionable
