# Encoded By Tir Bap
# https://github.com/BLACKGANG1M

import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))