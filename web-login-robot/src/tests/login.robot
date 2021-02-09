*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Log In With Username And Password  kalle  kalle123
    Login Should Succeed

Login With Incorrect Password
    Log In With Username And Password  kalle  kalle456
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Set Username  ville
    Set Password  password
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
