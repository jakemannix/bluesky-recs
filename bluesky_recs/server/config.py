import os

SERVICE_DID = os.environ.get("SERVICE_DID", None)
HOSTNAME = os.environ.get("HOSTNAME", None)


class MissingHostnameError(RuntimeError):
    def __init__(self):
        super().__init__('You should set "HOSTNAME" environment variable first.')


class MissingFeedUriError(RuntimeError):
    def __init__(self):
        super().__init__(
            "Publish your feed first (run publish_feed.py) to obtain Feed URI. "
            'Set this URI to "WHATS_ALF_URI" environment variable.'
        )


if HOSTNAME is None:
    raise MissingHostnameError()

if SERVICE_DID is None:
    SERVICE_DID = f"did:web:{HOSTNAME}"


WHATS_ALF_URI = os.environ.get("WHATS_ALF_URI")
if WHATS_ALF_URI is None:
    raise MissingFeedUriError()
