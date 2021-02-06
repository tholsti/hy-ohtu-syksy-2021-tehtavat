# A new user account can be created if a proper unused username and a proper password are given

*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create Mock User

*** Test Cases ***
Register With Valid Username And Password
    Input New Command And Create User  ville  strong_password!23
    Output Should Contain  New user registered
    

Register With Already Taken Username And Valid Password
    Input New Command And Create User  kalle  strong_password!23
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Input New Command And Create User  vi  strong_password!23
    Output Should Contain  Username is invalid

Register With Valid Username And Too Short Password
    Input New Command And Create User  ville  short!
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command And Create User  ville  longpassword
    Output Should Contain  Password contains only letters

*** Keywords ***
Input New Command And Create Mock User
    Input New Command
    Create User  kalle  kalle123

Input New Command And Create User
    [Arguments]  ${username}  ${password}
    Input New Command
    Create User  ${username}  ${password}

Create User
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application
