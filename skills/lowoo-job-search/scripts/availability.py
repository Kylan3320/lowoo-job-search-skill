"""Join a Chinese graduation/degree phrase to its availability commitment."""
import re
import sys

BOUNDARY = re.compile(
    r"((?:20)?[0-9]{2}\s*届(?:\s*(?:本科|硕士|博士|研究生)(?:生)?)?)"
    r"[ \t]*[,，][ \t]*(?=(?:可(?:以)?|能(?:够)?)(?:稳定|每周|连续|全职|实习|到岗|出勤|工作))"
)

if __name__ == "__main__":
    source = sys.stdin.buffer.read().decode("utf-8-sig")
    sys.stdout.buffer.write(BOUNDARY.sub(r"\1", source).encode("utf-8"))
