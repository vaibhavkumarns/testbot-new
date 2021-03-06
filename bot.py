from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount


class MyBot(ActivityHandler):

    async def on_message_activity(self, turn_context: TurnContext):
        print(turn_context.activity.text)
        await turn_context.send_activity(f"You said '{ turn_context.activity.text }' (from azure env)")

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello! What can I do for you?")
