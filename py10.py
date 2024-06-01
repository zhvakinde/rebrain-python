import os,time, logging, argparse
dict_1 = dict(os.environ)
parser = argparse.ArgumentParser()
parser.add_argument('-num', default=10, type=int, help='number of lines')
parser.add_argument('-delay', default=2, type=float, help='delay')
args = parser.parse_args()
logging.basicConfig(filename='log_file.log', format='%(asctime)s  %(levelname)s  %(message)s', datefmt='%b %d %H:%M:%S', level=logging.INFO)
for key, value in list(dict_1.items())[:args.num]:
            logging.info(f'{key} -> {value}')
            time.sleep(args.delay)

