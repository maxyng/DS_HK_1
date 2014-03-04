http://www.jds-online.com/file_download/398/JDS-1154.pdf

Objective/Abstract: What is the paper about, and what was the goal of the paper? Hypothesis: Where any hypotheses made within the paper before the work began? If so, what was it? What did you think about it?
===============================================================================================================================================================================================================

The paper presents the idea of measuring the Weight to Height (WOH) ratio of a child before the age of two can predict if the child will be obese at age 5.  The rate of obesity in the US is growing and studies have found obesity to be the root of many physical and mental complications.  The aim is to detect signs of obesity early on in a child's development and use preventative measures to help obesity instead of treating later.  Previously, the BMI (weight / height^2) was the way of judging if a person is obese or not and is used to judge if a person is in a healthy body weight.

Style: Who was the audience of the paper, and how could that get figured out? (Some data science papers are not written for other data scientists, but more targeted towards the applied section of the paper, ie Sociologists, etc).
===============================================================================================================================================================================================================

The audience of this paper if for members of health community.  Clinician, pediatrician or family physician who can regularly monitor and recommend/treat a child's health choices are the target of people who can benefit from this knowledge.  This is shown by need to carefully a child's health and well being.

Methods: What methodologies did the paper use to approach its objective? How well did they work?
================================================================================================

Data was measured by one region in the United States and from what is considered 'well-being' children.  Inclusive and Excusive criteria were listed which gave a 'healthy' data trying to phase out any abnormalities.  Obesity is judged by the BMI score and is needed to be compared with the WOH data.  The method of deciding if the child will be obese is by longitudinal decision analysis.  

The Longitudinal Decision Analysis (LDA) is stated as used in type control analysis for a trendline.  Groups of normal and obese were separated for comparison.  When plotting the LDA with the BMI and WOH data compared to the days since birth (dsb), the WOH shows a grouped linear trend for obese individuals while BMI plots also shows the linear relation but the deviation is larger.  A linear regression model for the obese group was found with the function of a exponential variable  exp(-dsb/454).   The normal group had a linear regression relationship of 0.929 - 0.494 exp(-dsb/454).

The R^2 came to a 85.8% variation and the standard error of estimate was 61 members.   It gathered a 95% confidence interval profile on the WOH versus dsb.
The positive predicted value (PPV) was slightly with 97% and 100% negative predicted value (NPV) with an upper decision limit of 3 and was slightly off with 95% and 97% when the upper decision limit was 2.   These values are very off compared with the BMI results of PPV 49% and NPV 83% in an upper warning limits and PPV 58% and NPV 77% when the lower warning limit.

Conclusions: Overall assessment of the paper. This is generally broken into parts of what you thought about the material you read, do you think it was well written or poorly written, how well did it answer the questions it was looking at, and did you have any follow up questions about the data, methodologies, etc.
===============================================================================================================================================================================================================

This method can be a step of using preventative measure to prevent obesity in children.  Although the steps to prevent obesity in children could be followed despite knowing if the child will become obese or not, it will help warn a parent through telling that the trend their child is falling in terms of weight is heading toward obesity and preventative measures should be taken instead of treatment after.  The paper goes into detail on the WOH being compared to the body volume index where the human body is considered cylindrical by taking the average radius of the head, shoulders, chest and abdomen.  This allows a density comparison than a simple height that can be considered inaccurate in knowing if a person is considered healthy.