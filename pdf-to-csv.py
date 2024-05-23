import argparse
import camelot
import json


# Read remote pdf into list of DataFrame 
def parse_pdf(file_path, configs):
    for config in configs:
        tables = camelot.read_pdf(file_path, flavor='stream', **config)
        tables.export('output.csv', f='csv', compress=False)
        # camelot.plot(tables[0], kind='grid').show()

def load_config(config_path, bank):
    print(config_path)
    with open(config_path, 'r') as file:
        data = json.load(file)
        return data.get(bank)
    

def parse_args():
    """Set up and return the argument parser."""
    parser = argparse.ArgumentParser(description="Process some PDFs.")
    parser.add_argument('-f', '--file', type=str, help='Your PDF file path')
    parser.add_argument('--config', type=str, default='pdf-config.json')
    parser.add_argument('--bank', type=str)
    return parser.parse_args()

def main():
    """Main function that uses parsed arguments."""
    args = parse_args()  # Parse arguments
    configs = load_config(args.config, args.bank)
    print(configs)
    parse_pdf(args.file, configs)

if __name__ == "__main__":
    main()