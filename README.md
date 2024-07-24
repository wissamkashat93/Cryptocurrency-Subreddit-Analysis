Here's the updated README file for your project:

---

# Cryptocurrency Subreddit Analysis

This project aims to analyze text data from various cryptocurrency-related subreddits. The analysis includes exploratory data analysis (EDA), word frequency analysis, sentiment analysis, and topic modeling using various machine learning models.

## Table of Contents

- [Data Cleaning and Preparation](#data-cleaning-and-preparation)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Word Frequency Analysis](#word-frequency-analysis)
- [Sentiment Analysis](#sentiment-analysis)
- [Topic Modeling](#topic-modeling)
- [Hyperparameter Tuning](#hyperparameter-tuning)
- [Model Evaluation and Comparison](#model-evaluation-and-comparison)
- [Results](#results)
- [Conclusion](#conclusion)

## Data Cleaning and Preparation

- Checked each subreddit DataFrame for missing values.
- Removed rows with empty 'body' values.
- Dropped the 'approved_date' column.
- Verified no duplicate rows existed.
- Filtered out extreme values in 'ups' and 'score' columns.

## Exploratory Data Analysis (EDA)

- **Score Distribution**: Histograms were created to visualize the distribution of scores for different subreddits.
- **Upvotes Distribution**: Histograms were created to visualize the distribution of upvotes for different subreddits.
- **Average Word Length**: Analyzed the average word length for posts in each subreddit.

## Word Frequency Analysis

- Tokenized text data and removed custom stop words.
- Calculated and printed the top 10 most common words in each subreddit.

## Sentiment Analysis

- Used the VADER sentiment analyzer to calculate sentiment scores for each post.
- Summarized the sentiment scores into positive, neutral, and negative percentages for each subreddit.

## Topic Modeling

- Converted cleaned text data into numerical vectors using TF-IDF and Count Vectorizer.
- Applied NMF, LSA, and LDA models to discover latent topics within the discussions.
- Displayed the top words for each topic identified by the models.

## Hyperparameter Tuning

- Evaluated different hyperparameters for the NMF, LSA, and LDA models to find the best coherence scores.

## Model Evaluation and Comparison

- Calculated coherence scores to evaluate the quality of the topics produced by each model.
- Visualized and compared the coherence scores of the NMF, LSA, and LDA models.

## Results

- The LSA model demonstrated the highest coherence score, indicating the most coherent and meaningful topics.
- Insights into the interests and sentiments of the cryptocurrency community were gained.

## Conclusion

This project successfully analyzed text data from cryptocurrency-related subreddits, uncovering significant topics and sentiments. The results can help in understanding community interests and guiding further research or business decisions in the cryptocurrency domain.

---

Feel free to modify and expand this README file according to your project's specific needs and additional details you may want to include.
