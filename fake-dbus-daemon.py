#!/usr/bin/env python3
# flake8: noqa: F722, F821
import asyncio

from dbus_next.aio import MessageBus
from dbus_next.service import method
from dbus_next.service import ServiceInterface
from dbus_next.service import Variant


DBUS_ID = "org.learningequality.Kolibri.Daemon"
DBUS_PATH = "/" + DBUS_ID.replace(".", "/")
IFACE = "org.learningequality.Kolibri.Daemon.Private"


USERS = {
    "TOKEN1": {
        "username": Variant("s", "adminuser"),
        "fullname": Variant("s", "EOS Admin Users"),
        "uid": Variant("i", 1000),
        "gid": Variant("i", 1000),
        "groups": Variant("as", []),
        "admin": Variant("b", True),
    },
    "TOKEN2": {
        "username": Variant("s", "eosuser"),
        "fullname": Variant("s", "EOS Normal Users"),
        "uid": Variant("i", 1001),
        "gid": Variant("i", 1001),
        "groups": Variant("as", []),
        "admin": Variant("b", False),
    },
}


class ExampleInterface(ServiceInterface):
    @method()
    def GetUserDetails(self, token: "s") -> "a{sv}":
        if token in USERS:
            return USERS[token]

        raise Exception("Invalid Token")


async def main():
    bus = await MessageBus().connect()
    interface = ExampleInterface(IFACE)
    bus.export(DBUS_PATH, interface)
    await bus.request_name(DBUS_ID)
    await asyncio.get_event_loop().create_future()


asyncio.get_event_loop().run_until_complete(main())
