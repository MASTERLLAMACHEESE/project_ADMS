
def print_on_screen(seq_bits, pad_bits):
    print(f"""
    {'-' * 15}
    {pad_bits[0]} {pad_bits[1]} {pad_bits[2]} {pad_bits[3]}
    {pad_bits[4]} {pad_bits[5]} {pad_bits[6]} {pad_bits[7]}
    {pad_bits[8]} {pad_bits[9]} {pad_bits[10]} {pad_bits[11]}
    {pad_bits[12]} {pad_bits[13]} {pad_bits[14]} {pad_bits[15]}
    {'-' * 15}
    
    {'-' * 15}
    {seq_bits[0]} {seq_bits[1]} {seq_bits[2]} {seq_bits[3]} {seq_bits[4]} {seq_bits[5]} {seq_bits[6]} {seq_bits[7]}
    {seq_bits[8]} {seq_bits[9]} {seq_bits[10]} {seq_bits[11]} {seq_bits[12]} {seq_bits[13]} {seq_bits[14]} {seq_bits[15]}
    {'-' * 15}
    """, end='\033[A' * 12)
