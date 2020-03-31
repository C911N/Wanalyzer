# Wanalyzer

![Tests](https://github.com/C911N/Wanalyzer/workflows/Tests/badge.svg)

Wanalyzer is a simple Python module providing tools to **parse** and **analyze** exported WhatsApp conversations (via the `Export Chat` feature of WhatsApp).

## Installation

To install **Wanalyzer**, you can simply use ``pip install analyser`` or use the `setup.py` python script.
And import it to your project with `import wanalyzer as wa` 

## Usage


### Parsing
You can choose between:
- Using the provided conversation parser and send the *file path* as `str` to the `Conversation` constructor.
- Do the parsing part yourself and send a `List[Message]` to the `Conversation` constructor (can be useful if your input formatting is not exactly the same as the WhatsApp exported chat feature).

**Message dataclass description**
| Attribute | Type         | Description                             |
| ----------|--------------|-----------------------------------------|
| date      | `datetime`   | Time (precise with secs) of the message |
| author    | `str`        | Author of the message                   |
| content   | `str`        | Content of the message                  |
| msg_type  | `MessageType`| Type of the message                     |

`Message.MessageType` can be `TEXT`, `STICKER`, `AUDIO`, `IMAGE`, `VIDEO`, or `FILE`.


### Filtering
You are able to create your own filters of type `Callable[[Message], bool]`: It have to be a function taking the `Message` as parameter, and return `false` if it have to be removed from the analysed conversation.

Some built-in filters as already available:
- `filter__min_size`: Remove all messages less than the given size.
- `filter__from_authors`: Remove all messages that are not from the given authors.
- `filter__contains_texts`: Remove all messages not containing any of the given texts.
- `filter__not_contains_texts`: Remove all messages containing any of the given texts.

### Statistics

Wanalyzer provide both *member* based, and *time* based statistics tools.

**Member Statistics**

With the `Conversation.get_members_stats()` method, you can get a `List[MemberStat]` describing the *statistics of each member of the conversation*.

The `MemberStat` dataclass gives informations about the messages sent by the member.

**MemberStat dataclass description**

| Attribute          | Type                                | 
| -------------------|:-----------------------------------:|
| member_name        | `str`                               |
| member_conv        | `str`                               | 
| messages           | `List[Message]`                     |
| msg_count_by_type  | `Dict[MessageType, int]`  |

The `msg_count_by_type` attribute provide the messages count of each type.

**Time scale splitting**

With the `Conversation.get_split_by(scale: TimeScale)` method, you can get a `Dict[datetime, Conversation]` dictionary that split the original conversation into smaller ones, taking the messages sorted by the given `TimeScale`: `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE` or `SECOND`.

## Contributing

*Pull requests are **opened*** to add any kind of features or improvements in the code.
Please **make sure that all the regression tests are passing** (using `test.sh`) and to **clean the repository** (using `clean.sh`) before submitting your pull request.

