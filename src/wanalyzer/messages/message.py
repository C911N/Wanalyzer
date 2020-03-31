import enum
import dataclasses as dc
import datetime as dt


@dc.dataclass
class Message:
    """MessageType - dataclass to represent a message data"""


    class MessageType(enum.Enum):
        """MessageType - Enum to represent the different types of messages
        :extends Enum:
        """

        TEXT = 0
        STICKER = 1
        AUDIO = 2
        IMAGE = 3
        VIDEO = 4
        FILE = 5


    # Message field
    date: dt.datetime
    author: str
    content: str
    msg_type: MessageType


def append_content(msg: Message, content: str) -> Message:
    """Create a copy of the message with content appened to it
    :param msg Message: the message to copy
    :param str content: the content to appen
    :return Message:    message with the appened content
    """
    return Message(date=msg.date, author=msg.author, content=msg.content + content, msg_type=msg.msg_type)