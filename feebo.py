import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Feebo Command Line Tool")
    parser.add_argument('--rating', type=int, default=1600, help='The rating to use for the Codeforces problemset')

    args = parser.parse_args()
    rating = args.rating

    # Open Sublime Text
    os.system('subl /home/aniket/code/codeforces.sublime-workspace')
    
    # Open Chrome with the specified link
    os.system(f'google-chrome https://codeforces.com/problemset?tags={rating}-{rating}')

if __name__ == "__main__":
    main()
