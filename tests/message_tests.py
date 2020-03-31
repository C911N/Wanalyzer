import datetime
from unittest import TestCase
from wanalyzer.messages.message import Message, append_content


_TYPING_ERROR_FORMAT = 'Typing test error (mypy)\n\n\n%s'


class MessageTest(TestCase):
    """Tests of the wanalyzer.messages.message.py file"""

    def test_message_constructor(self):
        """Message constructor"""

        message: Message = Message(date=datetime.date.min,
            author='Author',
            content='Content',
            msg_type=Message.MessageType.TEXT)

        # Test the attributes
        self.assertEqual(message.date, datetime.date.min, 'message.date != datetime.date.min')
        self.assertEqual(message.author, 'Author', 'message.author != \'Author\'')
        self.assertEqual(message.content, 'Content', 'message.content != \'Content\'')
        self.assertEqual(message.msg_type, Message.MessageType.TEXT, 'message.msg_type != Message.MessageType.TEXT')


    def test_message_append_content(self):
        """Message append_content"""

        message: Message = Message(date=datetime.date.min,
            author='Author',
            content='Content',
            msg_type=Message.MessageType.TEXT)
        new_message: Message = append_content(message, 'Append')
        
        # Test the attributes
        self.assertEqual(message.date, new_message.date, 'message.date != new_message.date')
        self.assertEqual(message.author, new_message.author, 'message.author != new_message.author')
        self.assertEqual(new_message.content, 'ContentAppend', 'new_message.content != \'ContentAppend\'')
        self.assertEqual(message.msg_type, new_message.msg_type, 'message.msg_type != new_message.msg_type')