from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionEmailSetup(Action):

    def name(self) -> Text:
        return "action_email_setup"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


# class ValidateContactForm(FormValidationAction):
#     def __init__(self, *args):
#         super(ValidateContactForm, self).__init__(*args)
        
