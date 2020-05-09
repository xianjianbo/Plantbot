## search weather 
* greet
  - utter_greet
* ask_weather
  - utter_ask_location
* inform{"location":"北京"}
  - action_search_weather
* thanks
  - utter_you_are_welcome
* goodbye
  - utter_goodbye

## search weather happy path
* greet
  - utter_greet
* ask_weather{"location":"上海"}
  - action_search_weather
* thanks
  - utter_you_are_welcome
* goodbye
  - utter_goodbye

## search plant location
* greet
  - utter_greet
* ask_plant_location{"plant":"樱花"}
  - action_search_plant_location
* ask_weather
  - action_search_weather
  - slot{"location": 北京}

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
