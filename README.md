### Introduction

We used add-alpha smoothing to estimate the probabilities in this assignment. We chose this method over add-1 smoothing because it more accurately distributes the trigram probabilities and therefore is more likely to generate accurate sequences. Furthermore, if the training data contains no instances of some trigrams, add-alpha smoothing will give them some small probability rather than 0 and therefore avoids the problem of overfitting to the training data. Since our vocabulary size is relatively small (30 characters), we also decided it was not necessary to use Kneser-ney smoothing, which is better for larger models. Finally, calculating the trigram probabilities is also faster and simpler with add-alpha smoothing compared to other methods such as Knesey-ney and Interpolation which involve more complex computations.  
Part of the reason that add-alpha is a relatively straight-foward method is that it makes the simplifying assumption that the probability of a given character is only dependent on a fixed number of previous characters - the Markov assumption. Consequently, in our trigram model where n = 3, we only look two characters into the past. 

We also made the simplifying assumption to exclude the probabilities of certain trigrams. This included sequences such as ‘#a#’ since we consider a line with only a single character an illegal sequence which should not be given any probability. Similarly, we excluded trigrams such as ‘a#a’ since a single ‘#’ marks the end of a line and no character should follow it, and the sequence ‘###’ which would be an empty line.  
The add-alpha equation used in this assignment is presented below:

P+ (xi | xi-2 ,xi-1) = C(xi-2 , xi-1 , xi) + C(xi-2 , xi-1) + v

In this equation we represent the probability of a particular random character Xi as P(xi). The n-gram probability of  xi given two previous characters xi-2xi-1 is calculated as the relative frequency of xi-2 , xi-1 , xi to xi-2,xi-1.  For add-alpha smoothing, we increase all the possible trigram counts by . More specifically, we sum all counts of the trigram sequence xi-2, xi-1,  xi plus  , and then divide by the sum of all counts of the sequence xi-2 , xi-1 x plus  v where v = set of all x.

We choose the value of alpha that minimises the perplexity of a development set under our model. We created the development set by using the first 5200 words of the file ep-00-02-03.en from the *Sample European Parliament Proceedings Parallel Corpus* from the NLTK Corpora. At roughly 5,200 words, it was around a 1/5 of the size of the training data and used standard American English. We ran tests on values of alpha between 0.001-1. (0.001 increments) and found that when alpha = 0.308 it returned the minimum perplexity on the development set.

### Research Question

Our research question - during preprocessing of the training data, will removing the diacritic rather than the entire character affect the perplexity (PP) of the test data under the model?

When we preprocessed the training data, we removed all characters with diacritics. For this test, we will replace the diacritic characters with their corresponding non-diacritic counterparts. We predict that this operation will make the Spanish-trained model and the German-trained model output a higher PP value for the test data (which is in English) compared to the result we represented in question 5. This is because, by leaving in the characters, albeit unaccented, it is a more faithful representation of the training language. A higher PP value implies that the test data is less likely to be written in the language that the model was trained on, thus improving the accuracy of the new model compared to the old model.

Our control values will be the perplexity results from the old model and our method is the same as the previous steps in the assignment, aside from the difference in pre-processing.



As the perplexity values show, after we use our new preprocessing method, both of the new language models have a slightly higher perplexity value when assessed on the English test document. The difference value for the German-trained model is noticeably larger compared to the Spanish-trained model. This is likely because we replaced a single umlaut with a two vowel sequence; ‘ae’ in particular is very rare in English text, as is ‘oe’ to a lesser extent (the word “does” is fairly common). Overall, this test suggests a slight improvement in the ability of the models to identify the language of the test document and in turn highlights the benefit of replacing rather than removing accented characters during training. Of course only 1 test is not statistically significant so no definitive conclusions can be drawn yet. Further research might also explore whether this replacement method would cause a Spanish-trained model to perform better when tested on a document written in German, and vice versa.
