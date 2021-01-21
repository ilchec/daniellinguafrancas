# This is the code accompanying the CLDF dataset for Daniel et al.'s "Lingua Franca as Lexical Donors: Evidence from Daghestan" from 2021

Cite it as

> Daniel et al. (2021) Lingua Franca as Lexical Donors: Evidence from Daghestan. Language.

This dataset is licensed under a CC-BY-4.0 license

## Notes

The project consists of two parts:

1. the data and scripts used to create the plots in the paper
2. preliminary markup of the Kibrik & Kodzasov 1990 data and comparison of our counts to the counts in this source.

### 1. Data and Scripts

This part of the project consists of the following files:

- *tests_and_visualizations.Rmd* — the R code.
- *tests_and_visualizations.html* — an HTML page rendered on the basis of the .Rmd file.
- *words_data.tsv* — the wordlists.
- *meta_anonymized.tsv* — metadata for the wordlists.
- *concepts.tsv* - the list of DagLoans concepts.
- *Multilingualism_data.tsv* - multilingualism data.
- *bibliography.bib* - bibliography for the Rnotebooks

The file **tests_and_visualizations.Rmd** creates the HTML version of the R-Notebook. The files **wordlist_data.tsv**, **meta_anonymized.tsv**, and  **avar_cognates.tsv** have to be in the same directory as the **.Rmd** file. The program requires the following software and packages:

Software:

- R (version 3.6.3) and R Studio

*Note that the code will not run in R 4.0 due to the changed behaviour of some important functions as well as compatibility issues.*

R packages:

- tidyverse
- ggplot2
- ggrepel
- dplyr
- ggpubr
- DT
- scales
- data.table
- arm
- sjPlot

The R Software and R Studio can be downloaded here: https://rstudio.com/products/rstudio/download/

Please use the **install.packages("<package_name>")** function to install the packages before running the code. To create the HTML output, use the **Knit** button.

The detailed notes on each code chunk are in the *Rmarkdown* file.

### 2. Kibrik and Kodzasov 1990

This part of the appendix consists of one file:

- *Kibrik&Kodzasov_1990.tsv* — Digitized version of Kibrik and Kodzasov 1990.


Kibrik and Kodzasov 1990 markup can be opened in **Excel** or similar software.
