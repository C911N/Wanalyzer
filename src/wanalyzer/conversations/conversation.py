from typing import List, Callable, Dict, Union, Optional, cast
import datetime as dt

# Internal imports
from ..messages import Message, filter_msgs, parse_messages
from ..utils import TimeScale, compare_time_by_scale, reset_time_by_scale
from .member_stat import MemberStat


# Default value of the type dict
_MSG_COUNT_BY_TYPE_DEFAULT = {
    Message.MessageType.TEXT: 0,
    Message.MessageType.STICKER: 0,
    Message.MessageType.AUDIO: 0,
    Message.MessageType.IMAGE: 0,
    Message.MessageType.VIDEO: 0,
    Message.MessageType.FILE: 0
}


class Conversation:
    """Conversation - used for manipulating the messages"""


    def __init__(self, messages: Union[List[Message], str]):
        """Conversation constructor
        :param messages List[Message]:  the messages of the conversation
        :param messages str:            the file to load messages from
        """

        self._messages: List[Message] = []
        if isinstance(messages, str):
            messages = cast(str, messages)
            parsed_messages: Optional[List[Message]] = parse_messages(messages)
            if parsed_messages == None:
                pass # TODO: Throw
            else:
                self._messages = cast(List[Message], parsed_messages)
        else:
            messages = cast(List[Message], messages)
            self._messages = messages

        # TODO: Trow error on less than 2 messages
        self._members: List[str] = []
        self._members_stat: List[MemberStat] = []
        self._split_by_scale: Dict[dt.datetime, Conversation] = {}


    def _load_members(self):
        """Load the members from the messages
        :set _members List[str]:    the members of the conversation
        """

        self._members.clear()
        for msg in self._messages:
            if msg.author not in self._members:
                self._members.append(msg.author)


    def _load_members_stat(self):
        """Load the member statistics from the messages
        :set _members_stat [MemberStat]:    the statistics of each members
        """

        self._members_stat.clear()
        for member in self._members:
            messages: [Message] = []
            msg_count_by_type: dict = _MSG_COUNT_BY_TYPE_DEFAULT

            # Get message counts by type
            for msg in self._messages:
                if msg.author != member:
                    continue
                messages.append(msg)
                msg_count_by_type[msg.msg_type] += 1

            # Build the MemberStat
            member_stat: MemberStat = MemberStat(member_name=member,
                member_conv=self,
                messages=messages.copy(),
                msg_count_by_type=msg_count_by_type.copy())
            self._members_stat.append(member_stat)

            # Clear message and msg_count_by_type
            messages.clear()
            for key in msg_count_by_type.keys():
                msg_count_by_type[key] = 0


    def _load_split_by_scale(self, scale: TimeScale):
        """Load the splitted conversations for a given time scale
        :param scale TimeScale:                                 the time scale used to sort the conversations
        :set _split_by_scale Dict[dt.datetime, Conversation]:   the splitted conversation
        """

        self._split_by_scale.clear()
        split_by_scale_msgs: Dict[dt.datetime, List[Message]] = {}
        for msg in self._messages:
            scaled_date: dt.datetime = reset_time_by_scale(scale, msg.date)
            if not scaled_date in split_by_scale_msgs:
                split_by_scale_msgs[scaled_date] = []
            split_by_scale_msgs[scaled_date].append(msg)

        # Create the conversations
        for msg_scale, messages in split_by_scale_msgs.items():
            self._split_by_scale[msg_scale] = Conversation(messages)


    def get_messages(self) -> List[Message]:
        """Get the messages of the conversation
        :return List[Message]:  the messages of the conversation 
        """
        return self._messages


    def get_msg_count(self) -> int:
        """Get the number of messages in the conversation
        :return int:    the number of messages in the conversation
        """
        return len(self._messages)


    def get_members(self) -> List[str]:
        """Get the members of the conversation
        :return List[str]:  the members of the conversation
        """
        self._load_members()
        return self._members


    def get_members_stat(self) -> List[MemberStat]:
        """Get the statistics of the members of the conversation
        :return List[MemberStat]:   the statistics of the members of the conversation
        """
        self._load_members()
        self._load_members_stat()
        return self._members_stat


    def get_split_by(self, scale: TimeScale) -> Dict[dt.datetime, 'Conversation']:
        """Get the conversation splitted by a time scale
        :return Dict[dt.datetime, Conversation]:    the conversation splitted by a time scale
        """  
        self._load_split_by_scale(scale)
        return self._split_by_scale


    def filter(self, *filters: Callable[[Message], bool]):
        """Apply a filter on the conversation messages
        :param *filters Callable[[Message], bool]:  the filters to apply to the messages
        """
        self._messages = filter_msgs(self._messages, *filters)


    def display(self):
        """Display each message of the conversation"""
        for msg in self._messages:
            print('({}) From {}: {}'.format(msg.date, msg.author, msg.content))
