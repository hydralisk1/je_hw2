```diff
@@ text in red @@
```

# QA_Automation Homework 2

## 0. Repeat everything I coded during the class. <done>

## 1. Materials: @@ <done> @@
    Review class presentation
    Read about XPATH:
[only xpath part] https://techno-girls.club/locators/
https://www.guru99.com/xpath-selenium.html



## 2. Practice with locators. 
Create locators + search strategy for these page elements of Amazon Sign in page:
Amazon logo
Email field
Continue button
Need help link
Forgot your password link
Other issues with Sign-In link
Create your Amazon account button
*Conditions of use link
*Privacy Notice link


For example: 
Email field, search by ID, “ap_email”


3. Create a test case for Help search using python & selenium script

Test Case: 
User can search for solutions of Cancelling an order on Amazon
1. Open Amazon Help page https://www.amazon.com/gp/help/customer/display.html 
2. Use “Search Help Library” field and search for Cancel order:

3. Emulate hitting keyboard ENTER btn with send_keys command
4. Verify that ‘Cancel Items or Orders’ text is present

4* [Not required!]. Create a Test Case using BDD (Behave features and steps):
Test Case: 
Logged out user sees Sign in page when clicking Orders

1. Open https://www.amazon.com
2. Click Orders
3. Verify Sign in page opened

* - Not Required

5* Codewars, solve this kata: https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a
