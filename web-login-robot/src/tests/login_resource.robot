***Settings***
Resource  resource.robot

***Keywords***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Login

Log In With Username And Password
    [Arguments]  ${username}  ${password}
    Set Username  ${username}
    Set Password  ${password}
    Submit Credentials

Create User And Go To Login Page
    [Arguments]  ${username}=kalle  ${password}=kalle123
    Create User  ${username}  ${password}
    Go To Login Page
    Login Page Should Be Open
