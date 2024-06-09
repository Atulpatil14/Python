import argparse,subprocess as ss

parser = argparse.ArgumentParser(description="This is test tool")

parser.add_argument("-c",type=str, help="Provide Command", required=True)

a = parser.parse_args()

ss.call(a.c, shell=True)
