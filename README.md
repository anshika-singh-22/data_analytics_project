Data Analytics Fundamentals Project
This repository serves as a portfolio project, demonstrating foundational skills in the data science pipeline: from data acquisition to cleaning, analysis, and insights generation.🛠️ Skills and TechnologiesThis project utilizes key Python libraries to execute core data analytics tasks:CategoryTaskLibraries UsedData AcquisitionWeb Scraping (Task 1)requests, BeautifulSoupData WranglingExploratory Data Analysis (EDA) (Task 2)pandas, numpyInsight GenerationSentiment Analysis (Task 4)nltk (VADER Lexicon)🚀 Getting StartedFollow these steps to get the project running on your local machine.PrerequisitesYou need Python 3.x installed.InstallationClone the repository:Bashgit clone [Your Repository URL]
cd [repo-name]
Install the required libraries:Bashpip install pandas numpy requests beautifulsoup4 nltk
Download the NLTK VADER lexicon (required for Sentiment Analysis):Open a Python interpreter (type python in your terminal) and run:Pythonimport nltk
nltk.download('vader_lexicon')
exit()
📋 Project 
Task 1: 
Web ScrapingFile: task_1_web_scraping.py (or task_1.py)
Description: Extracts data from a public source ([e.g., http://quotes.toscrape.com/]) to simulate collecting relevant datasets. Uses headers to avoid detection and handles HTTP errors.
Task 2: 
Exploratory Data Analysis (EDA)
File: task_2_eda.py
Description: Loads a sample dataset, assesses its structure (df.info()), calculates descriptive statistics (df.describe()), and identifies missing values and data distributions to inform further analysis.
Task 4: 
Sentiment AnalysisFile: task_4_sentiment_analysis.py
Description: Applies Natural Language Processing (NLP) techniques using the NLTK VADER lexicon to analyze text (e.g., simulated public opinion/reviews) and classify it as positive, negative, or neutral.
