# techminer
This project contains two parts, technology identification and maturity classification, in order to serve the business R&D process.


## Technology Identification
In this part, we use topic modelling to cluster technology articles.

### Tools
* arxiv.py handles the xml file from arxiv.org and convert it to txt to prepare for hlta
* vanilla_lda.py wrap lda by Scikit_Learn to use txt file we get from arxiv.py to do the vanilla favor LDA


### Notes
* However, how to define the abstraction level of "Technology" is ambiguous.
* Status quo of R&D should be monitoring.
* As an unsupervised learning task, how to evaluate the performance (likelihood, etc.) However, plausibility is questionable

### TODO
* Patent data contains only short description?
* How different variants of LDA perform?

## Technology Maturity Classification
In the second part, we see measure of maturity of technology as a classification process.

### Notes
* Use vanilla favor LDA as baseline for topic modelling.
* The result from hlta with default conf works pretty good.





## REF
[Measuring Technology Maturity: Operationalizing Information from Patents, Scientific Publications, and the Web](https://link.springer.com/content/pdf/10.1007%2F978-3-658-12132-7.pdf)
[HLTA on Github and related Paper](https://github.com/kmpoon/hlta)
