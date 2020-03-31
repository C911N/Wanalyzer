from typing import List, Optional, cast
import datetime as dt

# Internal imports
from .message import Message, append_content


# Messages constants
_MSG_MIN_SIZE =             23
_MSG_OPEN_BRACKET_IDX =     0
_MSG_CLOSE_BRACKET_IDX =    20

# Messages types by the content
_MSG_TYPES_MAP = {
    'sticker omitted': Message.MessageType.STICKER,
    'audio omitted': Message.MessageType.AUDIO,
    'image omitted': Message.MessageType.IMAGE,
    'video omitted': Message.MessageType.VIDEO,
    'image omitted': Message.MessageType.IMAGE,
    'file omitted': Message.MessageType.FILE
}


def parse_messages(file: str) -> Optional[List[Message]]:
    """Parse a messages from a file
    :param file str:        the path to the file to  parse
    :return None:           if the line is malformed
    :return List[Message]:   the parsed messages
    """

    messages: List[Message] = []

    # Open and read the file
    with open(file) as f:
        file_content: List[str] = f.readlines()
        file_content = [x.strip() for x in file_content]

        # Create messages
        for line in file_content:
            msg: Optional[Message] = _parse_msg(line)
            if msg == None:
                msg = append_content(messages.pop(), '\n' + line)
            msg = cast(Message, msg)
            messages.append(msg)

        # Return the messages
        return (messages)
    return (None)


def _parse_msg(line: str) -> Optional[Message]:
    """Parse a message from a line
    :param line str:    the line to parse
    :return None:       if the line is malformed
    :return Message:    the parsed message
    """

    # Fix the first space bug
    if _is_line_msg(line[1:]):
        line = line[1:]

    # Check if the line is a message
    if not _is_line_msg(line):
        return (None)

    # Date parsing
    date_str: str = line[_MSG_OPEN_BRACKET_IDX + 1:_MSG_CLOSE_BRACKET_IDX]
    date: Optional[dt.datetime] = None
    try:
        date = dt.datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')
    except ValueError:
        return (None)

    # Author name end index
    name_end_idx: int = line[_MSG_CLOSE_BRACKET_IDX + 1:].find(':')
    name_end_idx += _MSG_CLOSE_BRACKET_IDX + 1 

    # Message author and content
    author: str = line[_MSG_CLOSE_BRACKET_IDX + 2:name_end_idx]
    content: str = line[name_end_idx + 2:]

    # Determine message type
    msg_type: Message.MessageType = Message.MessageType.TEXT
    for type_match, type_val in _MSG_TYPES_MAP.items():
        if type_match in content:
            msg_type = type_val
            break
    
    # Return the message
    return Message(date=date, author=author, content=content, msg_type=msg_type)


def _is_line_msg(line: str) -> bool:
    """Check if a line is the start of a message
    :param line str:    the line to check
    :return bool:       true if it is a message start
    """

    return not (len(line) < _MSG_MIN_SIZE or \
        line[_MSG_OPEN_BRACKET_IDX] != '[' or \
        line[_MSG_CLOSE_BRACKET_IDX] != ']')
