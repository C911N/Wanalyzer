from typing import List, Dict
import dataclasses as dc

# Internal imports
from ..messages import Message


# Format to print a line of the ascii sheet
_LINE_FORMAT = '| %-8s | %-8d | %-6.2f%%%-11s | %-6.2f%%%-11s |'

# Conversation forward declaration
class Conversation:
    pass


@dc.dataclass
class MemberStat:
    """MemberStat - dataclass to represent a member statistics"""


    # MemberStat class fields
    member_name: str
    member_conv: Conversation
    messages: List[Message]
    msg_count_by_type: Dict[Message.MessageType, List[Message]]


    def display_stats(self):
        """Display the member statistics in an ascii sheet"""

        # Utils constants
        name: str = self.member_name
        msg_count: int = len(self.messages)
        count: int = self.member_conv.get_msg_count()
        percent_in_conv: int = (msg_count / count) * 100
        text: int = self.msg_count_by_type[Message.MessageType.TEXT]
        sticker: int = self.msg_count_by_type[Message.MessageType.STICKER]
        audio: int = self.msg_count_by_type[Message.MessageType.AUDIO]
        image: int = self.msg_count_by_type[Message.MessageType.IMAGE]
        video: int = self.msg_count_by_type[Message.MessageType.VIDEO]
        file: int = self.msg_count_by_type[Message.MessageType.FILE]

        # Display
        print('+' + ('-' * 21) + '+')
        print('| %-19s |' % name.encode('ascii',errors='ignore').decode())
        print('+%s+%s+%s+%s+' % (10 * '-', 10 * '-', 20 * '-', 20 * '-'))
        print('| %-8s | %-8s | %-18s | %-18s |' % ('Type', 'Count', 'Member ratio', 'Conversation ratio'))
        print('+%s+%s+%s+%s+' % (10 * '-', 10 * '-', 20 * '-', 20 * '-'))
        print(_LINE_FORMAT % ('Message', msg_count, 100.00, '', percent_in_conv, ''))
        print(_LINE_FORMAT % ('Text', text, (text / msg_count) * 100, '', (text / count) * 100, ''))
        print(_LINE_FORMAT % ('Sticker', sticker, (sticker / msg_count) * 100, '', (sticker / count) * 100, ''))
        print(_LINE_FORMAT % ('Audio', audio, (audio / msg_count) * 100, '', (audio / count) * 100, ''))
        print(_LINE_FORMAT % ('Image', image, (image / msg_count) * 100, '', (image / count) * 100, ''))
        print(_LINE_FORMAT % ('Video', video, (video / msg_count) * 100, '', (video / count) * 100, ''))
        print(_LINE_FORMAT % ('File', file, (file / msg_count) * 100, '', (file / count) * 100, ''))
        print('+%s+%s+%s+%s+' % (10 * '-', 10 * '-', 20 * '-', 20 * '-'))
