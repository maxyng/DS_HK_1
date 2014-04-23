Description of problem and hypothesis.
---
The problem to tackle for my final project is from an ongoing kaggle competition. The official description is:

> The Rotten Tomatoes movie review dataset is a corpus of movie reviews used for sentiment analysis, originally collected by Pang and Lee [1]. In their work on sentiment treebanks, Socher et al. [2] used Amazon's Mechanical Turk to create fine-grained labels for all parsed phrases in the corpus. This competition presents a chance to benchmark your sentiment-analysis ideas on the Rotten Tomatoes dataset. You are asked to label phrases on a scale of five values: negative, somewhat negative, neutral, somewhat positive, positive. Obstacles like sentence negation, sarcasm, terseness, language ambiguity, and many others make this task very challenging."

In my words, the problem is to be able to judge if the review written is giving a positive or negative opinion on the film based on any key words that would determine if the reviewer thinks highly of the film or not.
What I feel is, there will be words that greatly determine if the opinion given on the film is positive or negative and sarcastic adjectives will not sway the analysis greatly.

Detailed description your data set.
---
The data provided by Kaggle does not have many features.  There are only four features:

* PhraseId 
* SentenceId
* Phrase
* Sentiment

The unique identifier is "PhraseId" to distinguish the different rows.  This way it's being distinguished is by a numerical sequential number that increments by 1.  This is a standard for identifying each sentence uniquely.

The SentenceId is what makes this dataset special.  It is what groups the different rows together so the data scientist knows they belong to each other.  There is a main sentence that is broken up into phrases which appears to be randomly broken up.  One very unique thing about the phrases is that when the "'s" is written, there is a space between the word and "'s" causing string tokenizers to misinterpret "'s" as a single word.  There were over thirteen thousand instances of "'s" singilarily appearing.  Commas and other punctuation symbols also appear in the dataset.

The sentiment is the score the reviewer put along with the descriptive sentence describing their feeling of the film.  The mapping is as follows

* negative: 0
* somewhat negative: 1
* neutral: 2
* somewhat positive: 3
* positive: 4

There are 156060 rows for training data and 222352 rows for test data.

How did you decide what features to use in your analysis?
---
Since I only have 4 features, there isn't any drastic reduction of features in my dataset.  The PhraseId was removed because it provides no value to the data in this application.

What challenges did you face in terms of obtaining and organizing the data?
---
The biggest challenge faced with this data was being able to familiarize myself with the python tools to accomplish the data changes I wanted. The removal of unneeded features such as the SentenceId, PhraseId and separate Sentiment were not too difficult. Accomplishing the parsing of the words in each phrase was the most challenging part. Understanding what the libraries outputted into what datatype was challenging as each datatype class has their own functions that needed a deeper understanding to better manage the data.

Further additions would be to take out stop words in the parsed out phrases as they are not needed and could overfit my results.

Describe what kinds of statistical methods you used, and perhaps others you considered but did not use, and how you decided what to use.
---
My data set had me conclude that the best model was the Naive Bayes model to solve my sentiment analysis problem.   Through the libraries provided in python, I had the ability to use different types of Naive Bayes formulas and compare the results.   The attempts I made were as follows.

### Attempt A
`naive_bayes.MultinomialNB` on the whole phrase.  No parsing of the individual words into the model.

### Attempt B
`Gaussian Model` didn't work well and caused the machine to crash my python program.  It was found out later that this model cannot handle sparse data very well so it was unfit for my type of data.  This was an attempt to better understand these programs and try new things so I was not discouraged by this finding.

### Attempt C
`naive_bayes.BernoulliNB` on the whole phrase.  No parsing of the individual words into the model.

### Attempt D
`nltk.classify.NaiveBayesClassifier` is a python library made for natural language procesing. Using this library to generate results for comparison, it was able to come up with a list of features that generated the most significant scores in my training data set as attached in screenshot "impl_verD_result.png".  The result in taking the model and testing with the test data provided gave an accuracy of `0.3944`.  

### Attempt E
`DecisionTreeClassifier` was an attempt to use a whole different model to test textual content without resorting to strictly naive bayes. However, I was unsuccessful in making a worthwhile model giving results in my attempt.

### Attempt classification comparison
A text classifier library was introduced to me as a method of comparing the scores and times needed to run for different popular classifier models provided in python. The original program used textual data from a newsgroup and I was able to change the inputs to the data I have from rotten tomatoes. Other than comparing the test scores by each popular classifier model, it also recorded the time taken to generate the result. This data could benefit future comparisons in knowing what model gives the best result and which one gives the fastest. Trying to successfully change the program to give test scores didn't fare well as I encountered a memory error. I have results of training the models and running my test data with success. The setback was that I couldn't give a test score because there is no result to compare with.

What business applications do your findings have?
---
Natural learning classifier models have significant business applications in the future. In this sample data for example, it is able to judge the sentiment of a person through key words to determine if the score given is in favour or not of the movie.  This can help shift through customer opinions in many opinion sites and other textual intensive applications such as law, medical and editorial as a small set of examples.

Merging the natural learning classifiers with other significant data can be mapped with other models to gather more accurate results. One example I have, using the rotten tomatoes dataset is to also record the history of reviews by the reviewer and possible demographics as well.  This can better capture the person and give a more significant weight on a person's review to a user. An example for this is, a movie could be marketed to a particular demographic such as teenagers. A senior citizen's review will likely be more negative because the movie was not marketed toward that market. A user may only see the senior citizen's negative review, not knowing the demographic of the person giving the review and proceed to not watch the movie despite the person reviewing wasn't the target market. This application can be brought to target markets and better suited campaigns to customers.

Textual analysis has developed some new techniques in the last 10 years but it has far from peaked. Google uses models to predict the search a user wants to look for given the popularity of the search being made previously and spam filters utilize this to better filter unsolicited e-mails from a person's e-mail mailbox. A lot of data is in text form and there is more more than can be explored using computers that can process large quantities of data and greater speeds than humans can. We just need to teach them what we want from them.
