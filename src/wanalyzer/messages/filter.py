from typing import List, Callable

# Internal imports
from .message import Message


# Remove all messages less than size
def filter__min_size(size: int) -> Callable[[Message], bool]:
    return (lambda msg: len(msg.content) >= size)

# Remove all messages not from the author
def filter__from_authors(*authors: str) -> Callable[[Message], bool]:
    def _msg_from_authors(msg: Message) -> bool:
        for author in authors:
            if msg.author == author:
                return (True)
        return (False)
    return _msg_from_authors

# Remove all messages not containing any of the texts
def filter__contains_texts(ignorecare=False, *texts: str) -> Callable[[Message], bool]:
    def _msg_contains_texts(msg: Message) -> bool:
        for text in texts:
            text_to_find: str = text.lower() if ignorecare else text
            to_check: str = msg.content.lower() if ignorecare else msg.content
            if text_to_find in to_check:
                return (True)
        return (False)
    return _msg_contains_texts

# Remove all messages containing any of the texts
def filter__not_contains_texts(ignorecare=False, *texts: str) -> Callable[[Message], bool]:
    def _msg_not_contains_texts(msg: Message) -> bool:
        for text in texts:
            text_to_find: str = text.lower() if ignorecare else text
            to_check: str = msg.content.lower() if ignorecare else msg.content
            if text_to_find in to_check:
                return (False)
        return (True)
    return _msg_not_contains_texts


def filter_msgs(messages: List[Message], *filter_funcs: Callable[[Message], bool]) -> List[Message]:
    """Apply multiple filters to messages
    :param messages List[Message]:                  the messages to filter
    :param *filter_funcs Callable[[Message], bool]: the filters to apply
    :return List[Message]:                          the filtered messages
    """

    result: List[Message] = messages
    for filter_func in filter_funcs:
        result = _apply_filter(result, filter_func)
    return (result)


def _apply_filter(messages: List[Message], filter_func: Callable[[Message], bool]) -> List[Message]:
    """Apply a filter to messages
    :param messages List[Message]:                  the messages to filter
    :param filter_func Callable[[Message], bool]:   the filter to apply
    :return List[Message]:                          the filtered messages
    """

    result: List[Message] = []
    for msg in messages:
        if filter_func(msg):
            result.append(msg)
    return (result)
