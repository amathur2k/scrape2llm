from api_client import process_url

def main():
    # url = "https://adenlandscaping.com/"
    # url = "https://maisonlafleur.com/"
    url = "https://greenthumb-landscaping.com/"
    word_count, image_count = 100, 4
    
    #This is the function that will process the URL and return the marketing statement and pictures
    marketing_statement, pictures = process_url(url, word_count, image_count)
    
    print(f"\nMarketing Statement:\n{'-' * 50}")
    print(marketing_statement)
    
    print(f"\nPictures URLs:\n{'-' * 50}")
    for i, pic_url in enumerate(pictures, 1):
        print(f"{i}. {pic_url}")

if __name__ == "__main__":
    main() 