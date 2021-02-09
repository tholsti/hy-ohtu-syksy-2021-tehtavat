*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Registration Form

*** Test Cases ***
Register With Valid Username And Password
    Fill Out Registration Form  ville  ville_123!
    Submit Registration Form
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Fill Out Registration Form  vi  ville_123!
    Submit Registration Form
    Registration Should Fail With Message  Username is invalid

Register With Valid Username And Too Short Password
    Fill Out Registration Form  ville  v123!
    Submit Registration Form
    Registration Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Fill Out Registration Form  ville  v123!  ville_123!
    Submit Registration Form
    Registration Should Fail With Message  Password and confirmation do not match

Login After Successful Registration
    Create User And Go To Login Page  ville  ville123
    Log In With Username And Password  ville  ville123
    Main Page Should Be Open

Login After Failed Registration
    Create User And Go To Login Page  ville  abc
    Log In With Username And Password  ville  abc
    Login Page Should Be Open


*** Keywords ***
Fill Out Registration Form
    [Arguments]  ${username}  ${password}  ${password_confirmation}=${password}
    Set Username  ${username}
    Set Password  ${password}
    Set Password Confirmation  ${password_confirmation}

Submit Registration Form
    Click Button  Register

Registration Should Succeed
    Welcome Page Should Be Open

Reset Application And Go To Registration Form
    Reset Application
    Go To Registration Form

Registration Should Fail With Message
    [Arguments]  ${message}
    Registration Page Should Be Open
    Page Should Contain  ${message}
