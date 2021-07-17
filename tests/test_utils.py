from utils import bytes_utils


def test_bytes():
    speed_b = 1023
    speed_b_ch = bytes.bytes_to_human(speed_b)
    assert speed_b_ch == '1023B'

    speed_kb = 1024 * 1
    speed_kb_ch = bytes.bytes_to_human(speed_kb)
    assert speed_kb_ch == '1.0KB'

    speed_mb = 1024 * 1024 * 1
    speed_mb_ch = bytes.bytes_to_human(speed_mb)
    assert speed_mb_ch == '1.0MB'

    speed_gb = 1024 * 1024 * 1024 * 1
    speed_gb_ch = bytes.bytes_to_human(speed_gb)
    assert speed_gb_ch == '1.0GB'
