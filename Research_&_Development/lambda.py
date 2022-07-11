#import pandas as pd
import os
#from dotenv import load_dotenv
import alpaca_trade_api as tradeapi


# you need to open an account at a brokerage to buy/sell shares
# here assumption is that account is open and we are trading on that account
# i m using my alpaca account to do a paper trade in my account

def submit_crypto_order(crypto, buy_or_sell, number_of_shares):

    #load_dotenv('my_api.env')

    ## HARD CODING FOR NOW..FOR AWS LAMBDA..JUST SO I CAN TEST
    ## HAS TO BE CHANGED TO DO A LOADENV

    alpaca_secret_key='QrWTvuqjdWDgx7Klqe5iWIR8K5iESy6DFugfV4Xy'
    alpaca_api_key='PKSYV8TUR5L9XAGR5AHC'

    # Set the variables for the Alpaca API and secret keys
    #alpaca_api_key = os.getenv('ALPACA_API_KEY')
    #alpaca_secret_key = os.getenv('ALPACA_SECRET_KEY')

    # Create the Alpaca tradeapi.REST object
    # YOUR CODE HERE
    api = tradeapi.REST(
        alpaca_api_key,
        alpaca_secret_key,
        #api_version='v2'
        'https://paper-api.alpaca.markets'
    )


    # Submit a market order to buy 1 share of Apple at market price

    order_result= api.submit_order(
        symbol=crypto,
        qty=number_of_shares,
        side=buy_or_sell,
        type='market',
        time_in_force='gtc'
    )
    my_order = api.get_order_by_client_order_id('5b064140-f675-4777-b522-bdf0f62b5a50')
   

    return my_order

### Functionality Helper Functions ###
def parse_int(n):
    """
    Securely converts a non-integer value to integer.
    """
    try:
        return int(n)
    except ValueError:
        return float("nan")

### Validate the inputs from the user
#def validate_data(age, investmentAmount, riskLevel, intent_request):
def validate_data(crypto, buy_or_sell, number_of_shares, intent_request):

    """
    Validates the data provided by the user.
    """

    # Validate that the user is 0-65 years old
    if crypto is not None:
        crypto = str(crypto).upper()
        #age = parse_int(age)
        if crypto != 'BITCOIN' and crypto != 'ETHEREUM':
            return build_validation_result(
                False,
                "crypto",
                "Only BITCOIN or ETHEREUM please ",
        )
        '''
        else:
            crypto = str(crypto).upper()
            url = f"https://api.alternative.me/v2/ticker/{crypto}/?convert=USD"

            #get the stock price of the crypto
    
            response = requests.get(url).json()
            if crypto == 'BITCOIN': price = response['data']['1']['quotes']['USD']['price']
            if crypto == 'ETHEREUM': price = response['data']['1027']['quotes']['USD']['price']
            
            return build_validation_result(
                True,
                'buy_or_sell',
                "The price of {} is {} ".format(
                    crypto, price,
                )
            )

        '''
    # Validate the buy_or_sell, it should be >= 1
    
    if buy_or_sell is not None: 
        buy_or_sell = str(buy_or_sell).upper()
        print (f'buy_or_sell is {buy_or_sell}')
        if buy_or_sell !='BUY' and buy_or_sell !='SELL':
            return build_validation_result(
                False,
                "buy_or_sell",
                "Pls enter either BUY or SELL please ",
        )
            
    if number_of_shares is not None:
        number_of_shares = parse_int(
            number_of_shares
        )  # Since parameters are strings it's important to cast values
        if number_of_shares < 1:
            print (f'NUMBER of SHARES {number_of_shares}')
            return build_validation_result(
                False,
                "number_of_shares",
                "one or more shares please ",
            )
    '''
    # Validate if a correct curerency was passed
    if riskLevel is not None:
        riskLevel = str(riskLevel).upper()
        if riskLevel not in ["NONE", "LOW", "MEDIUM", 'HIGH']:
            return build_validation_result(
                False,
                "riskLevel",
                "Sorry, risk levels are NONE, LOW, MEDIUM, or HIGH,"
                "Please enter the risk level you are comfortable with.",
            )
    '''
    # A True results is returned if age or investmentAmount and riskLevel are valid
    # A true reults if correct crypto is entered
    
    
    return build_validation_result(True, None, None)

def build_validation_result(is_valid, violated_slot, message_content):
    """
    Define a result message structured as Lex response.
    """
    if message_content is None:
        return {"isValid": is_valid, "violatedSlot": violated_slot}

    return {
        "isValid": is_valid,
        "violatedSlot": violated_slot,
        "message": {"contentType": "PlainText", "content": message_content},
    }


### Dialog Actions Helper Functions ###
def get_slots(intent_request):
    """
    Fetch all the slots and their values from the current intent.
    """
    return intent_request["currentIntent"]["slots"]


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    """
    Defines an elicit slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "ElicitSlot",
            "intentName": intent_name,
            "slots": slots,
            "slotToElicit": slot_to_elicit,
            "message": message,
        },
    }


def delegate(session_attributes, slots):
    """
    Defines a delegate slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {"type": "Delegate", "slots": slots},
    }


def close(session_attributes, fulfillment_state, message):
    """
    Defines a close slot type response.
    """

    response = {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": fulfillment_state,
            "message": message,
        },
    }

    return response


"""
Step 3: Enhance the Robo Advisor with an Amazon Lambda Function

In this section, you will create an Amazon Lambda function that will validate the data provided by the user on the Robo Advisor.

1. Start by creating a new Lambda function from scratch and name it `recommendPortfolio`. Select Python 3.7 as runtime.

2. In the Lambda function code editor, continue by deleting the AWS generated default lines of code, then paste in the starter code provided in `lambda_function.py`.

3. Complete the `recommend_portfolio()` function by adding these validation rules:

    * The `age` should be greater than zero and less than 65.
    * The `investment_amount` should be equal to or greater than 5000.

4. Once the intent is fulfilled, the bot should respond with an investment recommendation based on the selected risk level as follows:

    * **none:** "100% bonds (AGG), 0% equities (SPY)"
    * **low:** "60% bonds (AGG), 40% equities (SPY)"
    * **medium:** "40% bonds (AGG), 60% equities (SPY)"
    * **high:** "20% bonds (AGG), 80% equities (SPY)"

> **Hint:** Be creative while coding your solution, you can have all the code on the `recommend_portfolio()` function, or you can split the functionality across different functions, put your Python coding skills in action!

5. Once you finish coding your Lambda function, test it using the sample test events provided for this Challenge.

6. After successfully testing your code, open the Amazon Lex Console and navigate to the `recommendPortfolio` bot configuration, integrate your new Lambda function by selecting it in the “Lambda initialization and validation” and “Fulfillment” sections.

7. Build your bot, and test it with valid and invalid data for the slots.

"""


### Intents Handlers ###
def recommend_portfolio(intent_request):
    """
    Performs dialog management and fulfillment for recommending a portfolio.
    """
    #### Changed the code to get all the slots once, and not call get_slots all the time
    slots = get_slots(intent_request)
    crypto = slots["crypto"]
    buy_or_sell = slots["buy_or_sell"]

    number_of_shares = slots["number_of_shares"]
    
    #investment_amount = slots["investmentAmount"]


    # YOUR CODE GOES HERE!

    # Gets the invocation source, for Lex dialogs "DialogCodeHook" is expected.
    source = intent_request["invocationSource"]

    if source == "DialogCodeHook":
        # This code performs basic validation on the supplied input slots.

        # Validates user's input using the validate_data function
        #validation_result = validate_data(age, investment_amount, risk_level, intent_request)

        validation_result = validate_data(crypto, buy_or_sell, number_of_shares, intent_request)

        # If the data provided by the user is not valid,
        # the elicitSlot dialog action is used to re-prompt for the first violation detected.
        if not validation_result["isValid"]:
            slots[validation_result["violatedSlot"]] = None  # Cleans invalid slot

            # Returns an elicitSlot dialog to request new data for the invalid slot
            return elicit_slot(
                intent_request["sessionAttributes"],
                intent_request["currentIntent"]["name"],
                slots,
                validation_result["violatedSlot"],
                validation_result["message"],
            )

        # Fetch current session attributes
        output_session_attributes = intent_request["sessionAttributes"]

        # Once all slots are valid, a delegate dialog is returned to Lex to choose the next course of action.
        return delegate(output_session_attributes, slots)

    # Now make the recommendation based upon the risk_level
    # Now execute the TRADE
    
    recommend = {
        'BITCOIN': "BITCOIN - Good choice",
        'ETHEREUM': "ETHEREUM - Not bad"
    }

    crypto = str(crypto).upper()
    my_order = submit_crypto_order(crypto, buy_or_sell, number_of_shares)
    #url = f"https://api.alternative.me/v2/ticker/{crypto}/?convert=USD"

    #get the stock price of the crypto
    
    #response = requests.get(url).json()
    #if crypto == 'BITCOIN': price = response['data']['1']['quotes']['USD']['price']
    #if crypto == 'ETHEREUM': price = response['data']['1027']['quotes']['USD']['price']


    # Return a message with conversion's result.
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": """You just bought {} shares of {},
           at USD{}. Happy Trading!
            """.format(
                number_of_shares ,crypto, my_order.filled_avg_price
            ),
        },
    )





### Intents Dispatcher ###
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    intent_name = intent_request["currentIntent"]["name"]

    # Dispatch to bot's intent handlers
    if intent_name == "tradeCrypto":
        return recommend_portfolio(intent_request)

    raise Exception("Intent with name " + intent_name + " not supported")


### Main Handler ###
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """

    return dispatch(event)