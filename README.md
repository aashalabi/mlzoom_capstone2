---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.6
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Zoomcamp ML project


## Website phishing and scam prediction


![website_phishing.png](attachment:website_phishing.png)


## 1. Description of the problem
```
Website phishing is a form of cyberattack where malicious actors create a fraudulent website that mimics a legitimate one. The goal is to deceive users into revealing sensitive information, such as:
Login credentials,Credit card details, Personal identification data (e.g., Social Security numbers), Account details for financial systems

These fake websites often closely resemble the appearance and URL of a trusted site, making it difficult for users to distinguish between the legitimate and malicious versions.

Techniques Used in Website Phishing
Spoofed URLs: Cybercriminals use URLs similar to legitimate websites (e.g., using "g00gle.com" instead of "google.com").
Email Phishing: Victims are lured through emails containing links to the phishing site.
Clone Websites: Replicas of legitimate websites with subtle differences.
SSL Certificates: Phishing sites might also use HTTPS to appear more authentic.
Pop-up Forms:Fake login or payment forms embedded in legitimate-looking sites.

How Website Phishing Affects Online Trading
Online trading platforms, such as stock brokerages, cryptocurrency exchanges, and e-commerce websites, are frequent targets of phishing attacks. The impact includes:
1. Loss of Sensitive Information
2. Theft of Funds
3. Compromised Reputation
4. Fraudulent Trades and Market Manipulation
5. Identity Theft
6. Loss of Business Opportunities


The goal is to use set collected features to predict phishing websites and avoid/minize losses.
```


## 2. Create environment
```
conda create --name ml-zoomcamp python=3.11.10
conda activate ml-zoomcamp

pip install -q scipy
pip install pandas
pip install numpy
pip install seaborn
pip install scikit-learn
pip install waitress
pip install pipenv
```



## 3. Data

    Data is download from the URL [archive.ics.uci.ed](https://archive.ics.uci.edu/dataset/327/phishing+websites)



### 3.1 Data Features
```
All data fields are described in data\Phishing Websites Features.pdf
All features are encoded as follows:
| **Category**   | **Value** |
|----------------|-----------|
| Legitimate     | 1         |
| Suspicious     | 0         |
| Phishing       | -1        |

The results column is encoded as :
| **Category**   | **Value** |
|----------------|-----------|
| Legitimate     | 1         |
| Phishing       | -1        |

```


## 4. Notebooks and included files
```
    ml_project.ipynb :  contains <br>
                            - Data preparation and data cleaning
                            - EDA, feature importance analysis                        
                            - Model selection process and parameter tuning                        
    train.py: selected model traianing and saving to file
    predecit.py: simple load model and predict
    app.py: flask app
    test_service: test the flash app
    Docker file: to create docker image


## 5. Instructions on how to run the project
```
    1- create the env as in (2)
    2- activate the environment
       conda activate ml-zoomcamp
    3- Clone the repo
       https://github.com/aashalabi/ml-zoomcamp-project.git
    4- run flask backend service
        cd src
        waitress-serve --port=9696 app:app
    5- Run predict test, open new cmd window , activate the env
       conda activate ml-zoomcamp
       cd src
       python test_service.py
```


## 6. Build and run through Docker


```
    pipenv --python 3.11
    pipenv install -q scipy
    pipenv install pandas numpy
    pipenv install seaborn scikit-learn waitress 
    pipenv install flask
    
    cd src
    docker build --no-cache -t site_spam_predict:1.0 .
    docker run -d -p 9696:9696 --name site_spam_predict site_spam_predict:1.0
    python test_service.py
```


## 7. AWS cloud impelemntation


## 7.1 Architecure
![image-2.png](attachment:image-2.png)


## 7.2 Convert binary model to protocol V4

It was suggested to used p4 or p5 protocol when saving the model.<br>
Execute the following to conver the model to v4 protocol<br>
python p4_bin_convert.py


<!-- #region -->
## 7.3 Detailed AWS implementation and depoloyment


Check the content of [README_AWS.md](./README_AWS.md)


<!-- #endregion -->
