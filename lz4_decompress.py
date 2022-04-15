#!/usr/bin/python3

import sys, struct, lz4.block, os.path

def main():
	if len(sys.argv) != 2:
		sys.exit("[i] Usage: " + sys.argv[0]  + " in_file.dll")

	in_file = sys.argv[1]

	with open(in_file, "rb") as compressed_file:
		compressed_data = compressed_file.read()

	header = compressed_data[:4]

	if header.decode('utf-8') != 'XALZ':
		sys.exit("[!] Wrong header, aborting...!")

	packed_payload_len = compressed_data[8:12]
	unpacked_payload_len = struct.unpack('<I', packed_payload_len)[0]
	compressed_payload = compressed_data[12:]
	decompressed_payload = lz4.block.decompress(compressed_payload, uncompressed_size=unpacked_payload_len)

	out_file = in_file.rsplit(".",1)[0] + "_out.dll"

	if os.path.isfile(out_file):
		sys.exit("[!] Output file [" + out_file  + "] already exists, aborting...!")

	with open(out_file, "wb") as decompressed_file:
		decompressed_file.write(decompressed_payload)
		print("[i] Success!")
		print("[i] File [" + out_file + "] was created as result!")

if __name__ == "__main__":
	main()
