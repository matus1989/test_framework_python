# **Test Framework Python**
This README file provides instructions on how to set up, run, and understand the testing framework built using Python, Selenium, Testcontainers, pytest, and pytest-bdd for the example website [Parabank](https://parabank.parasoft.com/parabank/index.htm).

## **Tabel of Contents**
1. [Prerequisites](#item-one)
2. [Installation](#item-two)
3. [How to run](#item-three)


<a id="item-one"></a>
### **1. Prerequisites**

Ensure you have the following installed on you system:
- Python 3.12 or higer
- Docker

<a id="item-two"></a>
### **2. Installation**

1. Clone repository
```sh
git clone https://github.com/matus1989/test_framework_python.git
cd test_framework_python
```
2. Create a virtual environemt and activate it:
```sh
python -m venv venv
source ven/bin/activate
```
3. Install the required packages
```sh
pip install -r requirements.txt
```

<a id="item-three"></a>
### **3. How to run**
To run the tests, use following command

```sh
pytest -s
```
<br>Test will run in default *FireFox latest* test container 
<br>If you wanna runn test with **Chrome latest** test container please use ***--browser*** parammetr
```sh
pytest --browser=[firefox/chrome] -s
```  
