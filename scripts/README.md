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
 - gdtools 0.2.2     
 - ggpattern 0.1.3   
 - rcompanion 2.3.26
 - rstatix 0.6.0     
 - arm 1.11-2       
 - MASS 7.3-51.5    
 - sjPlot 2.8.6      
 - ggpubr 0.4.0      
 - ggrepel 0.8.2     
 - forcats 0.5.0    
 - stringr 1.4.0     
 - dplyr 1.0.2       
 - purrr 0.3.4       
 - readr 1.4.0       
 - tidyr 1.1.2      
 - tibble 3.0.4     
 - ggplot2 3.3.2     
 - tidyverse 1.3.0   
 - lme 1.0-4        
 - lme4 1.1-26      
 - Matrix 1.2-18

The R Software and R Studio can be downloaded here: https://rstudio.com/products/rstudio/download/

Please use the **install.packages("<package_name>")** function to install the packages before running the code. To create the HTML output, use the **Knit** button.

The detailed notes on each code chunk are in the *Rmarkdown* file.

### 2. Kibrik and Kodzasov 1990

This part of the appendix consists of one file:

- *Kibrik&Kodzasov_1990.tsv* — Digitized version of Kibrik and Kodzasov 1990.


Kibrik and Kodzasov 1990 markup can be opened in **Excel** or similar software.
